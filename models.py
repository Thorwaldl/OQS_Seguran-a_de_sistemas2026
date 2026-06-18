from dataclasses import dataclass


@dataclass
class BenchmarkResult:
    algorithm: str

    iterations: int

    avg_keygen_ms: float
    avg_encap_ms: float
    avg_decap_ms: float

    min_keygen_ms: float
    max_keygen_ms: float

    public_key_size: int
    ciphertext_size: int
    shared_secret_size: int