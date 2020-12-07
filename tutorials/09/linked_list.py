class LinkedListNode:
    def __init__(self, item, previous=None, next=None):
        self.item = item
        self.previous = previous
        self.next = next

class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None

    def add_first(self, item):
        current_head = self._head
        self._head = LinkedListNode(item, next=current_head)
        
        if current_head == None:
            self._tail = self._head

    def add_last(self, item):
        current_tail = self._tail
        self._tail = LinkedListNode(item, previous=current_tail)

        if current_tail == None:
            self._head = self._tail

    def remove(self, item):
        current = self._head
        while current != None:
            if current.item == item:
                current.previous.next = current.next
            current = current.text

    def forward(self):
        current = self._head
        items = []
        while current != None:
            items.append(current.item)
            current = current.next
        return items

linkedList = LinkedList()
linkedList.add_first(1)
linkedList.add_first(2)
linkedList.add_first(3)
linkedList.add_last(3)
print(linkedList.forward())