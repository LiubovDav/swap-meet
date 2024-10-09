import uuid

class Item:
    
    def __init__(self, id=None, condition=0):
        if id == None:
            self.id = uuid.uuid4().int
        else:
            self.id = id
        self.condition = condition

    def get_category(self):
        return "Item"
    
    def __str__(self):
        return f"An object of type Item with id {self.id}."

    def condition_description(self):
        if self.condition == 5:
            return "Best"
        if self.condition == 4:
            return "Very good"
        if self.condition == 3:
            return "Questionable quality, but you can try"
        if self.condition == 2:
            return "Only if you need this particular product"
        if self.condition == 1:
            return "I strongly do not recommend it"
        if self.condition == 0:
            return "Bad"
 