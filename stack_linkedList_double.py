# stack_linkedList_double.py

class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    class node:
        def __init__(self, data, nextElement, prevElement):
            self.data = data
            self.nextElement = nextElement
            self.prevElement = prevElement

    def getSize(self):
        return self.size

    def empty(self):
        if self.getSize() == 0:
            return True
        else:
            return False

    def getFirst(self):
        if self.empty():
            return None
        else:
            return self.head.data

    def getLast(self):
        if self.empty():
            return None
        else:
            return self.tail.data

    def addToFront(self, data):

        newAdd = self.node(data, None, None)

        if self.empty():
            self.head = newAdd
            self.tail = newAdd

        else:

            temp = self.head
            self.head.prevElement = newAdd
            self.head = newAdd
            self.head.nextElement = temp

        self.size += 1

    def delFirst(self):
        if self.empty():
            raise Exception("bad fudge")
        else:
            newHead = self.head.nextElement

            self.head = newHead
            self.head.prevElement = None
            self.size -= 1

    def printList(self):

        current = self.head

        if self.empty():
            return None

        while (current.nextElement is not None):
            print(current.data)
            current = current.nextElement

        print(self.tail.data)

ll = linkedList()
ll.addToFront(13)
ll.addToFront(23)
ll.addToFront(33)
ll.addToFront(43)
ll.addToFront(53)
ll.addToFront(63)

print()
print()

# ll.delFirst()
# ll.addToFront(73)

ll.printList()

print("HEAD ", ll.head.data)
print("TAIL ", ll.tail.data)

print()
print()

'''

print(ll.head.prevElement)
print(ll.head.data)
print(ll.head.nextElement.data)

print()
print(ll.tail.prevElement.data)
print(ll.tail.data)
print(ll.tail.nextElement)

'''
