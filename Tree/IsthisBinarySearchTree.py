""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root):
    ls=[]

    def inorder(root):
        if root!=None:
            inorder(root.left)
            ls.append(root.data)
            inorder(root.right)

    inorder(root)

    ps=set(ls)

    if len(ls)!=len(ps):return False
    if ls==sorted(ls):
        return True