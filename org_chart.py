class Node():
    """Node in a tree."""

    def __init__(self, data, children):
        self.data = data
        self.children = children

    def __repr__(self):
        """Reader-friendly representation."""

        return f"<Node {self.data}>"

    def find(self, data):
        """Return node object with this data.

        Start here. Return None if not found.
        """

        to_visit = [self]

        while to_visit:
            current = to_visit.pop()

            if current.data == data:
                return current

            to_visit.extend(current.children)


class Tree():
    """Tree."""

    def __init__(self, root):
        self.root = root

    def __repr__(self):
        """Reader-friendly representation."""

        return f"<Tree root={self.root}>"

    def find_in_tree(self, data):
        """Return node object with this data.

        Start at root.
        Return None if not found.
        """

        return self.root.find(data)
    
    def levels(self):
        return self.level_check(self.root)
    
    def level_check(self, item):
        count = 0
        
        if  isinstance(item, str) :
            return 0
        
        for kid in item.children:
            count += self.level_check(kid)
        return (count + 1)



# resume = Node("resume.txt", [])
# recipes = Node("recipes.txt", [])
# jane = Node("jane/", [resume, recipes])
# server = Node("server.py", [])
# jessica = Node("jessica/", [server])
# users = Node("Users/", [jane, jessica])
# root = Node("/", [users])

# tree = Tree(root)
# print("server.py = ", tree.find_in_tree("server.py"))  # should find
# print("style.css = ", tree.find_in_tree("style.css"))  # should not find

def make_tree(ceo, reports):
    return Tree(Node(ceo, reports))

rnd = Node("Jim", ["Dave"])
call_center = Node("unknown", ["Lacie"])
merit = make_tree("Fred", [rnd, call_center])

print(merit)
print(merit.levels())