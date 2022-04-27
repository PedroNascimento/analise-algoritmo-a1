import random
import timeit

def bubbleSort(array):
    #loop para acessar cada elemento do array
    for i in range(len(array)):
        # loop para comparar elementos do array
        for j in range(0, len(array) - i - 1):
            # Comparando 2 elementos adjacentes
            # Mudar do > para o < para ordenar de forma decrescente
            if array[j] > array[j +1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

data = list(range(1,10001))
print(data)
random.shuffle(data)
print(data)

begin = timeit.default_timer()
bubbleSort(data)
final = timeit.default_timer()

print('Array ordenado:')
print(data)
print ('Tempo de execução do algoritmo: %fs' % (final - begin))