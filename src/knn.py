# Modulo KNN 
import math
import operator
import random

def minimo(instances):
    m=0
    minim=[]
    length = len(instances[0])-1
    for j in range(0,length):
        for i in range(0,len(instances)):
            if i>0:
                if instances[i][j] < m:m=instances[i][j]
            else:
               m=instances[i][j]
        minim.append(m)
    return minim

def maximo(instances):
    m=0
    maxim=[]
    length = len(instances[0])-1
    for j in range(0,length):
        for i in range(0,len(instances)):
            if i>0:
                if instances[i][j] > m:m=instances[i][j]
            else:
               m=instances[i][j]
        maxim.append(m)
    return maxim

def media(instances):
    media=[]
    soma=0
    length = len(instances[0])-1
    for j in range(0,length):
        for i in range(0,len(instances)):
            soma+=instances[i][j];
        media.append(soma/len(instances))
        soma=0
    return media

def std(instances,medias):
    sd=[]
    soma=0
    length = len(instances[0])-1
    for j in range(0,length):
        for i in range(0,len(instances)):
            soma+=math.pow(instances[i][j]-medias[j],2)
        sd.append(math.sqrt(soma/(len(instances)-1)))
        soma=0
    return sd

def dist_euc(p,q,al):
    dist=0
    soma=0
    for i in range(0,al):
        soma+=math.pow(p[i]-q[i],2)
    dist=math.sqrt(soma)
    return dist

def matrix_sim(instances):
    matrix=[]
    for i in range(0,len(instances)):
        row=[]
        for j in range(0,len(instances)):
            row.append(dist_euc(instances[i],instances[j],4))
        matrix.append(row)
    return matrix

def get_neighbors(test,t_set,k):
    dist=[]
    length=len(test)-1
    for x in range(len(t_set)):
        d=dist_euc(test,t_set[x],length)
        dist.append((t_set[x],d))
    dist.sort(key=operator.itemgetter(1))
    neighbors=[]
    for x in range(k):
        neighbors.append(dist[x][0])
    return neighbors
    
def get_resposta(neighbors):
    class_votes={}
    for x in range(len(neighbors)):
        resposta = neighbors[x][-1]
        if resposta in class_votes:
            class_votes[resposta]+=1
        else:
            class_votes[resposta]=1
    votos=sorted(class_votes.items(),key=operator.itemgetter(1),reverse=True)
    return votos[0][0]

def get_accuracy(testSet,predicts):
    certas=0
    for x in range(len(testSet)):
        if testSet[x][-1] == predicts[x]:
            certas+=1
    return (certas/float(len(testSet)))*100.0

def normalize(lista,mn,mx):
    norm=[]
    length = len(lista[0])
    for x in range(len(lista)):
        tup=[]
        for y in range(length):
            if y <=3:
                j = ((lista[x][y]-mn[y])/(mx[y]-mn[y]))
                tup.append(j)
            else:
                s = lista[x][y]
                tup.append(s)
        norm.append(tup)
    return norm
    
def normalize_z(lista,med,sd):
    norm=[]
    length = len(lista[0])
    for x in range(len(lista)):
        tup=[]
        for y in range(length):
            if y <=3:
                attr = ((lista[x][y]-med[y])/sd[y])
                tup.append(attr)
            else:
                s = lista[x][y]
                tup.append(s)
        norm.append(tup)
    return norm
acclist=[]
def prediction(test,training,k):
    neighbors=[]
    predictions=[]
    for i in range(len(test)):
        neighbors=get_neighbors(test[i],training,k)
        result = get_resposta(neighbors)
        predictions.append(result)
        print('> adivinhada = '+repr(result)+', real = '+repr(test[i][-1]))
    acc = get_accuracy(test,predictions)
    acclist.append(acc)
    print('Acuracia = '+repr(acc)+'%')

def get_acc_avg():
    s=0
    for i in range(len(acclist)):
        s+=acclist[i]
    return s/len(acclist)

def cross_validation(set1,sets,k):
    for i in range(len(sets)):
        print("Conjunto "+repr(i+1))
        prediction(set1,sets[i],k)
        
def create_subsets(base,folds):
    sub_tam=int(len(base)/folds)
    sets=[]
    for i in range(folds):
        subconj=[]
        for j in range(sub_tam):
            el = random.choice(base)
            subconj.append(el)
            base.remove(el)
        sets.append(subconj)
    return sets
       