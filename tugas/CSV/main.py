import csv

# baca semua data dari csv
with open("keuangan.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    data = list(reader)
print(data)

print("\n")


# 1. tampilkan semua data
print("😂semua data:")
for row in data:
    print(f"{row["Tanggal"]} | {row["Keterangan"]} | {row["Kategori"]} | Rp.{row["Jumlah"]}")

# 2.Hitung semua pengeluaran
total = sum(int(row["Jumlah"]) for row in data) 
print(f"😂Total pengeluaran: Rp.{total}")

# 3. Hitung Total per kategori
kategori_total = {}
for row in data:
    kategori = row["Kategori"]
    jumlah = int(row["Jumlah"])
    if kategori not in kategori_total:
        kategori_total[kategori] = 0
    kategori_total[kategori] += jumlah

print(f"😊 pengeluaran per kategori : ")
for kategori, jumlah in kategori_total.items():
    print(f" {kategori} : Rp.{jumlah}")