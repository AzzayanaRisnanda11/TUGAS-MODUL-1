# format string

"""
 string: kumpulan dari karakter
cara membuat string :
1. dengan single qoute '...'
2. dengan double qoute "..."
"""
# membuat string dengan single qoute
nama = 'nama saya azzayana'
print(nama)

# membuat string dengan double qoute
nama = "nama saya azzayana"
print(nama)

print("nama saya azzayana")
print("jangan lupa sholat jum'at")

# maksa harus single qoute
# pakai tanda \
print('g\'day')
print('what\'sUp!')

print('c:\\user\\azza')

nama = "Azza"
print("Selamat Datang", nama)

# format string 'f' dan '{}'
format_str = f'Selamat Datang' = {nama}
print(format_str)

# format string angka
angka = 2005.5
format_str = f'angka = {angka}'
print(format_str)

# bilangan dengan ordo ribuan
angka = 2000000
format_str = f'jutaan = {angka}'
print(format_str)

# bilangan desimal 
angka = 2005.54321
format_str = f'desimal = {angka: .3f}'
print(format_str)

# persen
angka = 0.55 # 0.55 * 100 = 55%
format_str = f'persen = {angka:%}'
print(format_str)

# operasi aritmatika dengan format string
harga = 57250
jumlah = 3

print(f'total bayar : {harga*jumlah:,}')