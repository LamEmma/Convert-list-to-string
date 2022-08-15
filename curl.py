
name = 'Hoang Thi Song'

name = name.split(' ')

name_sorted = []

i = 0

while i in range(len(name)):
    if i ==0:
        name_sorted.append(name[len(name)-1])
    elif i == len(name) -1:
       name_sorted.append(name[0]) 
    else:
        name_sorted.append(name[i][0] +'.')
    i+=1
    
name_list = name_sorted

def liststring(name_list):
    str = ''
    for s in name_list:
        str += s + ' '
    return str

print(liststring(name_sorted))


