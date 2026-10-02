sayı1 = int(input("ilk sayıyı giriniz"))
print(sayı1)

sayı2 = int(input("ikinci sayıyı giriniz"))
print(sayı2)

işlem = input("""yapmak istediğiniz işlemi giriniz.
(toplama = + , çıkarma = - , çarpma = * , bölme = /)""")

if işlem == "+":
    print("sonuç:" + str(sayı1+sayı2))

if işlem == "-":
    print("sonuç:" + str(sayı1-sayı2))

if işlem == "*":
    print("sonuç:" + str(sayı1*sayı2))

if işlem == "/":
    print("sonuç:" + str(sayı1/sayı2))
