secim = input("Seçim [1-6] : ")
if secim == "1":
    sayi = int(input("Sayı : "))
    bölenler = []
    for i in range(1,sayi):
        if sayi % i == 0:
            bölenler.append(i)
    if sum(bölenler) == sayi:
        print("Bu sayı Mükemmel Sayıdır !")
    else:
        print("Bu Sayı Mükemmel Sayı Değildir !")




elif secim == "2":
    sayi = int(input("Sayı : "))
    listesi = list(str(sayi))
    listesi =[int(i) for i in listesi]
    uzunluk = len(listesi)
    toplam = 0
    for i in range(uzunluk):
        rakam =  int(listesi[i])**uzunluk
        toplam +=rakam
    if toplam == sayi:
        print("Bu Sayı Bir Armstrong Sayısıdır !")
    else:
        print("Bu Sayı Bir Armstrong Sayısı Değildir !")
elif secim == "3":
    for i in range(10):
        for k in range(10):
            print(f"{i} * {k} = {i*k}")
elif secim == "4":
    toplam = 0
    while True:
        sayi = input("Sayı : ")
        if sayi.lower() =="q":
            break
        toplam += int(sayi)
    print(toplam)
elif secim == "5":
    toplam = []
    for i in range(100):
        if i not in toplam:
            if i %3 == 0:
                toplam.append(i)
                continue
    print(toplam)
elif secim == "6":
    print([i for i in range(100) if i %2==0])
