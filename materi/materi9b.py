# fungsi biasa dengan def

def hello_world(name):
    print("hello mr.",name)
    print(f"how you doing {name}?")

hello_world("hanif")
hello_world("farhat")
hello_world("royyan")
print("--------->lambda<--------")
# fungsi anonim lambda jika 1 baris

greeting = lambda name: print(f"hello, {name} ")
greeting("faiz")
greeting("azmi")
greeting("umar")
greeting("avicenna")
#""artinya string walaupun angka
nilai_string = "2000"
nilai_integer = int(nilai_string)
kalikan_dua_salah = nilai_string * 2
kalikan_dua_bener = nilai_integer * 2
print(kalikan_dua_salah, kalikan_dua_bener)

# map()
nilai_mentah = [100, 45 , 24 ,67.3 , 98.7]
nilai_bulat = map(lambda nilai : round(nilai), nilai_mentah)
list_nilai_dibulatkan = list(nilai_mentah)
print(f"nilai mentahan: {nilai_mentah}")
print(f"nilai mentah: {nilai_mentah}")

# sorted () mengurutkan data
daftar_angka = [
    {"nama": "umar", "angka": 78},
    {"nama": "avicenna", "angka": 11},
    {"nama": "reza", "angka": 28},
    {"nma": "nahdif", "angka": 27},

]
print("daftar angka siswa", daftar_angka)
daftar_siswa_terurut = sorted(daftar_angka, key=lambda siswa:siswa["angka"])
#for loop -> mengelurkan seluruh isi daftar
for siswa in daftar_siswa_terurut:
    print(siswa)
#sorting list
daftar_nama_kelas_b = ["hanif", "fauzan", "avicenna", "reza", "nadhif", "adzan"]
daftar_siswa_terurut = sorted(daftar_nama_kelas_b)
daftar_siswa_terbalik = sorted(daftar_nama_kelas_b, reverse=True)
for nama in daftar_siswa_terurut:
    print(nama)
print("-----#####------")
for siswa in daftar_siswa_terbalik:
    print(nama)
print("----FILTER------")
#FILTER PENYARING DATA
transaksi = [250000, 678000, 230000, 459000]
transaksi_besar = filter(lambda angka : )
