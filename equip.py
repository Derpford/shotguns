
# Put the equipment definition here.
class Equipment():
    name = "Missingno Device"
    desc = "Something does not seem right about this equipment."
    def __init__(self):
        """This is the class for Equipment Cards, which provide abilities for
        characters in the game. Cards will have a name, description, et cetera.
        They'll also have a cost function and effect function, and eventually
        an image and stuff."""
        
    def cost(self,room):
        """Checks for and deducts the cost of the card. Returns true if
        the card can be played, or false if the requirements are not there.
        Also contains a reference to the current 'room', which should be
        a combat scene."""
        raise NotImplementedError;

    def effect(self,*target):
        """Called when the cost is confirmed. It takes a target list, which 
        should be a list of actors in the room. Does not return anything."""
        raise NotImplementedError;


