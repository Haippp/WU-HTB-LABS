# The Last Dance
![](https://img.shields.io/badge/challange_by-HackTheBox-green) ![](https://img.shields.io/badge/difficulty-VeryEasy-blue)

## 📝Deskripsi Challange
••••

(no desc just [server.py](./server.py))

## 🔍Analisa
Ada hal yang janggal di codingan yang menyalahi standar penggunaan RSA.

1. E nya sangat kecil yaitu 5
```python
    def __init__(self, msg):
        self.msg = msg
        self.bit_size = 1024
        self.e = 5
```
2. Kemudian kita bisa meminta banyak hasil enkripsi dengan moudlus n yang beda beda tiap kali mengirimkan 'Y'.
```python
def challenge(req):
    time_capsule = TimeCapsule(FLAG)
    while True:
        try:
            req.sendall(
                b'Welcome to Qubit Enterprises. Would you like your own time capsule? (Y/n) '
            )
            msg = req.recv(4096).decode().strip().upper()
            if msg == 'Y' or msg == 'YES':
                capsule = time_capsule.get_new_time_capsule()
                req.sendall(json.dumps(capsule).encode() + b'\n')
            elif msg == 'N' or msg == "NO":
                req.sendall(b'Thank you, take care\n')
                break
            else:
                req.sendall(b'I\'m sorry I don\'t understand\n')
        except:
            # Socket closed, bail
            return

```

Nah dari dua analisa tersebut itu mengarahkan pada pola yang bisa di eksploitasi dengan serangan _hastad broadcast attack_.

## 🧩Penyelesaian
Untuk menyelesaikan challange ini kita perlu mendapatkan 5 buah pasangan n, dan ct yang berbeda beda agar bisa membalikkannya. maka dari itu kita perlu membuat sistem solve dengan algoritma seperti ini:
1. Sistem mengirimkan Y selama 5x agar bisa mendapatkan pasangan ct, dan n yang berbeda-beda
2. Setelah mendapatkan nilai tersebut kemudian kita gunakan fungsi _hastad broadcast attack_

Hasil dari algoritma tersebut bisa kalian baca di [solve.py](./solve.py)