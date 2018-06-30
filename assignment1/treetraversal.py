 def predorder(tree):
 	if tree:
 		print(tree.getrootval())
 		predorder(tree.leftchild())
 		predorder(tree.rightchild())
 # using the class method

 def predorder(self):
 	print(self.key)
 	if self.leftchild():
 		tree.predorder(self.leftchild)
 	if self.rightchild():
 		tree.predorder(self.rightchild)

def postorder(tree):
	postorder(tree.leftchild)
	postorder(tree.rightchiled)
	print(tree.getrootval())	

# parse tree traversal 
def parsetreeval(tree):
	opers={'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}
	res1=None
	res2=None
	if tree:
		res1=parsetreeval(tree.leftchild())
		res2=parsetreeval(tree.rightchild())
		if res2 and res1:
			return opers[tree.rootval()](res1,res2)
		else:
			return tree.rootval
