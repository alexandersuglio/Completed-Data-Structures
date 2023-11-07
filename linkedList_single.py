# linkedList_single.py

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    class node:
        def __init__(self, data, nextElement):

            self.data = data
            self.nextElement = nextElement

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

    def add(self, data):

        newAdd = self.node(data, None)

        if self.empty():
            self.head = newAdd
            self.tail = newAdd

        else:
            self.tail.nextElement = newAdd
            self.tail = newAdd

        self.size += 1

    def delFirst(self):
        if self.empty():
            raise Exception("bad fudge")

        else:

            newHead = self.head.nextElement
            self.head = None
            self.head = newHead


    def printList(self):

        current = self.head

        if self.empty():
            return None

        # while (self.head.nextElement is not None):
        while (current.nextElement is not None):
            print(current.data)
            current = current.nextElement

        print(self.tail.data)


ll = linkedList()
ll.add(13)
ll.add(23)
ll.add(33)
ll.add(43)
ll.add(53)

print()

ll.printList()

print()

print()

ll.delFirst()

ll.printList()

print("HEAD", ll.getFirst())
print("TAIL", ll.getLast())
