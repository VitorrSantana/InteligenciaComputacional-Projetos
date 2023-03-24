import numpy  as np
import pandas as pd

def gradienteDescendente(valoresX,YReal,valorA,valorB,numIter=100,taxaAprendizado=0.001):
    erroQuadradoMedio = []

    for iteracao in range(numIter):
        YPred = (valorA*valoresX) + valorB               # Equação da Reta ax + b. Pegando valor previsto de um dado Xi
        derivadaA = sum((valoresX*(YPred-YReal)))
        derivadaB = sum(((YPred-YReal)))
        valorA = valorA - (derivadaA*taxaAprendizado*(1/len(valoresX)))
        valorB = valorB - (derivadaB*taxaAprendizado*(1/len(valoresX)))
        erroQuadradoMedio.append((1/len(valoresX)*np.sum((YPred-YReal)**2)))
    
    return valorA,valorB,erroQuadradoMedio
   
