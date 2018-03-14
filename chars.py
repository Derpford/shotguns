from enum import Enum

#For characters.
class Symbol(Enum):
    # BASIC TYPES
    GUN=1;#Ranged.
    MELEE=2;#Melee.
    SCI=3;#High-tech stuff.
    CULT=4;#Magic stuff.
    MOVE=5;#Tactical movement.
    DEF=6;#Riot shields, etc
    # DIE MODIFIERS
    STUN=7;#Goes away when rolled.
    WOUND=8;#Only removed by medical treatments.
    BURN=9;#When rolled, randomly moves to another die.
    SICK=10;#When rolled, randomly moves to another face of the die.

class Dice():
    sides={}
    modsides={}
    def __init__(self):
        """Each character has a die associated with it. This die represents
        the character's abilities and health. Faces of the die may be "covered"
        when affected by damage."""

    def roll(self):
        """Returns a side from the die. No need to check side count. Also
        ensures that a modified side is returned, if any."""
        result = random(len(self.sides));
        if self.modsides[result] != None:
            return self.modsides[result];
        else:
            return self.sides[result];

    def modify(self,replace):
        """Replaces a random side with a modifier 'replace'. Only picks sides that aren't already modified."""
        done=False;
        if not replace is Symbol:
            raise ValueError("Tried to replace a die face with a non-symbol value!");
        while not done:
            result = random(len(self.sides));
            if self.modsides[result] == None:
                self.modsides[result] = replace;
                done = True;
        

