nama_pegawai = input("masukkan nama pegawai")
status_pegawai = input("masukkan status pegawai (tetap/tidak tetap): ")
gaji_pokok = float(input("masukkan gaji pokok: Rp. "))
durasi_lembur = float(input("masukkan durasi lembur (jam): "))


# perhitungan
if status_pegawai == "tetap": # pegawai tetap
   tunjangan = 0.7 * gaji_pokok
   lembur = durasi_lembur * (0.1 * gaji_pokok)
   gaji_bersih = gaji_pokok + tunjangan + lembur 
else: # pegawai tidak tetap 
    tunjangan = 0
    lembur = durasi_lembur * (0.05 * gaji_pokok)
    gaji_bersih = gaji_pokok + lembur

# output
print("\n--- Rincian gaji pegawai ---")
print(f"nama pegawai   : {nama_pegawai}")
print(f"gaji pokok     : Rp{gaji_pokok:,.3f}")
print(f"tunjangan      : Rp{tunjangan:,.3f}")
print(f"durasi lembur  : {durasi_lembur:,.0f} jam")
print(f"gaji bersih    : Rp{gaji_bersih:,.3f}")
print(f"lembur:Rp.{lembur:,.3f}")