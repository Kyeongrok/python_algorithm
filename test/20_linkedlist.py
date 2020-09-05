class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

        if self.head.next == None:
            self.head = new_node

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)

    def length(self):
        count = 0
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            count += 1
        return count

    def get(self, index):
        #  index = 0
        if index >= self.length():
            print("index out of range")
            return None

        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                return cur_node.data
            cur_idx += 1

    def delete(self, index):
        # when no data in here delete(0)을 하면
        # out of index가 나오게 >=를 하면 0도 걸리기 때문에 가능
        if index >= self.length():
            print("out of index")
            return None

        # delete(0)을 하면 head 다음에 있는 인덱스를 지웁니다.
        cur_idx = 0
        cur_node = self.head #어차피 head는 data가 음슴
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return
            cur_idx += 1

list = LinkedList()
list.display()

print(list.length())

print(list.get(0))
list.append(10)
list.display()
#
print(list.get(0))
list.delete(1)
list.delete(0)
print(list.get(0))

