# percabangan
# menggunakan statment IF

# struktur
"""
    1. if-nya
    2. Ada kondisi (bernilai TRUE/FALS)
    3. Ada Aksi -> proses lanjutan
"""

nama = input("masukkan nama anda = ")

# If statement dalam bentuk inline (satu baris)
# if nama == "azza" : print(f"selamat datang {nama}")
# print("Terima kasih")

# if statement dalam bentuk indentasi
#if nama == 'azza' :
 #    print(f'Selamat Datang {nama}')
#print("Terima kasih")

# IF-ELSE Statement
if nama == 'azza':
    # aksi 1
    print(f'selamat datang {nama}')
else:
    # aksi 2
    print(f'kamu {nama}, bukan azza')
print('terima kasih')
