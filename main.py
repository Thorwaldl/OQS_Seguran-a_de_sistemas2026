# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#import oqs
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
#kemalg = "ML-KEM-768"

#server = oqs.KeyEncapsulation(kemalg)
#public_key = server.generate_keypair()

#client = oqs.KeyEncapsulation(kemalg)
#ciphertext, shared_client = client.encap_secret(public_key)

#shared_server = server.decap_secret(ciphertext)

#print(shared_client == shared_server)

#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press F9 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
