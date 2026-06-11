import oqs

kemalg = "ML-KEM-768"

print("=== SERVIDOR ===")

# Servidor gera chaves
server = oqs.KeyEncapsulation(kemalg)

public_key = server.generate_keypair()

print("Chave pública gerada!")
print(f"Tamanho da chave pública: {len(public_key)} bytes")


print("\n=== CLIENTE ===")

# Cliente encapsula segredo
client = oqs.KeyEncapsulation(kemalg)

ciphertext, shared_secret_client = client.encap_secret(public_key)

print("Ciphertext gerado!")
print(f"Tamanho ciphertext: {len(ciphertext)} bytes")


print("\n=== SERVIDOR DECAPSULA ===")

# Servidor recupera segredo
shared_secret_server = server.decap_secret(ciphertext)

print("Segredo recuperado!")


print("\n=== VERIFICAÇÃO ===")

print(shared_secret_client == shared_secret_server)

print("\nShared Secret:")
print(shared_secret_client.hex())