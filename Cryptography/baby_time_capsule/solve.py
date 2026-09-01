from Crypto.Util.number import bytes_to_long, long_to_bytes
from functools import reduce
from gmpy2 import iroot, mpz
from json import loads
from math import gcd
from pwn import *

HOST = '154.57.164.73'
PORT = 30976

def hastad_broadcast_attack(pairs, e=5):
    """
    Håstad's Broadcast Attack.
 
    pairs: list of (n, ct) tuples -- same plaintext m, same e,
           but different (pairwise-coprime) moduli n. Need >= e pairs.
    e:     public exponent (default 5)
 
    Returns: bytes -- the recovered plaintext.
    """
    if len(pairs) < e:
        raise ValueError(f"Need at least {e} (n, ct) pairs, got {len(pairs)}")
 
    # sanity check: moduli must be pairwise coprime
    moduli = [n for n, _ in pairs]
    for i in range(len(moduli)):
        for j in range(i + 1, len(moduli)):
            if gcd(moduli[i], moduli[j]) != 1:
                raise ValueError(f"Moduli at index {i} and {j} are not coprime")
 
    # --- CRT combine: recover m^e mod (n1*n2*...*ne) ---
    N = reduce(lambda a, b: a * b, moduli)
    total = 0
    for n_i, ct_i in pairs:
        N_i = N // n_i
        inv = pow(N_i, -1, n_i)
        total += ct_i * inv * N_i
    m_pow_e = total % N
 
    # --- integer e-th root (works because m^e < N, no modular wraparound) ---
    root, exact = iroot(mpz(m_pow_e), e)
    if not exact:
        raise ValueError(
            "CRT result is not a perfect e-th root. Either fewer than e "
            "moduli were used, or m^e >= product(n_i)."
        )
 
    return long_to_bytes(int(root))

conn = remote(HOST, PORT)

pairs, e = [], 0

for _ in range(5):
    conn.sendline(b'Y')

    data_respond = conn.recvline().decode()
    dict_data = loads(data_respond[data_respond.index('{'):data_respond.index('}') + 1])

    ct = int(dict_data["time_capsule"], 16)
    n, e = int(dict_data["pubkey"][0], 16), int(dict_data["pubkey"][1], 16)

    pairs.append([n, ct])

print(hastad_broadcast_attack(pairs, e))