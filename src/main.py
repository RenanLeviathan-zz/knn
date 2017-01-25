# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import knn
def main():
    lista = [
    (1,  2,  3,  4,"Iris-setosa"),
    (3.2,5.4,1.3,4,"Iris-virginica"),
    (4,  1.2,3.2,3,"Iris-versicolor")
    ]
    nlista = []
    f = open("res/iris.arff")
    for line in f:
        values = line.split(",",4)
        x = float(values[0])
        y = float(values[1])
        z = float(values[2])
        w = float(values[3])
        st = values[4]
        nlista.append((x,y,z,w,st))
          
    for line in nlista:
        print(line)
    print(knn.minimo(lista))
    print("Media dos atributos numericos")
    med = knn.media(lista)
    print(med)
    print("Desvio padrao")
    print(knn.std(lista,med))
    matrix=knn.matrix_diss(lista)
    m2=knn.matrix_diss(nlista)
    for i in range(0,len(lista)):
        for j in range(0,len(lista)):
            print("%2.2f "%matrix[i][j])
        print("\n")
    
    ordem=10
    for i in range(0,ordem):
        for j in range(0,ordem):
            print("%2.2f "%m2[i][j])
        print("\n")
    
main()
