print("Kalkulator Kebutuhan Kalori")

# Input data
jenis_kelamin = input("Masukkan jenis kelamin (Laki-laki/Perempuan): ").lower()
usia = int(input("Masukkan usia (tahun): "))
berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (cm): "))
aktivitas = input("Masukkan tingkat aktivitas (Rendah/Sedang/Tinggi): ").lower()

# Rumus Harris-Benedict
if jenis_kelamin == "laki-laki":
    bmr = 66.5 + (13.75 * berat) + (5.003 * tinggi) - (6.75 * usia)
elif jenis_kelamin == "perempuan":
    bmr =  655.1 + (9.563 * berat) + (1.850 * tinggi) - (4.676 * usia)
else:
    print("Jenis kelamin tidak valid!")
    exit()

# Faktor Aktivitas
if aktivitas == "rendah":
    tdee = bmr * 1.2
elif aktivitas == "sedang":
    tdee = bmr * 1.55
elif aktivitas == "tinggi":
    tdee = bmr * 1.9
else:
    print("Tingkat aktivitas tidak valid!")
    exit()

# Hasil
print(f"\nKebutuhan kalori harian kamu adalah {tdee:.2f} kalori.")
