from benchmark import KEMBenchmark
from exporter import CsvExporter


algorithms = [

    "ML-KEM-512",
    "ML-KEM-768",
    "ML-KEM-1024",

    "Kyber512",
    "Kyber768",
    "Kyber1024",

    "sntrup761",

    "FrodoKEM-640-SHAKE",
    "FrodoKEM-976-SHAKE"
]

benchmark = KEMBenchmark(
    iterations=100
)

results = []

for algorithm in algorithms:

    print(f"\nExecutando {algorithm}")

    try:

        result = benchmark.execute(
            algorithm
        )

        results.append(result)

        print(
            f"KeyGen: {result.avg_keygen_ms:.3f} ms"
        )

        print(
            f"Encap: {result.avg_encap_ms:.3f} ms"
        )

        print(
            f"Decap: {result.avg_decap_ms:.3f} ms"
        )

    except Exception as ex:

        print(
            f"Erro em {algorithm}: {ex}"
        )

CsvExporter.export(
    results,
    "benchmarks/benchmark_results.csv"
)

print("\nBenchmark concluído.")