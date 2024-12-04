# operasi komparasi/perbandingan

# perhatikan
"""
   Hasil dari operasi komparasi 
   selalu bertipe data bolean
   (true/false)
"""
# >,<,>=,<=,==,!=, is, dan is not

a = 4
b = 2

# lebih dari >
print("===Lebih dari (>)")
hasil = a > 3 # TRUE
print(a, ">", 3, "=", hasil)
hasil = b < 3 # FALSE
print(b, "<", 3, "=", hasil)
hasil = b > 2
print(b, ">", 2, "=", hasil)

# kurang dari <
print("===Kurang dari (<)")
hasil = a < 3 # FALSE
print(a, "<", 3, "=", hasil)
hasil = b < 3 # TRUE
print(b, "<", 3, "=", hasil)
hasil = b < 2 # FALSE
print(b, "<", 2, "=", hasil)

# lebih dari sama dengan >=
print("===Lebih dari sama dengan (>=)")
hasil = a >= 3 # TRUE
print(a, ">=", 3, "=", hasil)
hasil = b >= 3 # FALSE
print(b, ">=", 3, "=", hasil)
hasil = b >= 2 # TRUE
print(b, ">=", 2, "=", hasil)

# Kurang dari sama dengan <=
print("===Kurang dari sama dengan (<=)")
hasil = a <= 3 # FALSE
print(a, "<=", 3, "=", hasil)
hasil = b <= 3 # TRUE
print(b, "<=", 3, "=", hasil)
hasil = b <= 2 # TRUE
print(b, "<=", 2, "=", hasil)

# Sama dengan ==
print("===sama dengan (==)")
hasil = a == 3 # FALSE
print(a, "==", 3, "=", hasil)
hasil = b == 3 # FALSE
print(b, "==", 3, "=", hasil)
hasil = b == 2 # TRUE
print(b, "==", 2, "=", hasil)

# Tidak sama dengan !=
print("===Tidak sama dengan (!=)")
hasil = a != 3 # FALSE
print(a, "!=", 3, "=", hasil)
hasil = b != 3 # TRUE
print(b, "!=", 3, "=", hasil)
hasil = b != 2 # FALSE
print(b, "!=", 2, "=", hasil)