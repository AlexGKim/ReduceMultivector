# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import numpy
mB = numpy.array([[1,2],[3,4],[5,6],[7,8],[9,10]])
norm = numpy.linalg.norm(mB,axis=0)
mB = mB/norm

(U, S, V) = numpy.linalg.svd(mB)
for i in range(5):
    for j in range(i+1,5):
        print(i,j, U[i,0]*U[j,1], mB[i,0]*mB[j,1]-mB[i,1]*mB[j,0])

wef
(U2, S, V) = numpy.linalg.svd(mB)
for i in range(5):
    for j in range(i+1,5):
        print(i,j, U[i,0]*U[j,1], U2[i,0]*U2[j,1])

wef
mB = numpy.array([[2,1],[4,3],[6,5],[8,7],[10,9]])
(U, S, V) = numpy.linalg.svd(mB)
for i in range(5):
    for j in range(i+1,5):
        print(i,j, U[i,0]*U[j,1], U[i,1]*U[j,0])

for j in range(2):
    for i in range(5):
        print(j,i,numpy.dot(mB[:,j],U[:,i]))



# print(numpy.linalg.qr(mB))