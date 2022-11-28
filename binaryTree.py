class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def searchvalue(self, searchValue):
        if searchValue < self.data:
            if self.left:
                return self.left.searchvalue(searchValue)
            else:
                return str(searchValue)+" Not Found"
        elif searchValue > self.data:
            if self.right:
                return self.right.searchvalue(searchValue)
            else:
                return str(searchValue)+" Not Found"
        else:
            return str(self.data)+" is Found"

    def PrintTreeInorder(self):
        if self.data:
            if self.left:
                self.left.PrintTreeInorder()
            print(self.data, end=" "),
            if self.right:
                self.right.PrintTreeInorder()
        else:
            print("No data on tree")

    def PrintTreePreorder(self):
        if self.data:
            print(self.data,  end=" "),
            if self.left:
                self.left.PrintTreePreorder()
            if self.right:
                self.right.PrintTreePreorder()
        else:
            print("No data on tree")

    def PrintTreePostorder(self):
        if self.data:
            if self.left:
                self.left.PrintTreePostorder()
            if self.right:
                self.right.PrintTreePostorder()
            print(self.data,  end=" "),
        else:
            print("No data on tree")


r = Node(50)
r.insert(30)
r.insert(20)
r.insert(40)
r.insert(70)   
r.insert(60)
r.insert(80)
r.insert(0)
r.PrintTreeInorder(), print()
r.PrintTreePreorder(), print()
r.PrintTreePostorder(), print()
print()
print()
print(r.searchvalue(2))
