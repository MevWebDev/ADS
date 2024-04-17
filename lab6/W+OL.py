import math
entries = []
# tworzę objekt {numer, nazwisko} z każdej linijki pliku.txt
with open("./nazwiska.txt", "r") as file:
    for line in file:
        number, name = line.split()
        
        object = {
            'key' : number,
            'surname' : name
        }
        entries.append(object)

def generateT(m): # tworzę liste pustych list
    T = []
    for _ in range(m):
        T.append([])
    return T

def goodHash(key): #funckja haszująca słowo na liczbe
    hashedKey = 0
    for i in range (0,len(key)-1,2):
        pair = ord(key[i])*256 + ord(key[i+1])
        hashedKey = hashedKey ^ pair
    return hashedKey

def h1(key,i,m): #hashowanie liniowe
    index = (key + i) % m
    return index

def hashInsert(T,key): #wstawianie do T objektu hashowanego po nazwisku
    surname = key["surname"]
    i = 0
    while i < len(T):
        hashedKey = goodHash(surname)
        index = h1(hashedKey,i, len(T)) % len(T)
        if len(T[index]) == 0:
            T[index].append(key)
            return i
        else:
            i += 1


def hashTable(size,entries):  
    T = generateT(size)
    for i in range (math.floor(len(T) * 0.5)): #tu ustalam jak bardzo chcę zapełnic tablice
        hashInsert(T,entries[i]) 
    return T

def printHashTable(hashTable): # printowanie każdej tabeli w nowej linii
    for table in hashTable:
        print(table, "\n")

#1. Test operacj na małej tablicy
smallHashedTable = hashTable(13,entries)
printHashTable(smallHashedTable)

def howManyTries(hashedTable): #liczenie ile prób zostalo wykonanych przy wstawianiu do tablicy
    tries = hashInsert(hashedTable, entries[500])
    return tries 

def analyzeInsert(hashedTable, n): #liczenie średniej ilości prób wstawiania n kluczy do tablicy
    sum = 0
    for i in range (n):
        sum += hashInsert(hashedTable, entries[-1*i])
    return sum / n

#2. Pomiary dla dużej tablicy
bigHashTable = hashTable(1031,entries)
print(analyzeInsert(bigHashTable,20))



