# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import knn
import random
def main():
    nlista = []
    copia = []
    base = []
    f = open("res/iris.arff")
    for line in f:
        values = line.split(",",4)
        x = float(values[0])
        y = float(values[1])
        z = float(values[2])
        w = float(values[3])
        st = values[4]
        nlista.append((x,y,z,w,st))
        copia.append((x,y,z,w,st))
        base.append((x,y,z,w,st))
          
    for line in base:
        print(line)
    mn=knn.minimo(nlista)
    print("Minimo dos atributos numericos")
    print(mn)
    mx=knn.maximo(nlista)
    print("Maximo dos atributos numericos")
    print(mx)
    print("Media dos atributos numericos")
    med = knn.media(nlista)
    print(med)
    print("Desvio padrao")
    sd = knn.std(nlista,med)
    print(sd)
    m2=knn.matrix_sim(nlista)
    ordem=10
    for i in range(0,ordem):
        for j in range(0,ordem):
            print("%2.2f "%m2[i][j],end=' ')
        print("\n")
    #for i in range(len(nlista)):
        #row=[]
        #length=len(nlista[0])-1
        #for j in range(length):
            #row.append((nlista[i][j]-mn[j])/(mx[j]-mn[j]))
        #norm.append(row)
    norm=knn.normalize(nlista,mn,mx)
    normz=knn.normalize_z(nlista,med,sd)
    #matriz com dados normalizados
    print("Normalização")
    m3=knn.matrix_sim(norm)
    for i in range(0,ordem):
        for j in range(0,ordem):
            print("%2.2f "%m3[i][j],end=' ')
        print("\n")
    #normalizacao z score
    print("Normalização z-score")
    m4=knn.matrix_sim(normz)
    for i in range(0,ordem):
        for j in range(0,ordem):
            print("%2.2f "%m4[i][j],end=' ')
        print("\n")
    #separacao dos grupos
    t_pc = int(input("Defina a porcentagem do grupo de treinamento"))
    print(t_pc)
    training = int(len(nlista)*t_pc/100)
    #test = len(nlista)-training
    t_set=[]#conjunto de treinamento
    #escolha do conjunto de treinamento
    for i in range(0,training):
        el = random.choice(nlista)
        t_set.append(el)
        nlista.remove(el)
    #escolha do conjunto de treinamento com os dados normalizados
    t_set1=[]
    for i in range(0,training):
        el = random.choice(norm)
        t_set1.append(el)
        norm.remove(el)
    #escolha do conjunto de treinamento com os dados normalizados (z score)
    t_set2=[]
    for i in range(0,training):
        el = random.choice(normz)
        t_set2.append(el)
        normz.remove(el)
    #predicao de classes
    k = int(input("Defina o valor de k:"))
    #hold-out
    print("Hold-out base normal")
    knn.prediction(nlista,t_set,k)
    print("Hold-out com base normalizada")
    knn.prediction(norm,t_set1,k)
    print("Hold-out com base normalizada (z score)")
    knn.prediction(normz,t_set2,k)
    #cross validation
    folds = int(input("Defina o numero de subconjuntos"))
    conjuntos = knn.create_subsets(copia,folds)
    c1 = random.choice(conjuntos)
    for i in range(len(c1)):
        print(c1[i])
    knn.cross_validation(c1,conjuntos)
main()
