import random
import timeit

def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1

        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1

        array[j + 1] = key

data = list(range(1,10001))
print(data)
random.shuffle(data)
print(data)

begin = timeit.default_timer()
insertionSort(data)
final = timeit.default_timer()

print('Array ordenado:')
print(data)

print ('Tempo de execução do algoritmo: %fs' % (final - begin))