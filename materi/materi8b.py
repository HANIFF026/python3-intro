#struktur fungsi tanpa parameter

def halo_dunia():
    ("hello world")
    ("hello dunia")

#cara akses function,sertakan nama dan () -nya
halo_dunia()

#funsi dgn parameter (variable fungsi)
def sapa_sapa_gan(nma):
    print("halo",__name__,"selamat gawe di hsi")
def rumus_luas_segi_tiga(alas,tinggi):
    print("Alas:",alas)
    print("Tinggi:",tinggi)
    rumusan = 1/2 * (alas *tinggi)
    print("hasil:",rumusan)

sapa_sapa_gan("Ujang")
sapa_sapa_gan("Asep")
#klo manual begini
print("halo Ujang selamat gawe di hsi")
print("halo Asep selamat gawe di hsi")
rumus_luas_segi_tiga(10,30)
rumus_luas_segi_tiga(50,100)

def rumus_keliling_persegi_panjang(panjang,lebar,tinggi):
    print("Panjang:",panjang)
    print("Lebar:",lebar)
    print("Tinggi:",tinggi)
    rumusan = panjang * lebar * tinggi
    print("hasil:",rumus_keliling_persegi_panjang)

rumus_keliling_persegi_panjang(20,13,10)

def rumus_luas_layang_layang(d1,d2):
    print("D1:",d1)
    print("D2:",d2)
    rumus_luas_layang_layang = 1/2 * d1 * d2
    print("")

def filter_teman_toxic(nama, sifat):
    #ciri ciri toxic
    sifat_toxic =[
        "julid",
        "pamer",
        "ngatain",
        "baperan",
        "drama",
        "sombaong",
    ]
    
    #deteksi kata sifat toxic dari parameter sifat
    if  any(kata in sifat for kata in sifat_toxic):
        print(nama, "itu teman toxic, kaboor")  
    else:
        print(nama,"temen baik, lanjutkan...")

filter_teman_toxic("azka","rajin,baik hati,tawadhu")
filter_teman_toxic("asep","sombong manipulatif drama")