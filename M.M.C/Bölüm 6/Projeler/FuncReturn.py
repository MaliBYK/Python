def toplama(a,b):
    return a+b
def ikiyleçarp(sayı):
    return sayı*2
def dördeböl(sayı):
    return sayı/4
    print("Bölündü")#return dan sonra olduğu için çalışmadı!

# toplam = toplama(3,4)
# ikiyle_çarpım =ikiyleçarp(toplam)
# print(ikiyle_çarp)

print(dördeböl(ikiyleçarp(toplama(5,3))))
