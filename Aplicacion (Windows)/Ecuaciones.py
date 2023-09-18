
class LlamaEcuaciones:
    def __init__(self):
        pass
    
    def EcuacionExperimental(self, CoordList, X):
        #ListCoordenadas = CoordenadasPuntos  # (Xa,Ya,Xb,Yb,Xc,Yc,Xd,Yd,Xe,Ye,Xf,Yf,Xi)
        ListCoordenadas = CoordList
        segmento = 1        
        i = 0 
        j = 1
        k = 2
        l = 3
        Xi = X
                             
        while Xi <= ListCoordenadas[10]: 
            
            if Xi >= ListCoordenadas[i] and Xi <= ListCoordenadas[k]:
                #print("Segmento: " + str(segmento) + " hora: " + str(Xi) + " Coordenadas: " + str(ListCoordenadas[i]) + "," + str(ListCoordenadas[j]) + "---" + str(ListCoordenadas[k]) +","+ str(ListCoordenadas[l])  )
                Pendiente = (ListCoordenadas[l] - ListCoordenadas[j]) / (ListCoordenadas[k]-ListCoordenadas[i])
                Yi = (Pendiente * Xi) + (Pendiente  * ListCoordenadas[k] * -1) + (ListCoordenadas[l])
                break
            else:
                segmento = segmento + 1
                i = i+2
                j = j+2
                k = k+2
                l = l+2

        return Yi

#Xi = 0
#w = LlamaEcuaciones()
#for Xi in range (24):
#    listalineal = [0,2,6,2,10,25,14,25,18,2,24,2,Xi]
#    print(w.EcuacionExperimental(listalineal, 18))