ax = float(input("birinci nokta x: "))
ay = float(input("birinci nokta y: "))
bx = float(input("ikinci nokta x: "))
by = float(input("ikinci nokta y: "))
a = (ax,ay)
b= (bx,by)
msf = ((a[0]- b[0])**2 + (a[1]-b[1])**2)**0.5
print("aradaki mesafe: " + str(msf))