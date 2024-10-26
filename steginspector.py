# StegInspector
# ;)
#--------------
#
# Program ini merupakan hasil analisis saya
# yang membandingkan output dari dua file 
# menggunakan perintah `strings`, di mana output 
# dari masing-masing file:
#
#--------------------------+-----------------------------------------------+
# File Gambar Biasa        | File Gambar Stego                             |
#--------------------------+-----------------------------------------------+
# JFIF                     | JFIF                                          |
# (ICC_PROFILE             | $3br                                          |
# mntrRGB XYZ              | %&'()*456789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz |
# acsp                     |         #3R                                   |
#         desc             | &'()*56789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz   |
# trXYZ                    |                                               |
# gXYZ                     |                                               |
# bXYZ                     |                                               |
# rTRC c                   |                                               |
# (gTRC                    |                                               |
# (bTRC                    |                                               |
# (wtpt                    |                                               |
# cprt                     |                                               |
# <mluc                    |                                               |
# enUS                     |                                               |
# XYZ                      |                                               |
# XYZ                      |                                               |
# XYZ                      |                                               |
# para                     |                                               |
# XYZ                      |                                               |
# -mluc                    |                                               |
# enUS                     |                                               |
#--------------------------+-----------------------------------------------+


# Import modul yang dibutuhkan 
import subprocess
import platform
import time
import re
import os

# Variabel warna
m = "\033[31m" # Merah
h = "\033[32m" # Hijau 
k = "\033[33m" # Kuning 
b = "\033[34m" # Biru
c = "\033[36m" # Cyan
p = "\033[37m" # Putih 
r = "\033[0m"  # Reset 

# Cek sistem operasi 
sistem_operasi = platform.system()
# Android (Termux) & Linux
if sistem_operasi == "Linux":
    os.system("clear")
else:
    print(f"{p}[{m}-{p}] Sistem operasi Anda tidak mendukung untuk menjalankan program StegInspector.{r}")
    exit(1)

# Banner program
print(f"""
{c}╔═╗╔╦╗╔═╗╔═╗╦╔╗╔╔═╗╔═╗╔═╗╔═╗╔╦╗╔═╗╦═╗{r}
{c}╚═╗ ║ ║╣ ║ ╦║║║║╚═╗╠═╝║╣ ║   ║ ║ ║╠╦╝{r}
{c}╚═╝ ╩ ╚═╝╚═╝╩╝╚╝╚═╝╩  ╚═╝╚═╝ ╩ ╚═╝╩╚═{r}

{p}[{b}*{p}] Program   : {b}StegInspector{r}
{p}[{b}*{p}] Deskripsi : {b}Program Python untuk mengecek file stego{r}
{p}[{b}*{p}] Pembuat   : {b}fixploit03{r}
{p}[{b}*{p}] Github    : {b}https://github.com/fixploit03/StegInspector/{r}
{p}[{b}*{p}] Team      : {b}ArSec (Arjuna Security){r}
""")

# Meminta nama file stego dari pengguna.
while True:
    try:
        file_stego = input(f"{p}[{b}#{p}] Masukkan nama file stego: ")
        if not file_stego:
            print(f"{p}[{m}-{p}] File stego tidak boleh kosong.{r}")
            continue 
        if not os.path.isfile(file_stego):
            print(f"{p}[{m}-{p}] File stego '{file_stego}' tidak ditemukan.{r}")
            continue
        # Cek ekstensi file stego
        if not file_stego.endswith((".jpg", ".jpeg", ".bmp", ".wav", ".au")):
            print(f"{p}[{m}-{p}] File '{file_stego}' bukan file stego.{r}")
            continue
        break
    except KeyboardInterrupt:
        print(f"\n{p}[{m}-{p}] Program dihentikan oleh pengguna.{r}")
        exit(1)
    except Exception as e:
        print(f"{p}[{m}-{p}] Terjadi kesalahan: {e}{r}")
        exit(1)
        
print(f"{p}[{b}*{p}] Mengecek file stego '{file_stego}'...{r}")
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
            print(f"{p}[{h}+{p}] File '{file_stego}' adalah file stego.{r}")
        else:
            print(f"{p}[{m}-{p}] File '{file_stego}' bukan file stego.{r}")
except KeyboardInterrupt:
        print(f"\n{p}[{m}-{p}] Program dihentikan oleh pengguna.{r}")
        exit(1)
except Exception as e:
  print(f"{p}[{m}-{p}] Terjadi kesalahan: {e}{r}")
