import numpy as np

#entrada:
	


def esfuerzos(cantelem,ind,factor,matrizmult,u):
	sigma=[]
	for e in range(cantelem):
		aux=matrizmult[e,:]	
		aux.shape=[3,6]
		aux=aux.dot(u[ind[e]])
		aux=factor[e]*aux
		sigma.append(aux)
	sigma=np.array([sigma])
	return sigma
	


