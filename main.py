# Ödev - 1

# Mustafa Alp YANIKOĞLU

# Python'da kullanılan veri tipleri:
    # String: Metinsel ifadelerin çıktılarının olduğu veri tipidir.
    # Numeric: Sayı veya rakam çıktılarının olduğu veri tipidir.
        # Intager: Tam sayı veri tipidir.
        # Float: Ondalık sayı veri tipidir.
    # Boolean: True veya False çıktıları veren mantıksal veri tipidir.
    # Sequence: Sıralama veya liste yapma veri tipidir.
    # Mapping: Haritalama veri tipidir.
    # Set: Birden fazla türün bulunduğu küme olan veri tipidir.

# kodlama.io sitesi üzerinde bulunan bazı değişken tipleri
    # Kodlama.io sitesinde yer alan bütün metinsel ifadeler string veri tipine sahiptir.
    # Sitede yer alan tüm tam sayılar integer veri tipine örnektir.
    # Sitede yer alan "giriş yap" kısmı boolean veri tipine örnek olabilir.

title = "(2023) Yazılım Geliştirici Yetiştirme Kampı - Python & Selenium" # String veri tipidir.

percentCompleted = 14 # Numeric veri tipidir

ePosta = "a@gmail.com"
password = "123"

loginePosta = "a@gmail.com"
loginPassword = "123"

if ePosta == loginePosta:
    if password == loginPassword:
        print("Giriş başarılı")
    else:
        print("E-posta veya şifreniz yanlıştır.")
else:
    print("Girilen e-posta yanlıştır.")