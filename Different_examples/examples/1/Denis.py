def magnifier(list):
    new_list = [kq+10 for kq in list]
    #for item in list:
        #item += 10
        #new_list.append(item)
    return new_list


ls = [i for i in range(1,101,5)]
#for i in range(1, 101, 5):
    #ls.append(i)
print(magnifier(ls))

