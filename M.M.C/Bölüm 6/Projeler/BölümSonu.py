def problem1():
    for i in range(1,1001):
        toplam = 0
        for j in range(1,i):
            if i % j ==0:
                toplam +=j
        if toplam ==i:
            print(f"{toplam} Bir Mükemmel sayıdır")


def problem2():
    def ebob(a,b):
        a_bölenler = []
        b_bölenler = []
        ortak =[]
        for j in range(1,a+1):
            if a %j ==0:
                a_bölenler.append(j)
        for k in range(1, b + 1):
            if b % k == 0:
                b_bölenler.append(k)
        for i in a_bölenler:
            if i in b_bölenler:
                ortak.append(i)
        return max(ortak)
    while True:
        print("""
                ==== EBOB BULMA ====
        """)
        a = input("1.Sayı : ")
        b = input("2.Sayı : ")
        if a.lower() == "q" or b.lower() == "q":
            print("Çıkış Yapılıyor...")
            break
        print("EBOB : {}".format(ebob(int(a),int(b))))


def problem3():
    def ekok(a,b):
        k =1
        while True:
            if (k % a ==0) and (k % b == 0):
                return k
            k +=1
    while True:
        print("""
                ==== EKOK BULMA ====
            """)
        a = input("1.Sayı : ")
        if a.lower() == "q":
            print("Çıkış Yapılıyor...")
            break

        b = input("2.Sayı : ")
        if b.lower() == "q":
            print("Çıkış Yapılıyor...")
            break
        print("EKOK : {}".format(ekok(int(a),int(b))))


def problem4():
    print(""""
            ===== YAZIDAN SESE =====
    """)
    birler = ["Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz",""]
    onlar = ["On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]
    def okuma(sayı):
        sayı_list = list(str(sayı))
        return onlar[int(sayı_list[0])-1]+" "+birler[int(sayı_list[1])-1]
    while True:
        a = input("Sayı : ")
        if a.lower() == "q":
            print("Program Sonlanıyor...")
            break
        a = int(a)
        print(okuma(a))
def problem5():
    def pisagorMu():
        for i in range(1,101):
            for j in range(1,101):
                c = (i**2 + j**2)**0.5
                if c == int(c):
                    print(f"{i} ve {j} Pisagor Üçgeni Oluşturur [Diğer Kenar : {int(c)}]!")
    pisagorMu()

while True:
    secim = input("Seçiminiz [1-5] : ")
    if secim.lower() == "q":
        print("Program Sonlanıyor...")
        break
    elif secim == "1":
        problem1()
    elif secim == "2":
        problem2()
    elif secim == "3":
        problem3()
    elif secim == "4":
        problem4()
    elif secim == "5":
        problem5()




