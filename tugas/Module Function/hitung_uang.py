def tambah_bonus(uang_list):
    uang_tambah = list(map(lambda uang: uang +50000, uang_list))

    return uang_tambah

def filter_uang_boros(uang_list):
    uang_boros = list(filter(lambda uang_gede:uang_gede >= 50000, uang_list))

    return uang_boros