entries = []
file = open("data.txt", "r")
for line in file:
    entries.append(line.rstrip('\n'))
file.close()


def goodHash(key):
    hashedKey = 0
    for i in range (0,len(key)-1,2):
        pair = ord(key[i])*256 + ord(key[i+1])
        hashedKey = hashedKey ^ pair
    return hashedKey
def badHash(key):
    key = ord(key[0]) * 256
    return key
sizes = [17]
for size in sizes:
    hashtableW = []
    hashtableD = []
    hashtableS = []
    for i in range(size):
        hashtableW.append(hash(entries[i]))
        hashtableD.append(goodHash(entries[i]))
        hashtableS.append(badHash(entries[i]))
    print(hashtableW)
    print(hashtableD)
    print(hashtableS)