import numpy as np
from readmsh import readmsh
from matrizB import matrizB
from Kgeneral import Kgeneral
from indice import indice
from esfuerzos import esfuerzos
#from esfuerzos import indice

nombre="puebaplancha.msh"
MN,cantnodos,ME,cantelem= readmsh(nombre)

###constantes
nu=0.3
E=30e6#psi
t=1 #in
K,factor, matrizmult,ind=Kgeneral(MN,cantnodos,ME,cantelem,nu,E,t)
#print K*.91/(375e3)

###cargas
vinc=np.array([[1,-1,-1,0,0],[2,-1,-1,0,0],[3,1,1,5000,0],[4,1,1,5000,0]])
gl=2

###cargas y fuerzas
r,Fr,s,us=indice(gl,vinc)
u=np.zeros(gl*cantnodos)
u[r]=np.linalg.solve(K[np.ix_(r,r)],Fr)
u[s]=us
F=np.zeros(gl*cantnodos)
F[s]=K[s,:].dot(u)
F[r]=Fr
Fmatriz=[]
umatriz=[]
for n in range(cantnodos):
	aux=[F[gl*n],F[gl*n+1],0]
	Fmatriz.append(aux)
	aux2=[u[gl*n],u[gl*n+1],0]
	umatriz.append(aux2)

###esfuerzos
sigma=esfuerzos(cantelem,ind,factor,matrizmult,u)



###guardado de datos





