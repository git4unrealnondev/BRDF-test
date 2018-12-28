import numpy as np
a = np.array([[.988767, -.55, .45], [.8888, -.9548754, .45], [.9875, -.93, .45], [.78978876, -.76, .45]])
b = np.array([255,233,211,55])
x = np.linalg.lstsq(a, b, rcond=0)
c=0
temp = []
for eff in x[3]:
	temp.append(x[3][c])
	c +=1
print (temp)
