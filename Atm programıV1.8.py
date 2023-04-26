
hesaplar= {
    "111":{
        'ad': 'arda  ',
        'sifre': '111',
        'bakiye': 3000,
        'ekHesap': 2000,
        'hesapNo':"111"
        },

    "222" : {
        'ad': 'Onur ',
        'sifre': '222',
        'bakiye': 2500,
        'ekHesap': 1000,
        'hesapNo':"222"
        }
}


def giris(hesapNo,sifre):
    for hesap in hesaplar:
        if hesap==hesapNo:
            #print("hesap no doğru")
            if sifre==hesaplar[hesapNo]["sifre"]:
                print("Sisteme giriş yaptınız \n Hoşgeldiniz \n Sayın {}".format(hesaplar[hesap]["ad"]))
                menu(hesap)
                online=True
            else:
                print("Sifre hatalı")
                online=False
            break
        else:
            print("Kullanıcı bilgileri yanlış")
            online=False
            break
    return online
    
def menu(hesapNo):
        islem=input("Lütfen İşlem yapmak için şeçim yapınız \n Para çekme: 1 \n Bakiye Sorgulama: 2 \n Para transferi: 3 \n İşlem : ")
        if islem=="2":
            print("Bakiye Sorgulama İşlemi")
            bakiyeSorgulama(hesapNo)
        elif islem=='1':
            print("Para Çekme")
            paraCekme(hesapNo)
        elif islem=='3':
            havale(hesapNo)
        else:
            print('hatalı işlem yaptınız')

def havale(hesap):
    tpara=int(input("göndermek istediğiniz parayı giriniz"))
    if tpara<hesaplar[hesap]["bakiye"]:
        thesap=int(input("göndermek istediğiniz hesabı giriniz"))
        for no in hesaplar:
            if thesap==no:
                print("para tranferi olabilir")
            else:
                print("girilen hesabı kontrol ediniz")
                break
    else:
        print("bakiyenizde yeterli para yoktur")


            
def bakiyeSorgulama(hesap):
    print("Sayın {} {} numaralı hesabınızdaki bakiye:".format(hesaplar[hesap]['ad'],hesap))
    print("Ana Bakiye: {}".format(hesaplar[hesap]["bakiye"]))
    print("Ek Hesap Bakiye: {}".format(hesaplar[hesap]["ekHesap"])),
    islem=input("Ana Menü: 1 \n Çıkış: 2 \n İşlem: ")
    if islem=="1":
        menu(hesap)
        
def paraCekme(hesap):
     para=int(input("Ne kadar para çekmek istersiniz:"))
     if para>hesaplar[hesap]["bakiye"]:
         print("Yetersiz bakiye, ek hesap kullanmak istermisiniz: \n Evet:1 \n Hayır:2 ")
         secim=input('...')
         if secim=='1':
             if hesaplar[hesap]['bakiye']+hesaplar[hesap]['ekHesap']>=para:
                kalan=hesaplar[hesap]['bakiye']-para
                hesaplar[hesap]['bakiye']=0
                kalan2=hesaplar[hesap]['ekHesap']+kalan
                print("bakiyeniz 0, ek hesabınızda {} bu kadar para kaldı".format(kalan2))
                hesaplar[hesap]['ekHesap']=kalan2
                menu(hesap)
             else:
                 print("Ek hesabınız ve bakiyeniz yetersizdir.")
                 menu(hesap)
         elif secim=='2':
            menu(hesap)
         
     elif para<=hesaplar(hesaplar[hesap]['bakiye']):
         print((hesaplar[hesap]['bakiye'])-para,"hessabınızda bu kadar para kalmıştır")
        
online=False
sayac=0
while online==False:
    if sayac<3:
        sayac+=1        
        g_hesap=input("Hesap No:")
        g_sifre=input("Şifre:")
        if sayac==2:
            print("2 kez şifrenizi yanlış girdiniz, bir daha yanlış girerseniz hesabınız bloke olacaktır")
            g_hesap=input("Hesap No:")
            g_sifre=input("Şifre:")
        online=giris(g_hesap,g_sifre)
    else:
        print("hesabınız bloke olmuştur")
        break
                 
giris(g_hesap,g_sifre)   
