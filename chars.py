from enum import Enum

#For characters.
class Symbol(Enum):
    GUN=1;
    MELEE=2;
    SCI=3;
    CULT=4;
    MOVE=5;
    DEF=6;

class Dice():
    sides={}
    def __init__(self):
        """Each character has a die associated with it. This die represents
        the character's abilities and health. Faces of the die may be "covered"
        when affected by damage."""

    def roll(self):
        """Returns a side from the die. No need to check side count."""
        return sides[random(len(sides))];
