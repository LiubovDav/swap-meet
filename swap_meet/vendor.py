class Vendor:

    def __init__(self, inventory=None):
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_id(self, item_id):
        for item in self.inventory:
            if item.id == item_id:
                return item

        return None

    def swap_items(self, other_vendor, my_item, their_item):

        if (my_item in self.inventory) and (their_item in other_vendor.inventory):
            self.inventory.remove(my_item)
            other_vendor.inventory.append(my_item)

            other_vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True
        else:
            return False
            
    # def swap_first_item(self, other_vendor):

    #     if self.inventory is None or other_vendor.inventory is None:
    #         return False
    #     if self.inventory[0] is not None and other_vendor.inventory[0] is not None:
    #         temp = self.inventory[0]
    #         self.inventory.remove(self.inventory[0])
    #         self.inventory.append(other_vendor.inventory[0])
    #         other_vendor.inventory.remove(other_vendor.inventory[0])
    #         other_vendor.inventory.append(temp)
    #         return True

    def swap_first_item(self, other_vendor):

        if self.inventory is None or other_vendor.inventory is None:
            return False

        if len(self.inventory) > 0 and len(other_vendor.inventory) > 0:
            temp = self.inventory[0]
            self.inventory[0] = other_vendor.inventory[0]
            other_vendor.inventory[0 ] = temp
            return True

    def get_by_category(self, category):
        objects_in_category = []

        for item in self.inventory:
            if item.get_category() == category:
                objects_in_category.append(item)

        return objects_in_category

    def get_best_by_category(self, category):
        
        max_condition = -1
        max_condition_item = None

        for item in self.inventory:
            if category == item.get_category() and item.condition > max_condition:
                max_condition = item.condition
                max_condition_item = item

        return max_condition_item

    def swap_best_by_category(self, other_vendor, my_category, their_category):
        my_best_item = self.get_best_by_category(their_category)

        if my_best_item == None:
            return False

        other_best_item = other_vendor.get_best_by_category(my_category)

        if other_best_item == None:
            return False

        self.swap_items(other_vendor, my_best_item, other_best_item)

        return True
