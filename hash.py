#
# Lukasz Pokorzyński, Adam Steciuk
# hash.py - hashmap and singly linked list implementation
#

class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        current = self.head
        string = "["
        while current:
            string += "'" + str(current.get_data()) + "'" + ", "
            current = current.get_next()
            if current is None:
                string = string[:-2]
        string += "]"

        return string

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current

    # for testing
    def get_list_as_array(self):
        array = []
        current = self.head
        while current:
            array.append(current.get_data)
            current = current.get_next
        return array

    def delete_first(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def delete_all(self, data):
        current = self.head
        previous = None
        found = False
        while current:
            if current.get_data() == data:
                found = True
                if previous is None:
                    self.head = current.get_next()
                else:
                    previous.set_next(current.get_next())
            else:
                previous = current
            current = current.get_next()


class HashTable:
    def __init__(self, length):
        self.array = [None] * length

    def hash(self, key):
        unicode_sum = 0
        for letter in key:
            unicode_sum += ord(letter)

        length = len(self.array)
        return unicode_sum % length

    def add(self, value):
        index = self.hash(value)
        if self.array[index] is None:
            self.array[index] = LinkedList()
            self.array[index].insert(value)
        else:
            self.array[index].insert(value)

    def longest_list(self):
        length = 0
        for list in self.array:
            if list.size() > length:
                length = list.size()
        return length

    def find(self, value):
        index = self.hash(value)
        self.array[index].search(value)

    def add_all(self, array):
        for v in array:
            self.add(v)

    def delete_first(self, value):
        index = self.hash(value)
        self.array[index].delete_first(value)

    def delete_all(self, value):
        index = self.hash(value)
        self.array[index].delete_all(value)
