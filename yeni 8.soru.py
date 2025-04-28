lst = list()
while True:
    a = input("sayı giriniz, toplama işlemine başlamak için 'e' yazın: ")
    if a != "e":
        try:
            a = float(a)
        except:
            print("sayı girin")
            continue
        lst.append(a)
    else:
        break
clst=[]
for i in lst:
    if i%2==0:
        clst.append(i)
    else:
        continue
b= 0
for i in clst:
    b = b+i
print(b)