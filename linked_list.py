class List:

    def __init__(self):
        self.nil = ListElement(None)
        self.nil.prev_p = self.nil
        self.nil.next_p = self.nil

    def insert(self, value):    # insert at the beginning of the list
        x = ListElement(value)
        x.next_p = self.nil.next_p
        self.nil.next_p.prev_p = x
        self.nil.next_p = x
        x.prev_p = self.nil

    def print(self):
        x = self.nil.next_p
        while x != self.nil:
            print(x.value)
            x = x.next_p


class ListElement:

    def __init__(self, value, prev_p=None, next_p=None):
        self.value = value
        self.prev_p = prev_p
        self.next_p = next_p


test_list = List()
test_list.insert(5)
test_list.insert(3)
test_list.print()