"""
The user has to choose the method on the command line:

   python sse.py  -r     generates the problem by adding rows
"""

import sys
import cplex
from cplex.exceptions import CplexError

# data common to all populateby functions
M = 1000
obj = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 1, 0]
ub = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, cplex.infinity, cplex.infinity]
lb = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -cplex.infinity, -cplex.infinity]
var_type = ["C", "C", "C", "C", "C", "B", "B", "B", "B", "B", "C", "C", ]
colnames = ["x1", "x2", "x3", "x4", "x5", "z1", "z2", "z3", "z4", "z5", "vdef", "vatt"]
rownames = ["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "c11", "c12", "c13", "c14", "c15", "c16",
            "c17"]
rhs = [1.0, 2.0, M - 1, M - 2, M, M - 3, M - 3, 2, 3, 5, 4, 6, M + 2, M + 3, M + 5, M + 4, M + 6]
sense = "EELLLLLGGGGGLLLLL"


# the rownames are the constraints and colnames
# type = ["c", "b"]
# "c" continuous

def populatebyrow(prob):
    prob.objective.set_sense(prob.objective.sense.maximize)

    # lower bounds are all 0.0 (the default)?
    # max u
    # x1, x2 >= 0
    prob.variables.add(obj=obj, ub=ub, lb=lb, names=colnames, types=var_type)

    # Populating row by coefficient
    rows = [[colnames, [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0.0, 0.0]],
            [colnames, [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0.0, 0.0]],
            [colnames, [-5, 0, 0, 0, 0, M, 0, 0, 0, 0, 1, 0.0]],
            [colnames, [0, -7, 0, 0, 0, 0, M, 0, 0, 0, 1, 0.0]],
            [colnames, [0, 0, -3, 0, 0, 0, 0, M, 0, 0, 1, 0.0]],
            [colnames, [0, 0, 0, -9, 0, 0, 0, 0, M, 0, 1, 0.0]],
            [colnames, [0, 0, 0, 0, -10, 0, 0, 0, 0, M, 1, 0.0]],
            [colnames, [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]],
            [colnames, [0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]],
            [colnames, [0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 1]],
            [colnames, [0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 1]],
            [colnames, [0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 1]],
            [colnames, [2, 0, 0, 0, 0, M, 0, 0, 0, 0, 0, 1]],
            [colnames, [0, 4, 0, 0, 0, 0, M, 0, 0, 0, 0, 1]],
            [colnames, [0, 0, 7, 0, 0, 0, 0, M, 0, 0, 0, 1]],
            [colnames, [0, 0, 0, 5, 0, 0, 0, 0, M, 0, 0, 1]],
            [colnames, [0, 0, 0, 0, 9, 0, 0, 0, 0, M, 0, 1]],
            ]

    prob.linear_constraints.add(lin_expr=rows, senses=sense, rhs=rhs, names=rownames)


def sse(pop_method):
    try:
        my_prob = cplex.Cplex()
        if pop_method == "r":
            print("Populated by row")
            populatebyrow(my_prob)
        else:
            raise ValueError('pop_method must be "r"')

        my_prob.solve()
    except CplexError as exc:
        raise

    numcols = my_prob.variables.get_num()

    print()
    # solution.get_status() returns an integer code
    print("Solution status = ", my_prob.solution.get_status(), ":", end=' ')
    # the following line prints the corresponding string
    print(my_prob.solution.status[my_prob.solution.get_status()])

    # printing objective value:
    print("Solution value  = ", my_prob.solution.get_objective_value())

    x = my_prob.solution.get_values()

    # Modify to print answers

    print("Results: ")
    print("The Utilities of the defender and attacker are as follows:")
    print(colnames[10], "= %10f" % (x[10]))
    print(colnames[11], "= %10f" % (x[11]))

    print("The Defenders Equilibrium Strategy Profile is as follows:")
    for j in range(0, 5):
        print(colnames[j], "= %10f" % (x[j]))

    for i in range(5,10):
        if x[i] == 1:
            print("The Attackers best response to the equilibrium defense profile is to attack Target", i-4)
            print("A strong Stackelberg Equilibrium occurs in this scenario")
    my_prob.write("sse.lp")


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ["-r"]:
        print("Usage: lpex1.py -X")
        print("   where X is one of the following options:")
        print("      r          generate problem by row")
        print(" Exiting...")
        sys.exit(-1)
    sse(sys.argv[1][1])
