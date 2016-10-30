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

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def size(self):
        current = self.head
        count = 0
        if self.head is None:
            return 0
        current = current.get_next()
        count += 1
        while current is not self.head:
            count += 1
            current = current.get_next()
        return count

    def add_end(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.head.set_next(new_node)
            return
        current = self.head
        while current.get_next() != self.head:
            current = current.get_next()
        current.set_next(new_node)
        new_node.set_next(self.head)
        current.set_next(new_node)

    def add_head(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.head.set_next(new_node)
            return
        current = self.head
        while current.get_next() != self.head:
            current = current.get_next()
        current.set_next(new_node)
        new_node.set_next(self.head)
        current.set_next(new_node)
        self.head = new_node

    def del_end(self):
        if self.head is None:
            print('List Empty')
            return
        current = self.head
        temp = self.head
        if current == current.get_next():
            self.head = None
            del current
            return
        while current.get_next() != self.head:
            temp = current
            current =current.get_next()
        temp.set_next(current.get_next())
        del current

    def del_head(self):
        if self.head is None:
            print('List Empty')
            return
        current = self.head
        temp = self.head
        if current == current.get_next():
            self.head = None
            del current
            return
        while current.get_next() != self.head:
            current =current.get_next()
        current.set_next(self.head.get_next())
        self.head = self.head.get_next()
        del temp


    def __repr__(self):
        current = self.head
        l = []
        if current is not None:
            l.append(current.data)
            current = current.get_next()
            while current != self.head:
                l.append(current.data)
                current = current.get_next()
        return str(l)
