
while True:
    try:
        daily = int(input("bugünkü yumurta sayısı : "))
    except:
        print("sayı giriniz")
        continue
    finally:
         if daily<0:
            print("negatif olamaz")
            continue
         
    oikrtn = daily//12
    oikln= daily%12
    akrtn = oikln//6
    artn = oikln%6
    print("on ikilik karton sayısı: " + str(oikrtn))
    print("altılık karton sayısı: " + str(akrtn))
    print("artan/kahvaltılık yumurta sayısı: " + str(artn))

