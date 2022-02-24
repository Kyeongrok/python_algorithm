class HashTable:
   def __init__(self):
       self.size = 10
       self.table = [[] for _ in range(self.size)]

   def hash(self, name):
       ascii_sum = 0
       for word in name:
           ascii_sum += ord(word)
       return ascii_sum % self.size

   def insert(self, name, value):
       hashIndex = self.hash(name)
       self.table[hashIndex].append((name, value))

   def printTable(self):
       for idx, value in enumerate(self.table):
           print([idx, value])

table = HashTable()
table.insert("jisoo", 1000)
table.insert("kavin", 2000)
table.insert("sam", 3000)
table.insert("res_hash kim", 4000)
table.insert("mirror", 5000)
table.printTable()
