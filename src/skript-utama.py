from luas.persegi import luas_persegi as Lp
from luas.lingkaran import luas_lingkaran as Ll
from luas.segitiga import luas_segitiga as Ls
print("menghitung luas persegi")
sisi = 10 
luas = Lp(sisi)
print("sisi= ", {sisi})
print(f"luas= ", {luas})
print("=================")
print("menghitung luas lingkaran")
radius =25
luas = Ll(radius)
print("radius= ", {radius})
print(f"luas= ", {luas})
print("=================")
print("menghitung luas segitiga")
alas= 6
tinggi = 8
luas = Ls(alas,tinggi)
print("alas= ", {alas})
print("tinggi= ", {tinggi})
print(f"luas= ", {luas})
print("=================")


from volume.bola import volume_bola as Vb
from volume.kubik import volume_kubik as Vk
from volume.prisma import volume_prisma as Vp
print("menghitung volume bola")
radius = 10
volume = Vb(radius)
print("radius= ", {radius})
print(f"volume= ", {volume})
print("=================")
print("menghitung volume kubik")
sisi = 4
volume = Vk(sisi)
print("sisi= ", {sisi})
print(f"volume= ", {volume})
print("=================")
print("menghitung volume prisma")
As = 5
Ts = 7
Tp = 4
volume = Vp(As,Ts,Tp)
print("As =", {As})
print("Ts =", {Ts})
print("Tp= ", {Tp})
print(f"volume= ", {volume})
print("===============")





