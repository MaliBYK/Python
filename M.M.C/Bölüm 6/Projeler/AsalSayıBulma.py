def bulma(sayı):
    if sayı == 1 or sayı == 0:
            return False
    for i in range(2,sayı):
        if sayı % i ==0:
            return False
    return True


while True:
    a = input("Sayı : ")
    if a.lower() =="q":
        print("Program Sonlanıyor...")
        break
    a = int(a)
    if bulma(a):
        print("Sayı Asaldır...")
    else:
        print("Sayı Asal Değildir...")
    
