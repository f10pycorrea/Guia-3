import numpy as np

def indice(gl, vinc):
	s=[] 
	us=[]
	r=[]
	Fr=[]
	numvinc=np.size(vinc[:,0])
	for i in range (0,numvinc):
		if vinc[i,1]==-1:
			s.append(gl*(vinc[i,0]-1))
			us.append(vinc[i,3])
		if vinc[i,2]==-1:
			s.append(gl*(vinc[i,0]-1)+1)
			us.append(vinc[i,4])
		if vinc[i,1]==1:
			r.append(gl*(vinc[i,0]-1))
			Fr.append(vinc[i,3])
		if vinc[i,2]==1:
			r.append(gl*(vinc[i,0]-1)+1)
			Fr.append(vinc[i,4])
	s=np.sort(s)
	r=np.sort(r)
	return r, Fr,s, us