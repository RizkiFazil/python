
import random
fazil = random.randint(1,5)

print("********************")
print("******haloooo!******")
print("*bagaimana kabarmu?*")
print("********************")


nama_kamu = input("masukkan namamu: ")
print(f'''halloo {nama_kamu} bagaimana perasaanmu hari ini? ''')

pilihan_kamu = input("ketik perasaan mu: ").strip().lower()

if pilihan_kamu == "baik":
    print(f"syukurlah kamu baik-baik saja, semoga harimu menyenangkan!")
else:
    print("kamu kenapa? jika kamu ingin nangis, jangan sungkan untuk nangis yaa...")

print("oiya aku ada sedikit games untuk menghiburmu, kamu mau coba ga?")

jawabamu = input("ketik jawabanmu: ").strip().lower()

if jawabamu == "mau":
    print("ayo main")
    
    print(f'''halooo {nama_kamu}! coba perhatikan goa dibawah ini! 
          |_| |_| |_| |_| |_|''')

    try: tebakan = int(input("menurut kamu dimana fazil berada? [1], [2], [3], [4], [5]: "))
    except ValueError:
        print("harus angka yaa ")
    
    if tebakan == fazil:
        print(f"selamat {nama_kamu}! fazil ada di goa nomor {fazil} ")
    else:
        print(f"belum tepat fazil ada di goa nomor {fazil}, tapi kamu sudah hebat mencoba 💪")

else:
    print(f"kenapa kamu {jawabamu}? kalau kamu butuh tempat untuk cerita, hubungi aku ya!!!")