import sys

def push_front(x, deque):

    new_deque = [0]*(len(deque)+1)

    new_deque[0] = x

    for i in range(1, len(deque)+1):
        
        new_deque[i] = deque[i-1]

    return new_deque

def push_back(x, deque):

    deque.append(x)
    return deque

def pop_front(deque):

    if len(deque)==0:
        print(-1)
        print("\n")
        return []
    else:
        new_deque = [0]*(len(deque)-1)

        print(deque[0])
        print("\n")

        for i in range(len(deque)-1):
            new_deque[i] = deque[i+1]
        return new_deque

def pop_back(deque):

    if len(deque)==0:
        print(-1)
        print("\n")
        return []
    else:
        new_deque = [0]*(len(deque)-1)
        print(deque[len(deque)-1])
        print("\n")

        for i in range(len(deque) - 1):
            new_deque[i] = deque[i]
        return new_deque

def size(deque):

    if len(deque)==0:
        print(0)
        print("\n")
    else: 
        print(len(deque))
        print("\n")

def empty(deque):
    
    if len(deque)==0:
        print(1)
        print("\n")
    else: 
        print(0)
        print("\n")

def front(deque):

    if len(deque)==0:
        print(-1)
        print("\n")
    else: 
        print(deque[0])
        print("\n")

def back(deque):

    if len(deque)==0:
        print(-1)
        print("\n")
    else: 
        print(deque[len(deque)-1])
        print("\n")

if __name__ == "__main__":

    deque = []
    number = int(sys.stdin.readline())

    for _ in range(number):

        command = sys.stdin.readline().split()

        if command[0] == 'push_back':
            deque = push_back(command[1], deque)
        elif command[0] == 'push_front':
            deque = push_front(command[1], deque)
        elif command[0] == 'pop_front':
            deque = pop_front(deque)
        elif command[0] == 'pop_back':
            deque = pop_back(deque)
        elif command[0] == 'size':
            size(deque)
        elif command[0] == 'empty':
            empty(deque)
        elif command[0] == 'front':
            front(deque)
        elif command[0] == 'back':
            back(deque)

