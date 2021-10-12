# Mantıksal Değerler ve Karşılaştırma Operatörleri
"""
Mantıksal Değerler (Boolean)

Mantıksal değerler ya da ingilizce ismiyle boolean değerler aslında Pythonda bir veri tipidir
ve iki değere sahiplerdir: True ve False.
"""

a = True
print(type(a))

b = False
print(type(b))

"""
Pythonda bir sayı değeri eğer 0'dan farklıysa True, 0 ise False olarak anlam kazanır. 
Bunu bool() fonksiyonuyla dönüştürme yaparak görebiliriz
"""

print(bool(12.4)) # true

print(bool(0.0)) # true

print(bool()) # false

print(bool(12)) # true

print(bool(-1)) # true

print(0) # false

"""
Bool değerleri ayrıca birazdan göreceğimiz bir karşılaştırma operatöründen sonra ortaya çıkan sonuç değeridir
"""

print(1 > 2)
print(1 < 2)

"""
Ayrıca Pythonda eğer bir değişkenin değerini sonradan belirlemek isterseniz 
geçici olarak bu değişken None (atanmamış anlamında) değerine eşitleyebilirsiniz.
"""

a = None # henüz değer atamadık
print(a)
a = 4 # Şimdi değer atıyoruz.
print(a)

"""
operatör: ==
görevi: İki değer birbirine eşitse True, değilse False değer döner.
örnek: 2 == 2 (True) , 2 == 3 (False)
"""

"""
operatör: !=
görevi: İki değer birbirine eşit değilse True, diğer durumda False döner.	
örnek: 2 != 2 (False), 2 != 3 (True)
"""

"""
operatör: >
görevi: Soldaki değer sağdaki değerden büyükse True, değilse False döner.
örnek: 3 > 2 (True), 2 > 3 (False)
"""

"""
operatör: <
görevi: Soldaki değer sağdaki değerden küçükse True, değilse False döner.
örnek: 2 < 3 (True) , 3 < 2 (False)
"""

"""
operatör: >=
görevi: Soldaki değer sağdaki değerden büyükse veya sağdaki değere eşitse True, değilse False döner.
örnek: 3 >= 2 (True),3 >= 3 (True) , 2 >= 3 (False)
"""

"""
operatör: <=
görevi: Soldaki değer sağdaki değerden küçükse veya sağdaki değere eşitse True, değilse False döner.
örnek: 3 <= 2 (False),3 <= 3 (True) , 2 <= 3 (True
"""

print("Mehmet" == "Mehmet")
print("Mehmet" == "Murat")
print("Murat" != "Mehmet")
print("Oğuz" < "Murat") # Alfabetik olarak bakar
print(2<3)
print(54>=54)
print(98>32)



















