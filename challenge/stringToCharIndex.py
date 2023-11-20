string = input("enter you string: ")
dic = dict()

for char in string:
    if char in dic:
        # dic.update({char : dic[char] + 1})
        dic.update({char : dic.get(char) + 1})
    else:
        dic.update({char : 1})

print(dic)