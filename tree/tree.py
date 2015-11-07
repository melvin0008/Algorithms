import unittest

class BinaryTree():
	def __init__(self,key):
		self.key=key
		self.left=None
		self.right=None

	def insertLeft(self,l):
		if self.left==None:
			self.left=BinaryTree(l)
		else:
			t=BinaryNode(l)
			t.left=self.left
			self.left=t

	def insertRight(self,l):
		if self.right==None:
			self.right=BinaryTree(l)
		else:
			t=BinaryNode(l)
			t.right=self.right
			self.right=t

	def getRightChild(self):
		return self.right

	def getLeftChild(self):
		return self.left

	def setRootVal(self,o):
		self.key=o

	def getRootVal(self):
		return self.key


def buildTree():
	r=BinaryTree('a')
	r.insertLeft('b')
	r.insertRight('c')
	r.getLeftChild().insertRight("d")
	r.getRightChild().insertLeft("e")
	r.getRightChild().insertRight("f")
	return r

class TreeCase(unittest.TestCase):
	def setUp(self):
		self.tree = buildTree()
	
	def test_tree_insert(self):
		self.assertEqual(self.tree.getRightChild().getRootVal(),"c")
		self.assertEqual(self.tree.getLeftChild().getRightChild().getRootVal(),"d")
		self.assertEqual(self.tree.getRightChild().getLeftChild().getRootVal(),"e")

if __name__ == "__main__":
    unittest.main()
