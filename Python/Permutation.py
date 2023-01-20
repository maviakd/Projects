list = [i for i in "cat"]
list2 = [i for i in "cat"]
newlist = []

def makeword(list):
    str = ""
    for item in list:
        str += item
    return str

for item in list:
    x = 0
    list = list2
    while x < len(list):
        hold = list[x]
        list[x] = item
        if x != 0:
            list[x-1] = hold
        x+=1
        word = makeword(list)
        if word not in newlist:
            newlist.append(word)





for item in newlist:
    print(item)

