from enum import Enum
from random import *

#For characters. Includes dice stuff too.

# Valid symbols to add to a die.
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
    sides=[]
    modsides=[]
    def __init__(self,*newsides):
        """Each character has a die associated with it. This die represents
        the character's abilities and health. Faces of the die may be "covered"
        when affected by damage."""
        for k in newsides:
            if isinstance(k,Symbol):
                self.sides.append(k);
            else:
                print(type(k));
                raise ValueError("Tried to add a non-symbol to a die: "+str(k)+" of type "+str(type(k)));
        for i in range(len(self.sides)):
            print(i)
            self.modsides.append(None);

    def roll(self):
        """Returns a side from the die. No need to check side count. Also
        ensures that a modified side is returned, if any."""
        result = randrange(len(self.sides));
        try:
            if self.modsides[result] != None:
                return self.modsides[result];
            else:
                return self.sides[result];
        except IndexError:
            return self.sides[result];

    def modify(self,replace):
        """Replaces a random side with a modifier 'replace'. Only picks sides that aren't already modified."""
        done=False;
        if not isinstance(replace, Symbol):
            raise ValueError("Tried to replace a die face with a non-symbol value!");
        while not done:
            result = randrange(len(self.sides));
            try:
                if self.modsides[result] == None:
                    self.modsides[result] = replace;
                    done = True;
            except IndexError:
                self.modsides[result] = replace;
                done = True;

    def getSides(self):
        """Returns a table with either the Sides or ModSides value for each face of the die."""
        sidelist = self.sides;
        for i in range(len(self.sides)):
            try:
                if self.modsides[i] != None:
                    sidelist[i] = self.modsides[i];
            except IndexError:
                sidelist.append(self.sides[i]);
        return sidelist;

if __name__ == "__main__": # Time to test dice.
    die = Dice(Symbol.GUN,Symbol.MELEE,Symbol.SCI,Symbol.CULT,Symbol.MOVE,Symbol.DEF)
    print(die.roll(),"Roll");
    die.modify(Symbol.STUN);
    print("Die modified with STUN");
    print(die.getSides());
