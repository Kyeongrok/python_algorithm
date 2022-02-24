class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [0 for _ in range(self.size)]

    def hash(self, name):
        ascii_sum = 0
        for word in name:
            ascii_sum += ord(word)
        return ascii_sum % self.size

    def insert(self, name, value):
        self.table[self.hash(name)] = value

    def printTable(self):
        for idx, value in enumerate(self.table):
            if value != 0:
                print([idx, value])

table = HashTable()
table.insert("jisoo", 1000)
table.insert("kavin", 2000)
table.insert("sam", 3000)
table.insert("res_hash kim", 4000)
table.insert("mirror", 5000)
table.printTable()