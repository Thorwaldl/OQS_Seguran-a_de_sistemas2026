# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import oqs
import time

kemalg = "ML-KEM-768"

# KeyGen
inicio = time.perf_counter()

server = oqs.KeyEncapsulation(kemalg)
public_key = server.generate_keypair()

fim = time.perf_counter()

tempo_keygen = (fim - inicio) * 1000


# Encapsulation
client = oqs.KeyEncapsulation(kemalg)

inicio = time.perf_counter()

ciphertext, shared_secret_client = client.encap_secret(public_key)

fim = time.perf_counter()

tempo_encap = (fim - inicio) * 1000


# Decapsulation
inicio = time.perf_counter()

shared_secret_server = server.decap_secret(ciphertext)

fim = time.perf_counter()

tempo_decap = (fim - inicio) * 1000


print(f"Algoritmo: {kemalg}")
print(f"KeyGen: {tempo_keygen:.3f} ms")
print(f"Encapsulation: {tempo_encap:.3f} ms")
print(f"Decapsulation: {tempo_decap:.3f} ms")
print(f"Public Key: {len(public_key)} bytes")
print(f"Ciphertext: {len(ciphertext)} bytes")
print(f"Shared Secret: {len(shared_secret_client)} bytes")