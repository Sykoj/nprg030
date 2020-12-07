class LinkLinkedNode:
    def __init__(self, item, previous=None, next=None):
        self.item = item
        self.previous = previous
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_first(self, item):
        new_first = LinkLinkedNode(item, next=self.head)
        
        if self.head == None:
            self.tail = new_first
            self.head = new_first
        else:
            self.head.previous = new_first
            self.head = new_first

    def add_last(self, item):
        new_last = LinkLinkedNode(item, previous=self.tail)

        if self.tail == None:
            self.tail = new_last
            self.head = new_last
        else:
            self.tail.next = new_last
            self.tail = new_last

    def remove(self, item):
        current = self.head
        while current != None:
            if current.item == item:
                
                # Fix neighbours
                if current.next != None:
                    current.next.previous = current.previous
                if current.previous != None:
                    current.previous.next = current.next                
                
                # Fix head and tail
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.previous

            current = current.next

    def forward(self):
        current = self.head
        result = []
        while current != None:
            result.append(current.item)
            current = current.next
        return result


class StringLinkedList(LinkedList):

    def join(self, delim):
        current = self.head
        result = ""
        while current != None:
            result += current.item
            current = current.next
        return result

class NumberCollectionUtils:

    @staticmethod
    def remove(collection):
        
        pass



linkedList = LinkedList()
linkedList.add_first(1)
linkedList.add_first(2)
linkedList.add_first(3)
linkedList.add_last(3)
print(linkedList.forward())

