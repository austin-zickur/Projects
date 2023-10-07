import numpy as np
A = np.array([0,1,0],[1,0,1],[0,0,0])
C = np.array([0,.5,0],[.5,0,0],[0,0,.5])
print(A@B)
print(np.dot(B,C))
print(np.inv(A@C))