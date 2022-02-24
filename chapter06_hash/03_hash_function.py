import hashlib

# 직접 만드는 해시 함수
def nameHash(name):
    ascii_sum = 0
    for word in name:
        print(word)
        ascii_sum += ord(word)
    return ascii_sum

name = 'chulsoo'
# print(nameHash(name))

# res_hash() 내장 함수
result = hash(name)
print('res_hash():', result)

#hashlib 활용, md5
name = name.encode('utf-8')
enc = hashlib.md5(name)
print(enc.hexdigest())