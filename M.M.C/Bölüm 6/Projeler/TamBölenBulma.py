def BölenBulma(sayı):
    bölenler = []
    for i in range(1,sayı+1):
        if sayı % i == 0:
            bölenler.append(i)
    return bölenler
while True:
    a =input("Sayı : ")
    if a.lower() == "q":
        print("Program Sonlanıyor...")
        break
    else:
        a = int(a)
        print(f"{a} Bölenleri : {BölenBulma(a)}")
    