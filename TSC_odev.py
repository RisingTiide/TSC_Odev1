#2 sayýnýn toplamý

# x= input('Sayi1:')
# y= input('Sayi2:')
# print(x)
# print(y)
# toplam= int(x)+int(y)
# print(toplam)




##1 den 100 e kadar toplam

# toplam=0 
# for i in range(100):
#     toplam += i
# print("1 den 100 e kadar olan sayilarin toplami:",toplam)



## Asal Sayi Kontrolü
# sayi=int(input("Sayinizi giriniz:"))
# if sayi<=1:
#  print("Girdiginiz sayi asal bir sayi degil !!!")
# elif sayi==2:
#  print("2, bir asal sayidir :):):)")
# else:
#  for i in range(2,sayi): 
#     control=True
#     if sayi % i==0: 
#         control=False
#         break
#  if control:
#     print("Girdiginiz sayi asal bir sayidir :):):)")
#  else:
#     print("Girdiginiz sayi asal bir sayi degil !!!")




##Dizide tekrar edilip edilmediði

# dizi=[10,99,17,-20,34,90,"yaren","yaren"] 
# benzersiz=[]
# control=True
# for x in dizi:
#  if x in benzersiz:
#   control=False
#   break
#  benzersiz.append(x)
# if control:
#  print("Dizide tekra eden eleman yok")
# else:
#  print("Dizide tekrar eden eleman var !!")



