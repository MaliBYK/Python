print("""
        ************************

            FAKTÖRİYEL BULMA
            
        ************************
""")
while True:
    sayı = input("Sayı : ")
    if sayı.lower() == "q":
        print("Program Sonlandırılıyor...")
        break
    sayı = int(sayı)
    faktöriyel = 1
    for i in range(2,sayı+1):
        faktöriyel *=i
    print(f"Faktöriyel : {faktöriyel}")
