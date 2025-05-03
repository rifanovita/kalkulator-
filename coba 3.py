gula = float(input("Masukkan kadar gula darah puasa (mg/dL): "))

if gula < 100:
    print("Normal")
elif gula < 126:
    print("Pra-diabetes")
else:
    print("Kemungkinan Diabetes")
