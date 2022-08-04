print("""************
ATM İşlemleri
1.Bakiye Sorgulama
2.Para Yatırma
3.Para Çekme
*************""")
bakiye = 2000

while True:
    islem = int(input("lütfen yapmak istediginiz işlemi seçiniz"))
    if (islem == "q"):
        print("hoşçakalın")
        break
    elif (islem == 1):
        print("hesabınızda {} tl vardır".format(bakiye))
    elif (islem == 2):
        miktar = int(input("yatırılacak tutarı giriniz"))
        bakiye += miktar
    elif (islem == 3):
        miktar = int(input("Çekmek istediğiniz tutar:"))
        if (bakiye - miktar < 0):
            print("Bu kadar para çekemezsiniz...")
            print("Bakiyeniz {} tldir".format(bakiye))

        bakiye -= miktar

    else:
        print("gecersiz işlem")

