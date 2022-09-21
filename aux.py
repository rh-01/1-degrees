import util

a = util.Node(1,2,3)
b = util.Node(2,2,1)
#c = util.Node(3,1,1)

#a.frontier = [b]
A = util.StackFrontier()
A = A.add(a)
#A = A.contains_state(1)
#A = A.remove()
A = A.empty()
#A = A.add(b)
print(A)



