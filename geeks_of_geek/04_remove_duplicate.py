str = "aoeuoentoheerchneth"

def removeDuplicate(str):
    result = ""
    for chr in str:
       if chr not in result:
          result = result + chr
    return result

print(removeDuplicate(str))