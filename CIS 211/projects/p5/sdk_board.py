"""
Hunter McMahon
project 5
Following instruction from: https://github.com/CIS-UO/Duck_Sudoku/blob/master/doc/HOWTO.md
TBH i prefer minesweeper and solitaire
"""

from sdk_config import CHOICES, UNKNOWN, ROOT
from sdk_config import NROWS, NCOLS
import logging
import enum
from typing import Sequence, List, Set

# change the level to logging.INFO to disable debug messages
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

# the above imports are also given in the instructions on github, pep8 just didnt like the comment to be above them
# given code for SDK_board.py
# can be found on https://github.com/CIS-UO/Duck_Sudoku/blob/master/doc/HOWTO.md
"""
A Sudoku board holds a matrix of tiles.
Each row and column and also sub-blocks
are treated as a group (sometimes called
a 'nonet'); when solved, each group must contain
exactly one occurrence of each of the
symbol choices.
"""


# --------------------------------
#  The events for MVC
# --------------------------------

class Event(object):
    """Abstract base class of all events, both for MVC
    and for other purposes.
    """
    pass


# ---------------
# Observer (base class)
# ---------------

class Observer(object):
    """Abstract base class for observers.
    Subclass this to make the notification do
    something useful.
    """

    def __init__(self):
        """Default constructor for simple observers without state"""
        pass

    def notify(self, event: Event):
        """The 'notify' method of the base class must be
        overridden in concrete classes.
        """
        raise NotImplementedError("You must override Observer.notify")


# --------------------------------------
# Events and observers for Tile objects
# --------------------------------------

class EventKind(enum.Enum):
    TileChanged = 1
    TileGuessed = 2


class TileEvent(Event):
    """
    Abstract base class for things that happen to tiles. We always indicate the tile.
    Concrete subclasses indicate the nature of the event.
    """

    def __init__(self, tile: 'Tile', kind: EventKind):
        self.tile = tile
        self.kind = kind
        # Note 'Tile' type is a forward reference;
        # Tile class is defined below

    def __str__(self):
        """Printed representation includes name of concrete subclass"""
        return f"{repr(self.tile)}"


class TileObserver(Observer):
    """Observers that need to receive TileEvents, like our view component"""

    def notify(self, event: TileEvent):
        raise NotImplementedError("TileObserver subclass needs to override notify(TileEvent)")


class Observable:
    """Objects to which observers (like a view component) can be attached"""

    def __init__(self):
        self.observers = []

    def add_observer(self, observer: Observer):
        self.observers.append(observer)

    def notify_all(self, event: Event):
        for observer in self.observers:
            observer.notify(event)


# ----------------------------------------------
#      Tile class
# ----------------------------------------------

class Tile(Observable):
    """
    One tile on the Sudoku grid.
    Public attributes (read-only): value, which will be either
    UNKNOWN or an element of CHOICES; candidates, which will
    be a set drawn from CHOICES.  If value is an element of
    CHOICES,then candidates will be the singleton containing
    value.  If candidates is empty, then no tile value can
    be consistent with other tile values in the grid.
    value is a public read-only attribute; change it
    only through the access method set_value or indirectly
    through method remove_candidates.
    """

    def __init__(self, row: int, col: int, value=UNKNOWN):
        # function is given by https://github.com/CIS-UO/Duck_Sudoku/blob/master/doc/HOWTO-START.md
        super().__init__()
        assert value == UNKNOWN or value in CHOICES
        self.value = None
        self.candidates = None
        self.row = row
        self.col = col
        self.set_value(value)

    def set_value(self, value: str):
        # function is given by https://github.com/CIS-UO/Duck_Sudoku/blob/master/doc/HOWTO-START.md
        if value in CHOICES:
            self.value = value
            self.candidates = {value}
        else:
            self.value = UNKNOWN
            self.candidates = set(CHOICES)
        self.notify_all(TileEvent(self, EventKind.TileChanged))

    # done by me:

    def __str__(self) -> str:
        """
        gives string of the tile instance
        :return: the value of the tile instance
        """
        return self.value

    def __repr__(self) -> str:
        """
        returns a string representing the call for the tile instance
        :return: a string representing the call for the tile instance
        """
        return f"Tile({self.row}, {self.col}, '{self.value}')"

    def could_be(self, value: str) -> bool:
        """True if value is a candidate value for this tile"""
        # function given by https://github.com/CIS-UO/Duck_Sudoku/blob/master/doc/HOWTO-START.md
        return value in self.candidates

    def __hash__(self) -> int:
        """Hash on position only (not value)"""
        # function given by https://github.com/CIS-UO/Duck_Sudoku/blob/master/doc/HOWTO-START.md
        return hash((self.row, self.col))

    def remove_candidates(self, used_values: Set[str]) -> bool:
        """The used values cannot be a value of this unknown tile.
        We remove those possibilities from the list of candidates.
        If there is exactly one candidate left, we set the
        value of the tile.

        Args:
            used_values:  set of values that cannot be candidates
        Returns:
            True means we eliminated at least one candidate,
            False means nothing changed (none of the 'used_values' was in our candidates set).
        """
        # function is given by https://github.com/CIS-UO/Duck_Sudoku/blob/master/doc/HOWTO-PROPAGATE.md
        new_candidates = self.candidates.difference(used_values)
        if new_candidates == self.candidates:
            # Didn't remove any candidates
            return False
        self.candidates = new_candidates
        if len(self.candidates) == 1:
            self.set_value(new_candidates.pop())
        self.notify_all(TileEvent(self, EventKind.TileChanged))
        return True


# start of board class given by https://github.com/CIS-UO/Duck_Sudoku/blob/master/doc/HOWTO-START.md
# ------------------------------
#  Board class
# ------------------------------

class Board(object):
    """A board has a matrix of tiles"""

    def __init__(self):
        """The empty board"""
        # function is mostly given by https://github.com/CIS-UO/Duck_Sudoku/blob/master/doc/HOWTO-START.md
        # Row/Column structure: Each row contains columns
        self.tiles: List[List[Tile]] = []
        for row in range(NROWS):
            cols = []
            for col in range(NCOLS):
                cols.append(Tile(row, col))
            self.tiles.append(cols)
        self.groups = []
        self.set_groups()

    def set_tiles(self, tile_values: Sequence[Sequence[str]]):
        """Set the tile values a list of lists or a list of strings"""
        # function is given by https://github.com/CIS-UO/Duck_Sudoku/blob/master/doc/HOWTO-START.md
        for row_num in range(NROWS):
            for col_num in range(NCOLS):
                tile = self.tiles[row_num][col_num]
                tile.set_value(tile_values[row_num][col_num])

    def set_groups(self):
        """
        creates the groups for the groups instance variable
        :return:
        """
        # function is mostly given by https://github.com/CIS-UO/Duck_Sudoku/blob/master/doc/HOWTO-START.md
        # copy the rows to the instance variable (given):
        for row in self.tiles:
            self.groups.append(row)
        # copy the columns into groups (done by me)
        for i in range(NCOLS):
            column = []
            for r in range(NROWS):
                column.append(self.tiles[r][i])
            self.groups.append(column)
        # create the list of blocks (given)
        for block_row in range(ROOT):
            for block_col in range(ROOT):
                group = []
                for row in range(ROOT):
                    for col in range(ROOT):
                        row_addr = (ROOT * block_row) + row
                        col_addr = (ROOT * block_col) + col
                        group.append(self.tiles[row_addr][col_addr])
                self.groups.append(group)

    def __str__(self) -> str:
        """In Sadman Sudoku format"""
        # given by https://github.com/CIS-UO/Duck_Sudoku/blob/master/doc/HOWTO-GUESS.md
        return "\n".join(self.as_list())

    def as_list(self) -> List[str]:
        """Tile values in a format compatible with
        set_tiles.
        """
        # given by https://github.com/CIS-UO/Duck_Sudoku/blob/master/doc/HOWTO-GUESS.md
        row_syms = []
        for row in self.tiles:
            values = [tile.value for tile in row]
            row_syms.append("".join(values))
        return row_syms

    def is_consistent(self) -> bool:
        """
        checks to see if there are duplicates in the groups
        :return: a boolean indicating if the board contains duplicates and is inconstant
        True: there are no duplicated symbols
        False: there are duplicated symbols
        """
        # pseudo code provided by https://github.com/CIS-UO/Duck_Sudoku/blob/master/doc/HOWTO-START.md
        for i in self.groups:
            used_symbols = []
            for t in i:
                if t.value in CHOICES:
                    if t.value == UNKNOWN:
                        continue
                    if t.value in used_symbols:
                        # board is not consistent
                        return False
                    used_symbols.append(t.value)
        # the solved part of the board is ok so far
        return True

    def naked_single(self) -> bool:
        """Eliminate candidates and check for sole remaining possibilities.

        Returns:
            True means we crossed off at least one candidate.
            False means we made no progress.
        """
        # docstring given by https://github.com/CIS-UO/Duck_Sudoku/blob/master/doc/HOWTO-PROPAGATE.md
        progress = False
        for i in self.groups:
            used_symbols = []
            for t in i:
                if t.value in CHOICES:
                    used_symbols.append(t.value)
            for t in i:
                if t.value == UNKNOWN:
                    progress = t.remove_candidates(used_symbols) or progress
        return progress

    def hidden_single(self) -> bool:
        """
        A Hidden Single is a single candidate remaining
        for a specific digit in a row, column or box.
        this function finds them
        :return:
        True if progress has been made
        False if otherwise
        """
        # pseudo code provided by https://github.com/CIS-UO/Duck_Sudoku/blob/master/doc/HOWTO-PROPAGATE.md
        progress = False
        for i in self.groups:
            leftovers = set(CHOICES)
            for t in i:
                if t.value in CHOICES:
                    leftovers.discard(t.value)
            for v in leftovers:
                can_go = 0
                for t in i:
                    if t.could_be(v):
                        can_go += 1
                        tile = t
                if can_go == 1:
                    tile.set_value(v)
                    progress = True
        return progress

    def min_choice_tile(self) -> Tile:
        """Returns a tile with value UNKNOWN and
        minimum number of candidates.
        Precondition: There is at least one tile
        with value UNKNOWN.
        """
        # docstring given by https://github.com/CIS-UO/Duck_Sudoku/blob/master/doc/HOWTO-GUESS.md
        current_min = NROWS + 1
        min_op_tile = None
        for i in self.tiles:
            for t in i:
                if t.value == UNKNOWN:
                    if len(t.candidates) < current_min:
                        current_min = len(t.candidates)
                        min_op_tile = t
        return min_op_tile

    def is_complete(self) -> bool:
        """None of the tiles are UNKNOWN.
        Note: Does not check consistency; do that
        separately with is_consistent.
        """
        # docstring given from https://github.com/CIS-UO/Duck_Sudoku/blob/master/doc/HOWTO-GUESS.md
        for i in self.groups:
            for t in i:
                if t.value == UNKNOWN:
                    return False
        return True

    def solve(self):
        """General solver; guess-and-check
        combined with constraint propagation.
        """
        # pseudo-code given by https://github.com/CIS-UO/Duck_Sudoku/blob/master/doc/HOWTO-GUESS.md
        self.propagate()
        if not self.is_consistent():
            return False
        if self.is_complete():
            return True
        current_state = self.as_list()
        tile_of_interest = self.min_choice_tile()
        for i in list(tile_of_interest.candidates):
            tile_of_interest.set_value(i)
            if self.solve():
                return True
            self.set_tiles(current_state)
        return False

    def propagate(self):
        """Repeat solution tactics until we
        don't make any progress, whether or not
        the board is solved.
        """
        # given by https://github.com/CIS-UO/Duck_Sudoku/blob/master/doc/HOWTO-GUESS.md
        progress = True
        while progress:
            progress = self.naked_single()
            self.hidden_single()
        return
