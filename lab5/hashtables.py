entries = []
file = open("data.txt", "r")
for line in file:
    entries.append(line.rstrip('\n'))
file.close()
#działanie. Robimy tablice T o rozmiarze m. Wypełniamy ją pustymi tablicami do których będziemy wrzucać elementy

def generateT(m):
    T = []
    for _ in range(m):
        T.append([])
    return T

def goodHash(key):
    hashedKey = 0
    for i in range (0,len(key)-1,2):
        pair = ord(key[i])*256 + ord(key[i+1])
        hashedKey = hashedKey ^ pair
    return hashedKey
def badHash(key):
    key = ord(key[0]) * 256
    return key

def hashTable(size,entries, hashMethod):
    T = generateT(size)
    for i in range(len(T) * 2):
        hashedKey = hashMethod((entries[i]))
        h = hashedKey % len(T)
        T[h].append(hashedKey)
    return T


def analyzeHash(hashedTable):
    empty_tables = 0
    max_length = 0
    not_empty_tables = []
    sum = 0
    for table in hashedTable:
        if len(table) == 0:
            empty_tables+=1
        else:
            not_empty_tables.append(table)
            if len(table) > max_length:
                max_length = len(table)

    for not_empty_table in not_empty_tables:
        sum += len(not_empty_table)
    average = sum / len(not_empty_tables) 
    return empty_tables, max_length, average


print("Empty lists, Max length, Average length")
print("Size 17")
print(analyzeHash(hashTable(17,entries,hash)) , "in built hash")
print(analyzeHash(hashTable(17,entries,goodHash)), "goodHash")
print(analyzeHash(hashTable(17,entries,badHash)),"badHash")
print("\nEmpty lists, Max length, Average length")
print("Size 1031")
print(analyzeHash(hashTable(1031,entries,hash)), "in built hash")
print(analyzeHash(hashTable(1031,entries,goodHash)), "goodHash")
print(analyzeHash(hashTable(1031,entries,badHash)), "badHash")
print("\nEmpty lists, Max length, Average length")
print("Size 1024")
print(analyzeHash(hashTable(1024,entries,hash)), "in built hash")
print(analyzeHash(hashTable(1024,entries,goodHash)), "goodHash")
print(analyzeHash(hashTable(1024,entries,badHash)), "badHash")


# Wyniki:
# Empty lists, Max length, Average length
# Size 17
# (3, 6, 2.4285714285714284) in built hash
# (1, 7, 2.125) goodHash
# (2, 5, 2.2666666666666666) badHash

# Empty lists, Max length, Average length
# Size 1031
# (143, 8, 2.3220720720720722) in built hash
# (478, 17, 3.72875226039783) goodHash
# (981, 183, 41.24) badHash

# Empty lists, Max length, Average length
# Size 1024
# (125, 8, 2.278086763070078) in built hash
# (736, 22, 7.111111111111111) goodHash
# (1020, 596, 512.0) badHash

# Wnioski:
#Lepsze wyniki dawał rozmiar rozmiar 1031 oprócz dla tablicy zbudowanej na haszowaniu wbudowanym.
# Wybór funkcji haszującej wpłynął na wyniki. funkcja wbudowana > goodHash > badHash