print("Kalkulator Diabetes (bukan diagnosis)")

print("Pilih jenis pengukuran:")
print("1. Gula darah puasa")
print("2. Gula darah 2 jam setelah makan")
print("3. Gula darah sewaktu/acak")

pilih = input("Masukkan pilihan (1/2/3): ")
gula = float(input("Masukkan kadar gula darah (mg/dL): "))

if pilih == "1":
    if gula < 100:
        print("Normal")
    elif gula < 126:
        print("Pra-diabetes")
    else:
        print("Kemungkinan Diabetes")
elif pilih == "2":
    if gula < 140:
        print("Normal")
    elif gula < 200:
        print("Pra-diabetes")
    else:
        print("Kemungkinan Diabetes")
elif pilih == "3":
    if gula < 200:
        print("Mungkin Normal atau Pra-diabetes")
    else:
        print("Kemungkinan Diabetes")
else:
    print("Pilihan tidak valid.")
