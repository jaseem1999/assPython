size = int(input("Enter the size of list"))
list_length = []
list_bdth = []
for i in range(1,size+1,1):
    l = int(input("Enter the length"))
    b = int(input("Enter the breadth"))
    print("langth and breadth entered rectangle",i)
    list_length.append(l)
    list_bdth.append(b)
list_area = []
c = 0
dec_area = {}
print(list_bdth[c])
for l in list_length:
    for b in range(c,c+1,1):
        a = l*list_bdth[c]
        c=c+1
        list_area.append(a)
print(list_area)

def Convert(list_area):
    dec_area = {list_area[i]: list_area[i + 1] for i in range(0, len(list_area), 2)}
    return dec_area
         

print(Convert(list_area))
