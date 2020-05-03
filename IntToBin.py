# Convert Integer to Binary Using A Stack
#Example Application of a Stack


from stack import Stack

def convert(num:int):
    b=Stack()
    binNum=""
    while num > 0 :
        rem=num%2
        b.push(rem)
        num = num // 2
    
    while not b.isEmpty():
        binNum+=str(b.pop())

    print(binNum)
if __name__ == "__main__":
    a=input('Enter the Integer Number to Be converted: ')
    convert(int(a))

