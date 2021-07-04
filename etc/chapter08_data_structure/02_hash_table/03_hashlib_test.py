import hashlib

string = 'a'
encoded_string = string.encode()
print(encoded_string)
hexdigest = hashlib.sha256(encoded_string).hexdigest()
print('a:', hexdigest)

string2 = 'a.'
encoded_string2 = string2.encode()
print('a.:', hashlib.sha256(encoded_string2).hexdigest())