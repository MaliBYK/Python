# Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın.
# Ekrana yazdırma işlemini format metoduyla yapmaya çalışın.

print("***Problem1***")
a = input("Birinci Sayı : ")
b = input("İkinci Sayı : ")
c = input("Üçüncü  Sayı : ")
print(f"Girdiğiniz sayılar Sırasıyla Şunlardır : {a} , {b} , {c}")


print("***Problem2***")
boy = float(input("Boyunuz [Metre Cinsinden] : "))
kilo = float(input("Kilonuz [Kg Cinsinden] : "))
print("Sizin Beden Kitle İndexiniz :\n{}".format(kilo/(boy*boy)))


print("***Problem3***")
araba = input("Aracınız 1 Kilometrede kaç TL yakıt Yakıyor : ")
yol = input("Gideceğiniz Yolum Km Cinsinden Uzunluğu : ")
yakıt = float(araba)*float(yol)
print(f"Toplam yakıt Maliyeti : {yakıt} TL")


print("***Problem4***")
ad = input("Adınız : ")
soyad = input("Soyadınız : ")
num = input("Numaranız : ")
print(f"\n\nAdı : {ad}\nSoyadı : {soyad}\nNumarası : {num}\n")


print("***Problem5***")
d1 = float(input("1.Değer : "))
d2 = float(input("2.Değer : "))
d1,d2 = d2,d1
print(f"\n1.Değer[Yeni] : {d1}")
print(f"2.Değer[Yeni] : {d2}")


print("\n***Problem6***")
a = float(input("1.Dik Kenar Uzunluğu : "))
b =float(input("2.Dik Kenar Uzunluğu : "))
c =((a**2)+(b**2))**0.5
if c.is_integer():
    c = int(c)
print(f"Hipotenüs : {c}")




