import random
class Node:
    def __init__(self,x):
        self.key = x
        self.left = None # lewy syn
        self.right = None # prawy syn
        self.p = None #ojciec

class BST:
    def __init__(self):
        self.root = None

    def BSTinsert(self, z):
        # wstawia wezel z do drzewa
        x = self.root
        y = None # y jest ojcem x
        while x != None:
            y=x
            if z.key<x.key:
                x=x.left
            else:
                x=x.right
        z.p=y
        if y==None: # drzewo puste
            self.root=z
        else:
            if z.key<y.key:
                y.left=z
            else:
                y.right=z 



    def BSTlenght(self,x):
        if x is None:
            return 0
        else:
            return 1 + self.BSTlenght(x.left) + self.BSTlenght(x.right) # przechodzi po kazdym nodzie i dodaje 1 do lenght
        

    def BSTinOrder(self, x):
    # przechodzi i drukuje klucze poddrzewa
    # o korzeniu "x" w kolejnosci
    # "wewnętrznej (in order)"
        if x==None: return
        self.BSTinOrder(x.left)
        print(x.key)
        self.BSTinOrder(x.right)
    #funckja drukuje drzewo w formie graficznej
    def BSTprint(self, x,depth=0): #skoro inorder wypisuje elementy "od lewej" to drukuje drzewo od lewej ale zamienilem kolejnosc dzieki temu góra(prawa część drzewa) jest wypisana
        if x is None: #jakby lustrzane odbicie względem wierzchołka
            return 
        self.BSTprint(x.right, depth + 1)
        print(' ' * depth * 4 + "->", x.key)
        self.BSTprint(x.left, depth + 1)

    def BSTheight(self,x):
        if x is None:
            return 0
        else:
            leftHeight = self.BSTheight(x.left) #rekurencyjnie przechodzi po wszystkich nodeach
            rightHeight = self.BSTheight(x.right)
            return max(leftHeight,rightHeight) +1 #przy kazdym wywolaniu zwraca dluzsze poddrzewo

    def BSTsearch(self,x,k):
    # szuka rekurencyjnie wezla zawierajacego klucz k
    # w poddrzewie o korzeniu x
        if x==None or x.key==k:
            return x # None oznacza, ze szukanego klucza
    # nie ma w drzewie
        if k<x.key:
            return self.BSTsearch(x.left,k)
        else:
            return self.BSTsearch(x.right,k) 
        
    def bstDelete(self,z):
 # usuwa węzeł"z" z drzewa
 # wersja "naturalna"
        if z.left==None and z.right==None: # (1) z liść
            if z==self.root:
                self.root=None
            else:
                 if z==z.p.left: # z jest lewym synem
                     z.p.left=None
                 else:
                    z.p.right=None
        elif z.left != None and z.right != None: # (3) dwóch synów
            y=self.bstMinimum(z.right)
            z.key=y.key # przepisz zawartość węzła y do z
            self.bstDelete(y) # przypadek (1) lub (2) 
        else: # (2) jeden syn
            if z.left != None: # z.right==None
                z.left.p=z.p
                if z==self.root:
                    self.root=z.left
                else:
                    if z==z.p.left:
                        z.p.left=z.left
                    else:
                        z.p.right=z.left
            else: # z.left==None
                z.right.p=z.p
                if z==self.root:
                    self.root=z.right
                else:
                    if z==z.p.left:
                        z.p.left=z.right
                    else:
                        z.p.right=z.right
    def clearBST(self,percentage): 
        size= self.BSTlenght(self.root) * (percentage) // 100 #bierzemy dlugosc drzewa i obliczamy ile elementów usunąć
        for i in range(size):
            self.bstDelete(self.BSTsearch(self.root,entries[i])) #usuwam node'y idac od poczatku entries[]
    def bstMinimum(self,x):
 # zwraca skrajny lewy węzeł w poddrzewie o korzeniu x
 # czyli węzeł o najmniejszym kluczu w tym poddrzewie
        while x.left != None:
            x = x.left
        return x 


entries = [] #tworze liste z pliku
with open("./words.txt", "r") as file:
    line = file.readline()
    entries = line.split()



def BSTcreate(size): #tworze drzewo o rozmiarze size
    T = BST()
    for i in range(size-1):
        entry= entries[i]
        T.BSTinsert(Node(entry))          
    return T

def analyzeBST(): # dla kazdej wielkosci tworze drzewo po czym wypisuje wysokosc drzewa
    sizes = [500,1000,2000]
    trees = []
    for size in sizes:
        T = BSTcreate(size)
        trees.append(T)
        print(f"Height: {T.BSTheight(T.root)}")
    for tree in trees: # dla kazdego drzewa wyczyszczam 80% drzewa i wypisuje wysokosc drzewa
        tree.clearBST(80)
        print(f"Height after deletion: {tree.BSTheight(tree.root)}")
        # tree.BSTprint(tree.root)
    
analyzeBST()





