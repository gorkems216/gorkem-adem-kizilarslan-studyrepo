import geometry
while True:
  try:
    chc = int(input("1-çevre,2-alan,3-hacim,4-mutlak değer,5-çıkış"))
  except:
    print("geçerli seçim yap")
    continue

  try:
    r = float(input("yarıçap: "))
  except:
    print("geçerli sayı giriniz")
    continue
  
  if chc == 5:
    break
  elif chc == 1:
    geometry.cevre(r)
  elif chc ==2:
    geometry.alan(r)
  elif chc ==3:
    try:
      h = float(input("yükseklik: "))
    except:
      print("geçerli sayı girin")
      continue
    geometry.silindirhacim(r,h)
  elif chc == 4:
    try:
      n = float(input("sayı: "))
    except:
      print("geçerli sayı giriniz")
      continue
    geometry.mutlak(n)



