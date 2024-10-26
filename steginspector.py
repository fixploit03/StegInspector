# StegInspector
# ;)

# Import modul yang dibutuhkan 
import subprocess
import time
import re
import os

# Banner program
print("""
╔═╗╔╦╗╔═╗╔═╗╦╔╗╔╔═╗╔═╗╔═╗╔═╗╔╦╗╔═╗╦═╗
╚═╗ ║ ║╣ ║ ╦║║║║╚═╗╠═╝║╣ ║   ║ ║ ║╠╦╝
╚═╝ ╩ ╚═╝╚═╝╩╝╚╝╚═╝╩  ╚═╝╚═╝ ╩ ╚═╝╩╚═

[*] Program   : Steg2crack
[*] Deskripsi : Program Python untuk meng-crack file stego
[*] Pembuat   : fixploit03
[*] Github    : https://github.com/fixploit03/Steg2crack/
[*] Team      : ArSec (Arjuna Security)
""")

# Meminta nama file stego dari pengguna.
while True:
    try:
        file_stego = input("[#] Masukkan nama file stego: ")
        if not file_stego:
            print(f"[-] File stego tidak boleh kosong.")
            continue 
        if not os.path.isfile(file_stego):
            print(f"[-] File stego '{file_stego}' tidak ditemukan.")
            continue
        # Cek ekstensi file stego
        if not file_stego.endswith((".jpg", ".jpeg", ".bmp", ".wav", ".au")):
            print(f"[-] File '{file_stego}' bukan file stego.")
            continue
        break
    except KeyboardInterrupt:
        print(f"\n[-] Program dihentikan oleh pengguna.")
        exit(1)
    except Exception as e:
        print(f"[-] Terjadi kesalahan: {e}")
        exit(1)
        
print(f"[*] Mengecek file stego '{file_stego}'...")
time.sleep(3)

# Perintah untuk mengecek file stego menggunakan strings 
perintah_cek_file_stego = f"strings {file_stego}"

try:
    # Cek file stego
    cek_file_stego = subprocess.run(perintah_cek_file_stego, shell=True, capture_output=True, text=True)
    if cek_file_stego.returncode == 0:
        # Pola file stego
        pola_file_steghide = r"%&'\(\)\*456789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz\n\s*#3R\n&'\(\)\*56789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz"
        if re.search(pola_file_steghide, cek_file_stego.stdout):
            print(f"[+] File '{file_stego}' adalah file stego.")
        else:
            print(f"[-] File '{file_stego}' bukan file stego.{r}")
except KeyboardInterrupt:
        print(f"\n[-] Program dihentikan oleh pengguna.")
        exit(1)
except Exception as e:
  print(f"[-] Terjadi kesalahan: {e}")
