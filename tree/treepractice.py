import unittest
from collections import deque

class BinaryTree():
	def __init__(self,key):
		self.key=key
		self.left=None
		self.right=None	

	def insertLeft(self,newNode):
		if not self.left:
			self.left=BinaryTree(newNode)
		else:
			temp=BinaryTree(newNode)
			temp.left=self.left
			self.left=temp

	def insertRight(self,newNode):
		if not self.right:
			self.right=BinaryTree(newNode)
		else:
			temp=BinaryTree(newNode)
			temp.left=self.left
			self.left=temp

	def getLeftChild(self):
		return self.left

	def getRightChild(self):
		return self.right

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

def search(root,key):
	if not root:
		return 0
	if root.key==key:
		return 1
	temp=search(root.left,key)
	if temp:
		return 1
	else:
		return search(root.right,key)

def height(root):
	if not root:
		return 0
	return max(height(root.left),height(root.right))+1

def deepestNode(root):
	if not root:
		return 0
	q=deque([root])
	while q:
		node=q.pop()
		if node.left:
			q.appendleft(node.left)
		if node.right:
			q.appendleft(node.right)
	return node.key

def deleteNode(root,key):
	n=deepestNode(root)
	if not n:
		return
	q=deque([root])
	while q:
		node=q.pop()
		if node.key==key:
			node.key=n
		if node.left:
			q.appendleft(node.left)
		if node.right:
			q.appendleft(node.right)
	del node
	return root

def diameter(root):
	if not root:
		return 0
	l=height(root.left)
	r=height(root.right)
	dl=diameter(root.left)
	dr=diameter(root.right)
	return max(l+r+1,dl,dr)


class TreeCase(unittest.TestCase):
	def setUp(self):
		self.tree = buildTree()
		# self.deltedTree=deleteNode(buildTree(),"d")

	def test_tree_insert(self):
		self.assertEqual(self.tree.getRightChild().getRootVal(),"c")
		self.assertEqual(self.tree.getLeftChild().getRightChild().getRootVal(),"d")
		self.assertEqual(self.tree.getRightChild().getLeftChild().getRootVal(),"e")

	def test_search(self):
		self.assertEqual(search(self.tree,"d"),1)
		self.assertEqual(search(self.tree,"f"),1)

	def test_height(self):
		self.assertEqual(height(self.tree),3)

	def test_deepest_node(self):
		self.assertEqual(deepestNode(self.tree),"f")

	def test_diameter(self):
		self.assertEqual(diameter(self.tree),5)

	# def test_deleteNode(self):
	# 	self.assertEqual(search(self.deltedTree,"d"),0)

if __name__ == "__main__":
    unittest.main()