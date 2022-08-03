class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        c = 0
        itr = self.head
        while itr:
            c += 1
            itr = itr.next
        return c

    def print(self):
        if self.head is None:
            print("Empty")
            return
        itr = self.head
        llstr = '0'

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("invalid index")
        if index == 0:
            self.head = self.head.next
            return
        c = 0
        itr = self.head
        while itr:
            if c == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            c += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index selected!")
        if index == 0:
            self.insert_at_begining(data)
        c = 0
        itr = self.head
        while itr:
            if c == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            c += 1


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_begining(5)
    ll.insert_at_begining(15)
    ll.print()
    ll.insert_at_end(75)
    ll.insert_at_end(100)
    ll.insert_values(["nafi", "ashraf", "usa", "bd"])
    ll.print()
    print("length = ", ll.get_length())
    ll.remove_at(3)
    ll.print()
    ll.insert_at(1, "dhaka")
    ll.print()
