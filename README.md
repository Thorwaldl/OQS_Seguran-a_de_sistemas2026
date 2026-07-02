# 🔐 Quantum-Safe Cryptography Benchmark

Benchmark de algoritmos de criptografia pós-quântica utilizando **Open Quantum Safe (liboqs-python)**.

Projeto desenvolvido para a disciplina de **Segurança de Sistemas**.

---

## 📖 Sobre o projeto

O objetivo deste projeto é avaliar o desempenho de diferentes algoritmos de criptografia pós-quântica através de benchmarks das operações fundamentais dos **Key Encapsulation Mechanisms (KEMs)**.

Para cada algoritmo são realizadas medições de:

- 🔑 Geração de chaves (KeyGen)
- 📦 Encapsulamento (Encapsulation)
- 🔓 Decapsulamento (Decapsulation)

Os resultados são exportados para um arquivo **CSV**, permitindo análises e comparações entre os algoritmos.

---

## 🚀 Algoritmos avaliados

### ML-KEM
- ML-KEM-512
- ML-KEM-768
- ML-KEM-1024

### Kyber
- Kyber512
- Kyber768
- Kyber1024

### Outros
- sntrup761
- FrodoKEM-640-SHAKE
- FrodoKEM-976-SHAKE

---

## 🛠 Tecnologias utilizadas

- 🐍 Python 3.11
- 🔐 Open Quantum Safe (OQS)
- 📚 liboqs-python
- 🐧 Ubuntu (VM Linux)
- 🪟 Windows 11
- 🌿 Git
- 🐙 GitHub

---

## 📂 Estrutura do projeto

```text
.
├── benchmark.py      # Execução dos benchmarks
├── main.py           # Inicialização dos testes
├── exporter.py       # Exportação dos resultados
├── models.py         # Estruturas de dados
├── timer.py          # Controle de tempo
├── benchmarks/
│   └── benchmark_results.csv
└── README.md
```

---

## ⚙️ Instalação

### Clone o repositório

```bash
git clone https://github.com/Thorwaldl/OQS_Seguran-a_de_sistemas2026.git

cd OQS_Seguran-a_de_sistemas2026
```

### Crie um ambiente virtual

```bash
python3.11 -m venv venv
```

Ative o ambiente:

**Linux**

```bash
source venv/bin/activate
```

**Windows**

```powershell
venv\Scripts\activate
```

---

## 📦 Instale as dependências

Atualize o pip:

```bash
python -m pip install --upgrade pip
```

Instale a biblioteca:

```bash
pip install liboqs-python
```

No Linux também é recomendado instalar:

```bash
sudo apt install build-essential cmake ninja-build git
```

---

## ▶️ Executando o benchmark

```bash
python main.py
```

Ao final da execução será gerado:

```text
benchmarks/benchmark_results.csv
```

---

## 📊 Métricas coletadas

Para cada algoritmo são registrados:

- ⏱ Tempo médio de geração de chaves
- ⚡ Tempo médio de encapsulamento
- 🔓 Tempo médio de decapsulamento
- 📉 Tempo mínimo e máximo de geração de chaves
- 🔑 Tamanho da chave pública
- 📦 Tamanho do ciphertext
- 🤝 Tamanho do segredo compartilhado

---

## 📈 Resultados

Os resultados são exportados automaticamente para um arquivo CSV, permitindo análises estatísticas e comparações entre os algoritmos avaliados.

---

## 🤖 Ferramentas de IA utilizadas

Durante o desenvolvimento deste projeto foram utilizadas ferramentas de IA como apoio:

- 💬 **ChatGPT** — auxílio na configuração do ambiente, depuração de erros e documentação.
- ✨ **Gemini** — apoio na investigação de dependências e problemas de compatibilidade.
- 🎨 **Gamma** — criação do layout da apresentação final.

As ferramentas foram utilizadas como suporte ao desenvolvimento e à documentação do projeto.

---

## 👥 Integrantes

- Emanuelle
- Ulisses

---

## 📄 Licença

Projeto desenvolvido exclusivamente para fins acadêmicos.
