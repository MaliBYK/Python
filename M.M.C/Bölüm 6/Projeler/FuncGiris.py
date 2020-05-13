def faktöriyel(sayı):
    faktöriyel =1
    if sayı != 0:
        for i in range(1,sayı+1):
                faktöriyel *=i
    print(faktöriyel)
faktöriyel(5)