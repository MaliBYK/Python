def bilgiler(ad ="Bilgi Yok",soyad = "Bilgi Yok",numara = "Değer Yok"):
    print(f"Ad: {ad}\nSoyad : {soyad}\nNumara : {numara}")
bilgiler()
print()
bilgiler("Ahmet")
print()
bilgiler(numara = 15978)
print("""
=========================
=========================
=========================
""")

def toplama(*sayılar):
    toplam =0
    for i in sayılar:
        toplam +=i
    return toplam
print(toplama(5,6,7,8,9,9,10))
