# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import knn
import random
def main():
    nlista = []
    base = []
    opt = input("Qual arquivo queres testar? 0 base normal 1\
    base normalizada 2 base normalizada (z score)")
    if opt=="0":
        f = open("res/iris.arff")
    elif opt=="1":
        f = open("res/iris_norm.arff")
    elif opt=="2":
        f = open("res/iris_normz.arff")
    else:
        print("Opcao invalida\
        \nate mais")
        exit()
    
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
    ordem=int(input("Ordem da matriz"))
    for i in range(0,ordem):
        for j in range(0,ordem):
            print("%2.2f "%m2[i][j],end=' ')
        print("\n")
    
    k = int(input("Defina o valor de k:"))
    t_set=[]#conjunto de treinamento
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
        #predicao de classes
        #hold-out
        print("Hold-out base normal")
        knn.prediction(nlista,t_set,k)
    elif option == 1:
        #cross validation
        folds = int(input("Defina o numero de subconjuntos"))
        copia=t_set+nlista
        conjuntos = knn.create_subsets(copia,folds)
        #efetua cross validation
        print("Cross validation")
        for c in range(len(conjuntos)):
            for d in range(len(conjuntos)):
                if(c!=d):
                    knn.prediction(conjuntos[c],conjuntos[d],k)
        print('Media das acuracias: {}%'.format(knn.get_acc_avg()))
        knn.acclist=[]
    else:
        print("Opcao invalida")
main()
