
print("materi 7b - python data structure")
print("=========================")
#set -> {} ->tdk berubah, berurutan, tdk duplikat
daftar_hanif = {"pou", "ff",}
daftar_syamil = {"mlbb", "gta",}
daftar_hanif = {"footrabll",}
print("Hanif game", daftar_hanif)
print("syamil game", daftar_syamil)

# .add() -> menambahkan item baru
daftar_hanif.add("pug")
daftar_syamil.add("mlbb")#tdk akan bertambah
daftar_hanif.add("football")

# .remove -> menghapus item
daftar_hanif.remove("pug",)
daftar_syamil.remove("mlbb",)

#len() -> menghitung jumlah item
print("Hanif ada", len(daftar_hanif),"games:",daftar_hanif)
print("Evan ada", len(daftar_hanif),"games:",daftar_hanif)

#.union() -> MENGGABUNGKAN 2 set barbeda
game_berdua = daftar_hanif.union(daftar_syamil)
total_game = len(game_berdua)
print("semua yang beda ada", len)

# intersection() -> mencari item yg kembar
game_kembar = daftar_hanif.intersection(daftar_syamil)
total_game = len(game_kembar)
print("game yang beda ada", daftar_hanif,"daftar:", game_kembar)

#difference()-> mencari item yg berbeda
daftar_hanif = daftar_syamil.difference(daftar_syamil)
total_beda = len(daftar_syamil)
print("game yang beda ada" ,daftar_hanif,"daftar:", daftar_syamil)

koleksi_anime = {
    "re_zero": "subaru",
    "onepieece": "usop",
    "waifu":{
        "re_zero":"rem-chan",
        "demon_slayer":"nezuko"
    }
}

print("koleksi_anime", koleksi_anime)
print("mc one_piecee:", koleksi_anime[" mc one_peicee"])
print("waifu re zero:", koleksi_anime["waifu"]["re zero"])

#menambah / mengubah data
koleksi_anime["naruto"] = "boruto"
koleksi_anime["onepieece"] = "zoro"
koleksi_anime["waifu"]["re_zero"] = "rem kanan"
print("koleksi anime skrg", koleksi_anime)

      





#Dict (dictionary) -> {key:value} / {kunci:isinya}
#berurutan berdasarkan key,berubah
#key tdk boleh duplikat