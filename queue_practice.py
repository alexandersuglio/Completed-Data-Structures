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

    def addToBack(self, data):

        newAdd = self.node(data, None, None)

        if self.empty():
            self.head = newAdd
            self.tail = newAdd

        else:
            temp = self.tail
            self.tail.nextElement = newAdd
            self.tail = newAdd
            self.tail.prevElement = temp

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
ll.addToBack(13)
ll.addToBack(23)
ll.addToBack(33)
ll.addToBack(43)
ll.addToBack(53)
ll.addToBack(63)

print()
print()

ll.delFirst()
ll.addToBack(73)

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
