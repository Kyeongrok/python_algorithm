p = ["leo", "kiki", "eden"]
c = set(["eden", "kiki"])

r = ''
for pi in p:
    if pi in c:
        pass
    else:
        r = pi

print(r)