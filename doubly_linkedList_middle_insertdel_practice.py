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

    def delLast(self):
        if self.empty():
            raise Exception("bad fudge")
        else:
            newTail = self.tail.prevElement

            self.tail = newTail
            self.tail.nextElement = None
            self.size -= 1

    def printList(self):

        current = self.head

        if self.empty():
            return None

        # while (self.head.nextElement is not None):
        while (current.nextElement is not None):
            print(current.data)
            current = current.nextElement

        print(self.tail.data)


    def insertAtIndex(self, data, index):

        newAdd = self.node(data, None, None)

        current = self.head

        position = 0

        if index == 0:
            self.addToFront(data)

        # this doesn't work
        # elif index == self.size - 1:
        #     self.addToBack(data)

        else:

            while position < index:

                current = current.nextElement
                position += 1

            # print("current, ", current.data, "position ", position)

            ahead = current.prevElement
            behind = current

            behind.prevElement = newAdd
            ahead.nextElement = newAdd

            newAdd.nextElement = behind
            newAdd.prevElement = ahead

            self.size += 1

    def deleteAtIndex(self, index):
        current = self.head
        position = 0

        if index == 0:
            self.delFirst()

        elif index == self.size - 1:
            self.delLast()

        else:

            while position < index:
                current = current.nextElement
                position += 1

            ahead = current.prevElement
            behind = current.nextElement

            ahead.nextElement = behind
            behind.prevElement = ahead

            self.size -= 1


ll = linkedList()
ll.addToBack(13)
ll.addToBack(23)
ll.addToBack(33)
ll.addToBack(43)
ll.addToBack(53)
ll.addToBack(63)

ll.deleteAtIndex(2)
#ll.insertAtIndex(1000, 5)

print()
print()

ll.printList()

print()
print("SIZE ", ll.size)

'''
print(ll.head.prevElement)
print(ll.head.data)
print(ll.head.nextElement.data)

print()
print(ll.tail.prevElement.data)
print(ll.tail.data)
print(ll.tail.nextElement)

'''
