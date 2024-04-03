class Node:
 def __init__(self,k):
    self.key = k
    self.next = None
    self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def listInsert(self, x): 
        x.next = self.head #Łączymy next dodawanego node'a z początkiem listy
        if self.head != None:
           self.head.prev = x #Jeżeli lista nie jest pusta to łączymy x przed głowę listy
           #Jeżeli lista jest pusta to nie ma potrzeby ustawiania poprzednika self.head bo nie istnieje
        self.head = x # Ustawiamy głowę listy na dodawanego node'a
        x.prev = None #ustawiamy .prev node'a na None (bo jest dodany na początku)

    def listSearch(self,k):
        x = self.head
        while x!= None and x.key != k: #przeszukujemy do czasu kiedy x nie jest None(czyli nie jest ostatni) i x.key nie bedzie szukaną wartością
          x = x.next    
        return x
    def listDelete(self,x):
        if x.prev != None: #Jeżeli x.prev nie jest None to znaczy, że x nie jest pierwszym elementem
          x.prev.next = x.next #Łączymy poprzednik z następnikiem x np, A->B->C to łączymy A z C przez to B jest jakby usuwane z listy bo nie ma dowiązań A -> C
        else: #Przypadek, gdy x jest pierwszym elementem to łączymy głowę z następnikiem np. None <-> A <-> None to łączymy None z None i lista jest pusta
           self.head = x.next
        if x.next != None: #jeżeli usuwany element ma następnika to łączymy następnika z poprzednikiem np. A -> C to mamy A <-> C
           x.next.prev = x.prev
    def listDisplay(self):
        elements = []
        x = self.head
        while x != None:
          elements.append(x.key)
          x = x.next  
        return elements       
    def listNoDupe(self):
        seen = set() #Tworzę set z wartościami 
        noDupList = LinkedList()
        x = self.head
        while x != None:
          key = x.key
          if key not in seen:
             seen.add(key)
             noDupList.listInsert(Node(key)) #tworzymy Node z wartością i dodajemy go do listy
          x = x.next 
        return noDupList
          
def listMerge(list1,list2):
    newList = LinkedList()
    newList.head = list1.head
    x = newList.head
    while x.next != None:
      x = x.next
    x.next = list2.head
    return newList
       
     
list = LinkedList()
node1 = Node("Franek")
node2 = Node("Kacper")
node3 = Node("Franek")
node4 = Node("Franek")
node5 = Node("Szymon")
list.listInsert(node1)
list.listInsert(node2)
list.listInsert(node3)
list.listInsert(node4)
list.listInsert(node5)


list2 = LinkedList()
node1 = Node("1")
node2 = Node("2")
node3 = Node("3")
node4 = Node("4")
node5 = Node("5")
list.listInsert(node1)
list.listInsert(node2)
list.listInsert(node3)
list.listInsert(node4)
list.listInsert(node5)


print(list.listDisplay())
noDupList = list.listNoDupe()
print(noDupList.listDisplay())

mergedList = listMerge(list,list2)
mergedList.listDisplay()


