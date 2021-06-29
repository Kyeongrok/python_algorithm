l = ['A', 'B', 'C']

def fn2(arr):
    if len(arr) == 2:
        return [f'{arr[0]}{arr[1]}', f'{arr[1]}{arr[0]}']
    else:
        r = []
        for i in range(len(arr)):
            extracted = arr.pop(0)
            for string in fn2(arr):
                r.append(f'{extracted}{string}')
            arr.append(extracted)
        return r

print(fn2(l))