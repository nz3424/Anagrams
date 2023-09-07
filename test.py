import random
CHARARRAY = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X","Y", "Z"]

weighted = [5, 3, 3, 4, 10, 5, 4, 5, 7, 2, 5, 7, 5, 6, 6, 6, 1, 8, 10, 7, 5, 2, 3, 1,
5,1]

def weightedRandom(a1):
    aux = [weighted[i] for i in range(len(a1))]
    for j in range(1, len(a1)):
        aux[j] += aux[j- 1]
    randomn = random.random() * aux[len(weighted) - 1]
    print(aux)
    k = 0
    while k < len(weighted):
        if (aux[k] > randomn):
            break
        else:
            k+=1
    return a1[k]

output = {}
for i in range(5):
    x = (weightedRandom(CHARARRAY))
    if x not in output:
        output[x] = 1
    else:
        output[x] +=1

print(output)