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


    

