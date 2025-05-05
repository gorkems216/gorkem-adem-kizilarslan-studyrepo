euro={"Espresso": 2.50, "Americano":3.0,
"Latte":2.50, "Cappuccino":3.0, "Macchiato":2.50, "Mocha" :3.50, "Flat White":2.50}
select=["Espresso", "Americano",
"Latte", "Cappuccino", "Macchiato", "Mocha" , "Flat White"]
toplam=0
while True:
    try:
        chck= int(input("menü: 1- Espresso, 2- Americano, 3- Latte, 4- Cappuccino, 5- Macchiato, 6- Mocha , 7- Flat White: "))
        chcb=int(input("kahve boyutu: 1- medium , 2- large, 3- xlarge: "))
        cccc= int(input("seçim: 1-Eat in, 2- take away: "))
    except:
        print("geçerli seçim yapın")
        continue
    finally:
        if not 0<chck<=7:
            print("geçerli seçim yapın")
            continue
        if not 0<chcb<=3:
            print("geçerli seçim yapın")
            continue
        if not 0<cccc<=2:
            print("geçerli seçim yapın")
            continue
        if cccc ==1:
            cccc= True
        else:
            cccc= False
    a = euro[select[chck-1]]
    if chcb==2:
        b= a + 1
    elif chcb ==3:
        b= a + 1.5
    if cccc == False:
        c= b + 1

    d= input("devam mı? y/n: ")
    if d=="y":
        toplam += c
        continue
    elif d == "n":
        toplam += c
        break
    else:
        toplam += c
        print("geçersiz seçim! fiyat kaydedildi, çıkış yapıldı.")
        break
print(f"Toplam: {toplam}")
     
    

    
    

