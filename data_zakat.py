import csv
import os

print("===========================================")
print("Selamat datang di program penginputan zakat")
print("===========================================")

# codding file start

file_csv = "data_zakat.csv"

if not os.path.exists(file_csv):
    with open(file_csv, mode = "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["nama", "jenis_zakat", "jumlah_jiwa", "jumlah_zakat"])

def data_sudah_terdaftar(data_baru):
    with open(file_csv, mode = "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader :
            if row[0] == data_baru:
                return True
    return False
# codding file end

# codding program start
while True:
    print("============= input data zakat========")

    nama = input("masukkan nama : ")
    
    print("""
        Pilih jenis zakat:
        1. Zakat Fitrah
        2. Zakat Mal
        3. Zakat Emas
        4. Zakat Perak
        """)

    pilihan = int(input("Masukkan pilihan (1-4): "))

    if pilihan == 1:
        jiwa = int(input("Masukkan jumlah jiwa: "))
        zakat = jiwa * 2.5
        jenis = "Zakat Fitrah"

    elif pilihan == 2:
        harta = float(input("Masukkan total harta (Rp): "))
        zakat = harta * 0.025
        jenis = "Zakat Mal"

    elif pilihan == 3:
        emas = float(input("Masukkan berat emas (gram): "))
        zakat = emas * 0.025
        jenis = "Zakat Emas"

    elif pilihan == 4:
        perak = float(input("Masukkan berat perak (gram): "))
        zakat = perak * 0.025
        jenis = "Zakat Perak"

    else:
        print("Pilihan tidak valid!")
        exit()

    konfirmasi = input("Apakah data sudah benar? [y/n]: ").lower()

    if konfirmasi == "y":
        with open(file_csv, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([nama, jenis, jiwa, zakat])


        print("\n====== DATA ZAKAT ======")
        print(f"Nama          : {nama}")
        print(f"Jenis Zakat   : {jenis}")
        print(f"jumlah jiwa   : {jiwa}")
        print(f"Jumlah Zakat  : {zakat}")
        print("========================")
    else:
        print("Penginputan dibatalkan.")
# codding program end