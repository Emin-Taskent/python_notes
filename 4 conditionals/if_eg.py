print("Merhaba, Vücut Kitle Endeksi Hesaplama Uygulamasına hoşgeldiniz!")

Boy=int(input("Lütfen Boyunuzu cm Cinsinden Giriniz:"))
Kilo=int(input("Lütfen Kilonuzu Giriniz:"))

Endeks=round((Kilo)/((Boy/100)**2),2)

if Endeks<=18.5:
    print("Vücut Kitle Endeksiniz {}'dir. Düşük Kilolu Grubundasınız!".format(Endeks))
elif Endeks>18.5 and Endeks<=24.9:
    print("Vücut Kitle Endeksiniz {}'dir. Normal Kilolu Grubundasınız!".format(Endeks))
elif Endeks>24.9 and Endeks<=29.9:
    print("Vücut Kitle Endeksiniz {}'dir. Fazla Kilolu Grubundasınız!".format(Endeks))
elif Endeks>29.9 and Endeks<=40:
    print("Vücut Kitle Endeksiniz {}'dir. Obez Grubundasınız!".format(Endeks))
elif Endeks>40:
    print("Vücut Kitle Endeksiniz {}'dir. Aşırı Obez Grubundasınız!".format(Endeks))
else:
    print("Hatalı işlem Yaptınız, Tekrar deneyiniz...")