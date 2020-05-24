import numpy as np

def readmsh(nombre):

    algo= open (nombre,'rt')
    line = algo.readline()
    while line:
        line = algo.readline()
        if '$Nodes' in line.strip():
            cantnodos=int(algo.readline().strip())
            MN=np.zeros([cantnodos,3])
            for i in range(cantnodos):
                MN[i,:]=np.fromstring(algo.readline().strip(),dtype=float ,sep=" " )[1:]
        elif '$Elements' in  line.strip():
            cantelem=int(algo.readline().strip())
            ME = []
            for e in range(cantelem):
                aux=np.fromstring(algo.readline().strip(),dtype=int ,sep=" " )
                q_tri=aux[1]
                if q_tri == 2:
                    ME.append(aux[-3:])
            ME=np.array(ME)

    algo.close
    return MN,cantnodos,ME,cantelem
