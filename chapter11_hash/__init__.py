hash_table = list([0 for i in range(10)])

def get_key(data):
    return hash(data)


def hash_func(key):
    return key % 8

def lsave_data(data, value):
    index_key = get_key(data)
    hash_address = hash_func(index_key)

    if hash_table[hash_address] != 0:
        for i in range(hash_address, len(hash_table)):
            if hash_table[i] == 0:
                hash_table[i] = [index_key, value]
                return
            elif hash_table[i][0] == index_key:
                hash_table[i][1] = value
                return

    else:
        hash_table[hash_address] = [index_key, value]