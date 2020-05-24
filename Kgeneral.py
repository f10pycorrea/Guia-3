import numpy as np
from readmsh import readmsh
from matrizB import matrizB

#entrada:
	#MN: matriz de nodos. cantnodos x 3, ubicacion de cada nodo
	#ME: matriz de elementos. cantelem x 3, nodos que forman triangulito
#salida
#Kg: matriz ensamblada general de resolucion
#matrizmult: matriz 3x6, para obtener valores de sigma 
#Nfm:numero de elemento y factor multiplicativo

def Kgeneral(MN,cantnodos,ME,cantelem,nu,E,t):
	d=E/((1-nu**2))
	D=np.array([[1,nu,0],[nu,1,0],[0,0,(1-nu)/2]])
	Kg=np.zeros([2*cantnodos,2*cantnodos])
	matrizmult=[]
	factor=[]
	ind=[]
	for i in range(cantelem):
		xi=MN[ME[i,0]-1,:]
		xj=MN[ME[i,1]-1,:]
		xm=MN[ME[i,2]-1,:]
		area,B=matrizB(xi,xj,xm)
	#matriz de ctes elastcas
		k=np.transpose(B).dot(D)
		k=k.dot(B)
		fm=t*d/(area*2**2)
		a=np.array([2*(ME[i,:]-1)],dtype=int)
		b=np.array([2*(ME[i,:]-1)+1],dtype=int)
		indice=np.array([2*(ME[i,0]-1), 2*(ME[i,0]-1)+1,2*(ME[i,1]-1), 2*(ME[i,1]-1)+1,2*(ME[i,2]-1), 2*(ME[i,2]-1)+1])
		Kg[np.ix_(indice,indice)]=Kg[np.ix_(indice,indice)]+fm*k
	#para definir las matriz multiplicativa		
		aux=D.dot(B)
		matrizmult.append(aux)
		fm2=d/(2*area)
		factor.append(fm2)	
		ind.append(indice)
	matrizmult=np.array(matrizmult)
	ind=np.array(ind)
	return Kg,factor, matrizmult, ind
	


