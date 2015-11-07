import unittest

class BinaryTree():
	def __init__(self,key):
		self.key=key
		self.left=None
		self.right=None	
	
	
	def insert(self,item):
		if item<self.key and self.left:
			self.left.insert(item)
		elif item>self.key and self.right:
			self.right.insert(item)
		elif item < self.key:
			self.insertLeft(item)
		elif item > self.key:
			self.insertRight(item)
		

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

def buildBST():
	b=BinaryTree(50)
	b.insert(20)
	b.insert(60)
	b.insert(30)
	b.insert(10)
	b.insert(70)
	return b



def preorder(tree,acc):
	if tree:
		acc.append(tree.getRootVal())
		acc1=preorder(tree.getLeftChild(),acc)
		return preorder(tree.getRightChild(),acc1)
	else: 
		return acc

def postorder(tree,acc):
	if tree:
		acc1=postorder(tree.getLeftChild(),acc)
		acc2=postorder(tree.getRightChild(),acc1)
		acc2.append(tree.getRootVal())
		return acc2	
	else:
		return acc

def inorder(tree,acc):
	if tree:
		acc1=inorder(tree.getLeftChild(),acc)
		acc1.append(tree.getRootVal())
		return inorder(tree.getRightChild(),acc)
	else:
		return acc


class TreeCase(unittest.TestCase):
	def setUp(self):
		self.tree = buildTree()
		self.bst= buildBST()
	
	def test_tree_insert(self):
		self.assertEqual(self.tree.getRightChild().getRootVal(),"c")
		self.assertEqual(self.tree.getLeftChild().getRightChild().getRootVal(),"d")
		self.assertEqual(self.tree.getRightChild().getLeftChild().getRootVal(),"e")
	
	def test_BST(self):
		self.assertEqual(self.bst.getRightChild().getRootVal(),60)
		self.assertEqual(self.bst.getLeftChild().getRootVal(),20)
		self.assertEqual(self.bst.getRightChild().getRightChild().getRootVal(),70)
		self.assertEqual(self.bst.getLeftChild().getLeftChild().getRootVal(),10)
		self.assertEqual(self.bst.getLeftChild().getRightChild().getRootVal(),30)


	def test_traversal(self):
		self.assertEqual(preorder(self.tree,[]),["a","b","d","c","e","f"])
		self.assertEqual(postorder(self.tree,[]),["d","b","e","f","c","a"])
		self.assertEqual(inorder(self.tree,[]),["b","d","a","e","c","f"])
if __name__ == "__main__":
    unittest.main()
