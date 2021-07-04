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
        if self.search(name) is True:
            print("Already exist!")
            return
        hashIndex = self.hash(name)
        self.table[hashIndex].append([name, value])

    def search(self, name):
        hashIndex = self.hash(name)
        for i in range(len(self.table[hashIndex])):
            if self.table[hashIndex][i][0] == name:
                print("name : %s  / value : %d" % (name, self.table[hashIndex][i][1]))
                return True

    def remove(self, name):
        hashIndex = self.hash(name)
        for i in range(len(self.table[hashIndex])):
            if self.table[hashIndex][i][0] == name:
                del self.table[hashIndex][i]

    def update(self, name, value):
        hashIndex = self.hash(name)
        for i in range(len(self.table[hashIndex])):
            if self.table[hashIndex][i][0] == name:
                self.table[hashIndex][i][1] = value

    def printTable(self):
       for idx, value in enumerate(self.table):
           print([idx, value])

table = HashTable()
table.insert("jisoo", 1000)
table.insert("kavin", 2000)
table.insert("sam", 3000)
table.insert("hash kim", 4000)
table.insert("mirror", 5000)

table.search("sam")
table.search("hash kim")
table.search("mirror")

table.remove("mirror")
table.printTable()

table.search("hash kim")
table.update("hash kim", 1500)
table.search("hash kim")