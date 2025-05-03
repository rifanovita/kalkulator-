def hitung_risiko_diabetes(usia, bmi, riwayat_keluarga):
    skor_risiko = 0

    # Penilaian berdasarkan usia
    if usia >= 45:
        skor_risiko += 2
    elif usia >= 30:
        skor_risiko += 1

    # Penilaian berdasarkan BMI
    if bmi >= 30:
        skor_risiko += 2
    elif bmi >= 25:
        skor_risiko += 1

    # Penilaian riwayat keluarga
    if riwayat_keluarga.lower() == 'ya':
        skor_risiko += 2

    # Interpretasi risiko
    if skor_risiko >= 5:
        return "Risiko tinggi terkena diabetes. Disarankan periksa ke dokter."
    elif skor_risiko >= 3:
        return "Risiko sedang terkena diabetes. Jaga pola hidup sehat."
    else:
        return "Risiko rendah terkena diabetes."

# Input dari pengguna
print("=== Kalkulator Risiko Diabetes Sederhana ===")
usia = int(input("Masukkan usia Anda: "))
bmi = float(input("Masukkan BMI Anda: "))
riwayat_keluarga = input("Apakah Anda memiliki riwayat keluarga diabetes? (ya/tidak): ")

# Output hasil
hasil = hitung_risiko_diabetes(usia, bmi, riwayat_keluarga)
print("\nHasil Penilaian:")
print(hasil)
