def ikiyleçarp(x):
    return x*2
print(ikiyleçarp(5))
print("""

=====================
=====================
=====================

""")
ikiyleçarp2 = lambda x  : print(x*2)
ikiyleçarp2(5)
def toplama(x,y,z):
    return x+y+z
print(toplama(5,6,7))
toplama2 = lambda x,y,z : x+y+z
print(toplama2(5,6,7))


def tersçevir(s):
    return s[::-1]
print(tersçevir("Python"))
tersçevir2 = lambda s:s[::-1]
print(tersçevir2("Python Programlama..."))
def ÇiftTek(sayı):
    return sayı % 2==0
sayı = 6
if ÇiftTek(sayı):
    print("Sayı Çift")
else:
    print("Sayı Tek !")
ÇiftTek2 = lambda sayı : sayı % 2 ==0
if ÇiftTek2(5):
    print("sayı Çift")
else:
    print("Sayı Tek")