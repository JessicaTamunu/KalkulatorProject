def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Error: Tidak bisa membagi dengan nol!"
    return a / b

def main():
    print("=== KALKULATOR SEDERHANA ===")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")

    pilihan = input("Pilih operasi (1-4): ")

    a = float(input("Masukkan angka pertama: "))
    b = float(input("Masukkan angka kedua: "))

    if pilihan == "1":
        print("Hasil:", tambah(a, b))
    elif pilihan == "2":
        print("Hasil:", kurang(a, b))
    elif pilihan == "3":
        print("Hasil:", kali(a, b))
    elif pilihan == "4":
        print("Hasil:", bagi(a, b))
    else:
        print("Pilihan tidak valid.")

main()