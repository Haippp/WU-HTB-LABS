# The Last Dance
![](https://img.shields.io/badge/challange_by-HackTheBox-green) ![](https://img.shields.io/badge/difficulty-VeryEasy-blue)

## 📝Deskripsi Challange
To be accepted into the upper class of the Berford Empire, you had to attend the annual Cha-Cha Ball at the High Court. Little did you know that among the many aristocrats invited, you would find a burned enemy spy. Your goal quickly became to capture him, which you succeeded in doing after putting something in his drink. Many hours passed in your agency's interrogation room, and you eventually learned important information about the enemy agency's secret communications. Can you use what you learned to decrypt the rest of the messages?


## 🧩Penyelesaian
Nah disini setalah aku amati lebih lanjut, nonce(iv) itu digunakan 2x pada message dan flag. Artinya keystream untuk meng-xor-kan message dan flag itu kurang lebih sama. Nah maka dari itu kita bisa merecover keystream.

```math
Ciphertext = Keystream \oplus Plaintext
```
Biar aku jelaskan pelan pelan agar bisa memahami cara penyelesaian dengan benar. Kita tahu pada chacha20, keystremam di buat menggunakan key, nonce, dan counter. Kemudian hasil keystream tersebut akan di xor kan dengan 20 blok plaintext sehingga menghasilkan ciphertext.
```math
Keystream = Ciphertext \oplus Plaintext
```
Nah karena sebelumnya kita tahu bahwa nonce untuk plaintext(msg) digunakan lagi pada plaintext(flag) maka kita cuman perlu cari tahu keystreamnya, tanpa perlu mencari keynya. Karena kita tahu plaintext dari msg dan ct, kita bisa mendapatkan keystream, lalu bisa mendekripkan ct dari flag tersebut.

untuk script lengkap nya bisa di lihat di [solve.py](./solve.py)