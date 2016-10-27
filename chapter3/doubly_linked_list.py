class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

    def set_prev(self, new_prev):
        self.prev = new_prev

class UnorderdDoublyList:
    def __init__(self):
        self.head = None
        self.prev = None

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
        new_node = Node(item)
        if position == 1:
            new_node.set_next(self.head)
            if self.head is not None:
                new_node.get_next().set_prev(new_node)
            self.head = new_node
        else:
            temp = self.head
            current_i = 1
            while temp.get_next() is not None and current_i < position:
                current_i += 1
                temp = temp.get_next()
                print(current_i)
            if current_i != position:
                print('Desired position does not exist')
                return
            new_node.set_next(temp.get_next())
            new_node.set_prev(temp)
            if temp.get_next() is not None:
                temp.get_next().set_prev(new_node)
            temp.set_next(new_node)

    def delete(self, position):
        temp = self.head
        if temp is None:
            print('List is empty')
            return
        if position == 1:
            self.head = self.head.get_next()
            if self.head is not None:
                self.head.prev = None
            del temp
        current_i = 1
        while temp.get_next() is not None and current_i < position:
            temp = temp.get_next()
            current_i += 1
        if current_i != position:
            print('Desired position does not exist')
            return
        temp2 = temp.get_prev()
        temp2.set_next(temp.get_next())
        if temp.get_next():
            temp.get_next().set_prev(temp2)
            del temp


    def __repr__(self):
        current = self.head
        l = []
        while current != None:
            l.append(current.data)
            current = current.get_next()
        return str(l)
