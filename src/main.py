# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import knn
import random
def main():
    nlista = []
    base = []
    f = open("res/iris.arff")
    for line in f:
        if (line[0] != '%') and (line[0] != '@') and (line[0] != '\n'):
            values = line.split(",",4)
            x = float(values[0])
            y = float(values[1])
            z = float(values[2])
            w = float(values[3])
            st = values[4]
            nlista.append((x,y,z,w,st))
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
    for i in range(len(med)):
        print("%2.3f"%(med[i]),end=' ')
    print("\nDesvio padrao")
    sd = knn.std(nlista,med)
    for i in range(len(sd)):
        print("%2.3f"%(sd[i]),end=' ')
    print("\nMatriz de similaridade")
    m2=knn.matrix_sim(nlista)
    ordem=10
    for i in range(0,ordem):
        for j in range(0,ordem):
            print("%2.2f "%m2[i][j],end=' ')
        print("\n")
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
    k = int(input("Defina o valor de k:"))
    t_set=[]#conjunto de treinamento
    t_set1=[]#conjunto de treinamento hold-out com dados normalizados
    t_set2=[]#conjunto com dados normalizados (z score)
    option=int(input("Hold-out(0) ou cross validation(1)?Digite o numero correspondente"))
    if option == 0:
        #separacao dos grupos
        t_pc = int(input("Defina a porcentagem do grupo de treinamento"))
        print(t_pc)
        training = int(len(nlista)*t_pc/100)
        #test = len(nlista)-training
        #escolha do conjunto de treinamento
        for i in range(0,training):
            el = random.choice(nlista)
            t_set.append(el)
            nlista.remove(el)
        #escolha do conjunto de treinamento com os dados normalizados
        t2 = int(len(norm)*t_pc/100)
        for i in range(0,t2):
            el2 = random.choice(norm)
            t_set1.append(el2)
            norm.remove(el2)
        #escolha do conjunto de treinamento com os dados normalizados (z score)
        t3 = int(len(normz)*t_pc/100)
        for i in range(0,t3):
            el3 = random.choice(normz)
            t_set2.append(el3)
            normz.remove(el3)
        #predicao de classes
        #hold-out
        print("Hold-out base normal")
        knn.prediction(nlista,t_set,k)
        print("Hold-out com base normalizada")
        knn.prediction(norm,t_set1,k)
        print("Hold-out com base normalizada (z score)")
        knn.prediction(normz,t_set2,k)
    elif option == 1:
        #cross validation
        folds = int(input("Defina o numero de subconjuntos"))
        copia=t_set+nlista
        conjuntos = knn.create_subsets(copia,folds)
        c1 = random.choice(conjuntos)
        #retira o conjunto
        conjuntos.remove(c1)
        for i in range(len(c1)):
            print("%2.2f %2.2f %2.2f %2.2f %s"%(c1[i][0],c1[i][1],c1[i][2],c1[i][3],c1[i][4]))
        knn.cross_validation(c1,conjuntos,k)
        print("Media das acuracias: ",knn.get_acc_avg(),"%")
        knn.acclist=[]
        #cross validation com dados normalizados
        lista2=t_set1+norm
        conj2=knn.create_subsets(lista2,folds)
        c2=random.choice(conj2)
        conj2.remove(c2)
        print("\nCross validation com dados normalizados")
        print("Conjunto eleito")
        for i in range(len(c2)):
            print("%2.2f %2.2f %2.2f %2.2f %s"%(c2[i][0],c2[i][1],c2[i][2],c2[i][3],c2[i][4]))
        knn.cross_validation(c2,conj2,k)
        print("Media das acuracias: ",knn.get_acc_avg(),"%")
        knn.acclist=[]
        #cross validation com dados normalizados (z score)
        lista3=t_set2+normz
        conj3=knn.create_subsets(lista3,folds)
        c3=random.choice(conj3)
        conj3.remove(c3)
        print("\nCross validation com dados normalizados (z score)")
        print("Conjunto eleito")
        for i in range(len(c3)):
            print("%2.2f %2.2f %2.2f %2.2f %s"%(c3[i][0],c3[i][1],c3[i][2],c3[i][3],c3[i][4]))
        knn.cross_validation(c3,conj3,k)
        print("Media das acuracias: ",knn.get_acc_avg(),"%")
        knn.acclist=[]
    else:
        print("Opcao invalida")
main()
