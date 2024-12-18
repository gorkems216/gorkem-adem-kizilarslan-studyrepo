while True:
  
  try:
    preis= float(input("Kitap fiyatı"))
    rabatt= float(input("indirim oranı: %"))/100
    kargo_1= float(input("1. kitap kargo ücreti"))
    kargo= float(input("2 ve daha fazla kitap kargo ücreti"))
    zahl= int(input("60 kitabın fatura bedelini hesaplayın"))
    print(((preis-preis*rabatt)*zahl)+(kargo_1+kargo*(zahl-1)))
    break
  except:
    print("sadece sayı giriniz")
    continue
