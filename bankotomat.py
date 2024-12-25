bakiye = 1000
işlemler =  [1,2,3]
while True:
    işlem =  int(input("para çekme için '1' yatırmak için '2' çıkmak için '3'"))
    if işlem  not in işlemler:
         print("geçerli bir işlem seçin, bakiye: ", bakiye)
    elif işlem == 2:
         tutar = int(input("tutar girin: "))
         bakiye += tutar
         print("yeni bakiye: ", bakiye)
         continue
    elif işlem == 1:
         çekilecektutar = int(input("çekilecek tutarı girin: "))
         if bakiye - çekilecektutar <0:
              print("bakiyeniz eksi olamaz! bakiye: ", bakiye)
              continue
         else:
              bakiye -= çekilecektutar
              print("yeni bakiye: ", bakiye)
              continue
    else:
         break
print("Kartınızı unutmayın!")
     

   
         
   





