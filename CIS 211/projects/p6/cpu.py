"""
CIS 211
Project 6
Hunter McMahon
All code is given by the instructions for the project except for the functions/methods:
- the SUB, MUl & Divide portion of the ALU ops
- Exec Method
"""

from instr_format import Instruction, OpCode, CondFlag, decode
from typing import Tuple
from memory import Memory
from register import Register, ZeroRegister
from mvc import MVCEvent, MVCObservable
import logging

"""
Duck Machine model DM2022W CPU
"""

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


class ALU(object):
    """The arithmetic logic unit (also called a "functional unit"
    in a modern CPU) executes a selected function but does not
    otherwise manage CPU state. A modern CPU core may have several
    ALUs to boost performance by performing multiple operations
    in parallel, but the Duck Machine has just one ALU in one core.
    """
    # The ALU chooses one operation to apply based on a provided
    # operation code.  These are just simple functions of two arguments;
    # in hardware we would use a multiplexer circuit to connect the
    # inputs and output to the selected circuitry for each operation.
    ALU_OPS = {
        OpCode.ADD: lambda x, y: x + y,
        # For division, use // for floor division
        OpCode.SUB: lambda x, y: x - y,
        OpCode.DIV: lambda x, y: x // y,
        OpCode.MUL: lambda x, y: x * y,
        # For memory access operations load, store, the ALU
        # performs the address calculation
        OpCode.LOAD: lambda x, y: x + y,
        OpCode.STORE: lambda x, y: x + y,
        # Some operations perform no operation
        OpCode.HALT: lambda x, y: 0
    }

    def exec(self, op: OpCode, in1: int, in2: int) -> Tuple[int, CondFlag]:
        """
        handles the execution of the CPU
        :param op: an OpCode object that tells the function what to do with in1 and in2
        :param in1: an integer to be operated on
        :param in2: an integer to be operated on
        :return:
        a tuple with the result of the operation and a condition flag so that the status of the result is known
        """
        operation = self.ALU_OPS[op]
        zero_error = False
        if op == OpCode.DIV and in2 == 0:
            result = 0
            zero_error = True
        else:
            result = operation(in1, in2)
        condition = None
        if result == 0:
            if zero_error:
                condition = CondFlag.V
            else:
                condition = CondFlag.Z
        elif result < 0:
            condition = CondFlag.M
        elif result > 0:
            condition = CondFlag.P
        log.debug(condition)
        return result, condition


class CPUStep(MVCEvent):
    """CPU is beginning step with PC at a given address"""

    def __init__(self, subject: "CPU", pc_addr: int, instr_word: int, instr: Instruction) -> None:
        super().__init__(subject)
        self.subject = subject
        self.pc_addr = pc_addr
        self.instr_word = instr_word
        self.instr = instr


class CPU(MVCObservable):
    """Duck Machine central processing unit (CPU)
    has 16 registers (including r0 that always holds zero
    and r15 that holds the program counter), a few
    flag registers (condition codes, halted state),
    and some logic for sequencing execution.  The CPU
    does not contain the main memory but has a bus connecting
    it to a separate memory.
    """

    def __init__(self, memory: Memory):
        """
        initiator function for the cpu class
        :param memory: the duck machine memory object
        """
        super().__init__()
        # Not part of CPU; what we really have is a connection
        self.memory = memory
        self.registers = [ZeroRegister(), Register(), Register(), Register(),
                          Register(), Register(), Register(), Register(),
                          Register(), Register(), Register(), Register(),
                          Register(), Register(), Register(), Register()]
        self.condition = CondFlag.ALWAYS
        self.halted = False
        self.alu = ALU()
        self.pc = self.registers[15]

    def step(self):
        """
        the step function, handles the fetch, decode and execution
        :return: void
        """
        instr_addr = self.pc.get()
        instr_word = self.memory.get(instr_addr)
        # Decode
        instr = decode(instr_word)
        log.debug(self.pc)
        log.debug(instr)
        # Display the CPU state when we have decoded the instruction,
        # before we have executed it
        self.notify_all(CPUStep(self, instr_addr, instr_word, instr))
        # execution:
        predicate = instr.cond
        if predicate & self.condition:
            log.debug("predicate passed")
            left_reg = self.registers[instr.reg_src1].get()
            right_reg = instr.offset + self.registers[instr.reg_src2].get()
            result = self.alu.exec(instr.op, left_reg, right_reg)
            self.pc.put(self.pc.get() + 1)
            # store the value
            if instr.op.value == 2:
                self.memory.put(result[0], self.registers[instr.reg_target].get())
            elif instr.op.value == 1:
                self.registers[instr.reg_target].put(self.memory.get(result[0]))
            elif instr.op.value == 0:
                self.halted = True
            else:
                self.registers[instr.reg_target].put(result[0])
                self.condition = result[1]
        else:
            self.pc.put(self.pc.get() + 1)

    def run(self, from_addr=0, single_step=False) -> None:
        """
        handles the running of programs
        :param from_addr: the starting addr
        :param single_step: determines if input taken ig
        :return: void
        """
        self.halted = False
        self.pc.put(from_addr)
        step_count = 0
        while not self.halted:
            if single_step:
                input("Step {}; press enter".format(step_count))
            self.step()
            step_count += 1
