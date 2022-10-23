

def rev(list):
    #list_ = [i*2 for i in reversed(list)]
    list_ = []
    for i in reversed(list):
        i = i*2
        list_.append(i)
    return list_

print(rev([1,2,3,4]))

