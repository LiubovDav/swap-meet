import uuid

class Item:
    
    def __init__(self, id=None):
        if id == None:
            self.id = uuid.uuid4().int
    