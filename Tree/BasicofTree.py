class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 2
        prefix = spaces + "__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_product_tree():
    root = TreeNode("Stream")

    Science = TreeNode("Science")
    Science.add_child(TreeNode("Tech"))
    Science.add_child(TreeNode("Medical"))

    Commerce = TreeNode("Commerce")
    Commerce.add_child(TreeNode("Accounts"))
    Commerce.add_child(TreeNode("Business"))

    Arts = TreeNode("Arts")
    Arts.add_child(TreeNode("Educator"))
    Arts.add_child(TreeNode("Artist"))

    root.add_child(Science)
    root.add_child(Commerce)
    root.add_child(Arts)

    root.print_tree()

if __name__ == '__main__':
    build_product_tree()