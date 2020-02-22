import unittest


class List:

    def __init__(self):
        self.nil = ListElement(None)
        self.nil.prev_p = self.nil
        self.nil.next_p = self.nil

    def insert(self, x):    # insert at the beginning of the list
        x.next_p = self.nil.next_p
        self.nil.next_p.prev_p = x
        self.nil.next_p = x
        x.prev_p = self.nil

    def insert_value(self, value):
        x = ListElement(value)
        self.insert(x)

    @staticmethod
    def delete(x):
        x.prev_p.next_p = x.next_p
        x.next_p.prev_p = x.prev_p

    def delete_value(self, value):
        x = self.search(value)
        self.delete(x)

    def search(self, value):
        x = self.nil.next_p
        while (x != self.nil) & (x.value != value):
            x = x.next_p
        if x == self.nil:
            return None
        return x

    def print(self):
        x = self.nil.next_p
        while x != self.nil:
            print(x.value)
            x = x.next_p

    def to_list(self):
        l = list()
        x = self.nil.next_p
        while x != self.nil:
            l.append(x.value)
            x = x.next_p
        return l


class ListElement:

    def __init__(self, value, prev_p=None, next_p=None):
        self.value = value
        self.prev_p = prev_p
        self.next_p = next_p


class TestLinkedList(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(List().to_list(), [])

    def test_insert(self):
        test_list = List()
        test_list.insert_value(10)
        self.assertEqual(test_list.to_list(), [10])

    def test_search(self):
        test_list = List()
        test_list.insert_value(10)
        self.assertEqual(test_list.search(10).value, 10)
        self.assertEqual(test_list.search(9), None)

    def test_delete(self):
        test_list = List()
        test_list.insert_value(10)
        test_list.insert_value(11)

        test_list.delete_value(10)
        self.assertEqual(test_list.to_list(), [11])
        with self.assertRaises(AttributeError):
            test_list.delete_value(14)


if __name__ == '__main__':
    unittest.main()
