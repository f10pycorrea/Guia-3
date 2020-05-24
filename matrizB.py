import numpy as np

def matrizB(xi,xj,xm):
	indice=np.arange(3)
	B=np.zeros([3,6])
	beta=np.array([xj[1]-xm[1], xm[1]-xi[1], xi[1]-xj[1]])
	gama=np.array([xm[0]-xj[0], xi[0]-xm[0], xj[0]-xi[0]])
	B[0,2*indice]=beta
	B[1,2*indice+1]=gama
	B[2,[2*indice,2*indice+1]]=[gama,beta]
	v1=xj-xi
	v2=xm-xi
	area=0.5*np.linalg.norm(np.cross(v1,v2))
	return area,B