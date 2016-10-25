class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

class UnorderdList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def add(self, item, position=1):
        temp = Node(item)
        if position == 1:
            temp.set_next(self.head)
            self.head = temp
        else:
            current = self.head
            current_i = 1
            while current != None and current_i < position:
                current_i += 1
                previous_node = current
                current = current.get_next()
            previous_node.set_next(temp)
            temp.set_next(current)

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def __repr__(self):
        current = self.head
        l = []
        while current != None:
            l.append(current.data)
            current = current.get_next()
        return str(l)
