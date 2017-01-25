# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import math
def minimo(instances):
    m=0
    minim=[0,0,0,0]
    for j in range(0,4):
        for i in range(0,len(instances)):
            if i>0:
                if instances[i][j] < m:m=instances[i][j]
            else:
               m=instances[i][j]
        minim[j]=m
    return minim

def maximo(instances):
    m=0
    maxim=[0,0,0,0]
    for j in range(0,4):
        for i in range(0,len(instances)):
            if i>0:
                if instances[i][j] > m:m=instances[i][j]
            else:
               m=instances[i][j]
        maxim[j]=m
    return maxim

def media(instances):
    media=[0,0,0,0]
    soma=0
    for j in range(0,4):
        for i in range(0,len(instances)):
            soma+=instances[i][j];
        media[j]=soma/len(instances)
    return media

def std(instances,medias):
    sd=[0,0,0,0]
    soma=0
    for j in range(0,4):
        for i in range(0,len(instances)):
            soma+=math.pow(instances[i][j]-medias[j],2)
        sd[j]=math.sqrt(soma/len(instances))
    return sd

def dist_euc(p,q,al):
    dist=0
    soma=0
    for i in range(0,al):
        soma+=math.pow(p[i]-q[i],2)
    dist=math.sqrt(soma)
    return dist

def matrix_diss(instances):
    matrix=[]
    for i in range(0,len(instances)):
        row=[]
        for j in range(0,len(instances)):
            row.append(dist_euc(instances[i],instances[j],4))
        matrix.append(row)
    return matrix