# Stack Data Structure
# Modifying a Traditional Python List
# Last In First Out

class Stack():

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item) #Pushes the Element to the Stack

    def pop(self):
        self.items.pop() #Pops the top-most Element of the Stack

    def viewStack(self):
        return self.items #Returns All the elements of a Stack

    def isEmpty(self):
        return self.items == []
    
    def viewTopElement(self):
        return self.items[-1]

a = Stack() #Object Initialisation
print(a.isEmpty()) #Returns True because the Stack is Empty
a.push(1) #Pushes Element to the Stack
a.push(2) #Pushes Element to the Stack
a.push(3) #Pushes Element to the Stack
print("Top Most Element of Stack: " + str(a.viewTopElement()))
print (a.viewStack())
a.pop()
print (a.viewStack())
print(a.isEmpty())
