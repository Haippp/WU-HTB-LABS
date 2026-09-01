# The Last Dance
![](https://img.shields.io/badge/challange_by-HackTheBox-green) ![](https://img.shields.io/badge/difficulty-VeryEasy-blue)

## 📝Deskripsi Challange
Anda sedang memburu sebuah kelompok kejahatan terorganisir yang bertanggung jawab atas peredaran senjata ilegal di negara Anda. Sebagai agen rahasia, Anda telah berhasil menyusup ke dalam kelompok tersebut hingga diizinkan menghadiri pertemuan dengan para klien. Selama negosiasi terakhir, Anda menemukan salah satu pesan rahasia untuk pelanggan tersebut. Pesan itu berisi informasi penting mengenai pengiriman. Apakah Anda yakin bisa memecahkan kodenya?

## 🧩Penyelesaian
Inti dari enkripsi nya ada disini:
```python
ct.append((123 * char + 18) % 256)
```
Kita tahu bahwa secara matematis, alur enkripsi nya itu seperti ini:
```math
123 \times char = (result + 18) \mod 256
```
Jadi tugas kita sekarang tinggal perlu membalik alurnya aja. yaitu :
```math
char - 18 = result \times modinverse(123) \mod 256
```
Kenapa mod inverse? karena dalam dunia modular tidak ada pembagian, dan kebalikan dari perkalian adalah modular inverse dari nilai perkalian itu.

coding lengkapnya bisa di lihat di [solve.py](./solve.py)