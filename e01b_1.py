import numpy as np
from readmsh import readmsh
from matrizB import matrizB
from Kgeneral import Kgeneral
from indice import indice
from esfuerzos import esfuerzos

nombre="1b.msh"
MN,cantnodos,ME,cantelem= readmsh(nombre)

nu=0.3
E=30e6#psi

t=1 #in
K,factor, matrizmult,ind=Kgeneral(MN,cantnodos,ME,cantelem,nu,E,t)
#print K*.91/(375e3)

vinc=np.array([[1,-1,-1,0,0],[2,-1,-1,0,0],[3,1,1,5000,0],[4,1,1,5000,0],[5,1,1,0,0]])
gl=2

#cargas y furzas
r,Fr,s,us=indice(gl,vinc)
print cantnodos, cantelem
u=np.zeros(gl*cantnodos)
u[r]=np.linalg.solve(K[np.ix_(r,r)],Fr-K[np.ix_(r,s)].dot(us))
u[s]=us
F=np.zeros(gl*cantnodos)
F[s]=K[s,:].dot(u)
F[r]=Fr

###esfuerzos
sigma=esfuerzos(cantelem,ind,factor,matrizmult,u)


