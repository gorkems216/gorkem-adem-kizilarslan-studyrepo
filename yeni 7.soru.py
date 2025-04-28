lst = list()
glst= list()
while True:
    a = input("sayı giriniz, toplama işlemine başlamak için 'exit' yazın: ")
    if a != "exit":
        lst.append(a)
    else:
        break
for i in range(len(lst)):
    glst.append(f"item[index no:{i},item:{lst[i]}]")
print(glst)
