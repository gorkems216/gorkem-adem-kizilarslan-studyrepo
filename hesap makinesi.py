def add(a,b):
  print(a+b)
def subs(a,b):
  print(a-b)
def mult(a,b):
  print(a*b)
def div(a,b):
  print(a/b)

lst=[1,2,3,4,5]

chc=None

while chc != 5:
  try:
    chc=int(input("1-toplama,2-çıkarma,3-çarpma,4-bölme,5-çıkış"))
  except:
    print("geçerli seçim yap")
    continue
  if chc not in lst:
    print("geçerli seçim yap")
    continue
  if chc== 5:
    break
  try:
    a=float(input("sayı 1"))
    b=float(input("sayı 2"))
  except:
    print("geçerli sayı gir")
    continue
  if chc == 1:
    add(a,b)
  elif chc == 2:
    subs(a,b)
  elif chc == 3:
    mult(a,b)
  elif chc == 4:
    div(a,b)

