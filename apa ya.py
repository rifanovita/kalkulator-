# Input data
jenis_kelamin = input("Jenis kelamin (Laki-laki/Perempuan): ").lower()
usia = int(input("Usia (tahun): "))
berat = float(input("Berat badan (kg): "))
tinggi = float(input("Tinggi badan (cm): "))
aktivitas = input("Aktivitas (Rendah/Sedang/Tinggi): ").lower()

# Rumus Harris-Benedict
if jenis_kelamin == "laki-laki":
    bmr = 66.5 + (13.75 * berat) + (5.003 * tinggi) - (6.75 * usia)
else:
    bmr = 655.1 + (9.563 * berat) + (1.850 * tinggi) - (4.676 * usia)

# Faktor Aktivitas
if aktivitas == "rendah":
    tdee = bmr * 1.2
elif aktivitas == "sedang":
    tdee = bmr * 1.55
else:
    tdee = bmr * 1.9

# Output hasil
print(f"\nKebutuhan kalori harian: {tdee:.2f} kalori.")
