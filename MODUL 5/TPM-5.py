# Input apakah pengguna memiliki kartu member
kartu_member = input("Apakah Anda punya kartu member? (ya/tidak): ")

if kartu_member == "ya":
    # Jika punya kartu member, cek belanjaan
    belanja = float(input("Berapa total belanja Anda? Rp."))
    #if belanja > 500:
        #print("Selamat Anda mendapatkan diskon 50rb.")
    #elif belanja > 100:
        #print("Selamat Anda mendapatkan diskon 15rb.")
    #else:
       # print("Anda tidak mendapatkan diskon.")
        
elif kartu_member == "tidak":
    # Jika tidak punya kartu member, cek belanjaan
    belanja = float(input("Berapa total belanja Anda? Rp. "))
    if belanja > 100:
        print("Selamat Anda mendapatkan diskon 10rb.")
    else:
        print("Anda tidak mendapatkan diskon.")
else:
    print("Input tidak valid. Silakan masukkan 'ya' atau 'tidak'.")