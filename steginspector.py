# StegInspector
# ;)

import subprocess
import time
import re

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

file_stego = input("[#] Masukkan nama file stego: ")

print(f"[*] Mengecek file stego '{file_stego}'...")
time.sleep(3)

perintah_cek_file_stego = f"strings {file_stego}"

try:
    cek_file_stego = subprocess.run(perintah_cek_file_stego, shell=True, capture_output=True, text=True)
    if cek_file_stego.returncode == 0:
        pola_file_steghide = r"%&'\(\)\*456789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz\n\s*#3R\n&'\(\)\*56789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz"
        if re.search(pola_file_steghide, cek_file_stego.stdout):
            print(f"[+] File '{file_stego}' adalah file stego.")
        else:
            print(f"[-] File '{file_stego}' bukan file stego.{r}")
except Exception as e:
  print(f"[-] Terjadi kesalahan: {e}")
