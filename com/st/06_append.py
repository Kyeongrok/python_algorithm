string = "13+24*(35-46.76)"
#["13", "+", "24", "*", "(", "35", "-", "46.76", ")"]

def stringTokenizer(string):
   result=[]
   for chr in string:
       result.append(chr)
   return result

result=stringTokenizer(string)
print("=>",result)