class A(object):
	__slots__ = ['x','y']
	sVar = 10
	def __init__(self):
	    self.x = 5
	    z = 12
	    print(z)
	    #	A.sVar = []

class B():
	a = A()
	print (A.sVar)
	print (a.sVar)
	A.sVar = [25,26]
	#print (a.z)
	print (A.__slots__)