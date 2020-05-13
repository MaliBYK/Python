secim = input("Hangi Problem Çözümü [1-4] : ")
if secim == "1":
    print("***Problem1***")
    boy =float(input("Boy Uzunluğunuz[Metre Cinsinden] : "))
    kilo = float(input("Kilonuz[Kg Cinsinden] : "))
    bki = kilo/(boy**2)
    if bki < 18.5:
        print("Zayıf !")
    elif bki < 25:
        print("Normal ! ")
    elif bki < 30:
        print("Fazla Kilolu !!")
    else:
        print("Obez !!!")
elif secim == "2":
    print("***Problem***")
    a = float(input("Birinci sayı : "))
    b = float(input("İkinci Sayı : "))
    c = float(input("Üçüncü Sayı : "))
    liste = [a,b,c]
    print(f"En Büyük sayı {max(liste)}")
elif secim == "3":
    print("Yakında...")

elif secim == "4":
    şekil =input("Kenar Sayısı [3 veya 4]: ")
    if şekil == "4":
        k1 = input("1.Kenar : ")
        k2 = input("2.Kenar : ")
        k3 = input("3.Kenar : ")
        k4 = input("4.Kenar : ")
        if k1 == k2 == k3 == k4:
            print("Buldum Bu Bir Kare !")
        elif ((k1 == k2)and(k3 == 4))or((k1 == k3)and(k2 == k4))or((k1 == k4)and(k2 == k3)):
            print("Buldum Bu Bir Dikdörtgen !")
        else:
            print("Bu Normal Bir Dörtgen !")
        
    


    
    
