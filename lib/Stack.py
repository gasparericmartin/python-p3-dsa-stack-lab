class Stack:

    def __init__(self, items = [], limit = 100):
        self.limit = limit
        self.items = items

    def isEmpty(self):
        print(self.items)
        if len(self.items) == 0:
            return True
        else:
            return False

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            return False
            # raise Exception('Not today pal')

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop(len(self.items) - 1)
        else:
            return None

    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def full(self):
        if len(self.items) == self.limit:
            return True
        else:
            return False

    def search(self, target):

        targ_index = -1

        for i in range(len(self.items)):
            if self.items[i] == target:
                targ_index = i
                break
        
        if targ_index != -1:
            return len(self.items) - targ_index -1
        else:
            return targ_index
