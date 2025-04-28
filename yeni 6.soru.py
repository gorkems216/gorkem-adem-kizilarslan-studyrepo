
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
b= 0
for i in lst:
    b = b+i
print(b)



