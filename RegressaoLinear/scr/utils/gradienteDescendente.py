import numpy  as np
import pandas as pd
import matplotlib.pyplot as plt

def gradienteDescendenteUnicaVariavel(valoresX,YReal,valorA,valorB,numIter=100,taxaAprendizado=0.01):
    erroQuadradoMedio = []

    for iteracao in range(numIter):
        YPred = (valorA*valoresX) + valorB               # Equação da Reta ax + b. Pegando valor previsto de um dado Xi
        derivadaA = sum((valoresX*(YPred-YReal)))
        derivadaB = sum(((YPred-YReal)))
        valorA = valorA - (derivadaA*taxaAprendizado*(1/len(valoresX)))
        valorB = valorB - (derivadaB*taxaAprendizado*(1/len(valoresX)))
        erroQuadradoMedio.append((np.sum(((YPred-YReal)**2)))/len(valoresX))
    
    return valorA,valorB,erroQuadradoMedio


def equacaoRegressaoLinear(thetas,features):
    Ypred = [] 
    nameColumns = list(features.columns)
    for i in range(1,len(thetas)):
        equacaoAtual = thetas[i]*features[nameColumns[i-1]]
        if i == 1:
            Ypred = equacaoAtual #1
        else:
            Ypred = [(a+b) for a,b in zip(Ypred,equacaoAtual)]
    
    return np.array(Ypred) + thetas[0]

def derivadasParciais(thetas,features,target,Ypred):
    nameColumns = list(features.columns)
    derivadas = []
    for i in range(0,len(thetas)):
        if i == 0:
            derividaParcial = np.sum((Ypred-target))/len(features)
        else:
            derividaParcial = np.sum(((Ypred-target)*features[nameColumns[i-1]]))/len(features)
        derivadas.append(derividaParcial)
    return derivadas

def atualizaThetas(derivadasParciais,thetas,taxaAprendizado):
    thetasAtualizados = []
    for derivadaParcial,thetaAtual in zip(derivadasParciais,thetas):
        theta =  thetaAtual - (taxaAprendizado * derivadaParcial)
        thetasAtualizados.append(theta)
    return thetasAtualizados

def erroQuadradoMedio(Ypred,target):
    return ((np.sum(((Ypred-target)**2)))/(2*len(target)))

def gradienteDescendente(features,target,thetas,numIter=100,taxaAprendizado=0.01):
    erro = []
    
    for iteracao in range(numIter):
        Ypred = equacaoRegressaoLinear(thetas,features)
        derivadasParcial = derivadasParciais(thetas,features,target,Ypred)
        thetas = atualizaThetas(derivadasParcial,thetas,taxaAprendizado)
        erro.append(erroQuadradoMedio(Ypred,target))
    
    return thetas,erro

def equacaoNormal(features,target):
    array_ums = np.ones(len(features),int)
    X = np.matrix([array_ums,features['TamanhoCasa'],features['NumeroQuartos']]).transpose()
    Xtransposta = X.transpose()
    y = np.matrix([target['PrecoCasa']]).transpose()

    thetas = np.linalg.inv(Xtransposta*X)*Xtransposta*y
    thetas = [float(thetas[0]), float(thetas[1]), float(thetas[2])]
    Ypred = equacaoRegressaoLinear(thetas,features)
    return thetas, erroQuadradoMedio(Ypred,target['PrecoCasa'])
    