import statistics
import time

import oqs

from models import BenchmarkResult


class KEMBenchmark:

    def __init__(self, iterations=100):
        self.iterations = iterations

    def execute(self, algorithm):

        keygen_times = []
        encap_times = []
        decap_times = []

        public_key_size = 0
        ciphertext_size = 0
        shared_secret_size = 0

        for _ in range(self.iterations):

            # KEYGEN
            start = time.perf_counter()

            server = oqs.KeyEncapsulation(algorithm)
            public_key = server.generate_keypair()

            end = time.perf_counter()

            keygen_times.append(
                (end - start) * 1000
            )

            # ENCAP
            client = oqs.KeyEncapsulation(algorithm)

            start = time.perf_counter()

            ciphertext, shared_client = \
                client.encap_secret(public_key)

            end = time.perf_counter()

            encap_times.append(
                (end - start) * 1000
            )

            # DECAP
            start = time.perf_counter()

            shared_server = \
                server.decap_secret(ciphertext)

            end = time.perf_counter()

            decap_times.append(
                (end - start) * 1000
            )

            if shared_client != shared_server:
                raise Exception(
                    f"Handshake falhou para {algorithm}"
                )

            public_key_size = len(public_key)
            ciphertext_size = len(ciphertext)
            shared_secret_size = len(shared_client)

        return BenchmarkResult(
            algorithm=algorithm,
            iterations=self.iterations,

            avg_keygen_ms=statistics.mean(keygen_times),
            avg_encap_ms=statistics.mean(encap_times),
            avg_decap_ms=statistics.mean(decap_times),

            min_keygen_ms=min(keygen_times),
            max_keygen_ms=max(keygen_times),

            public_key_size=public_key_size,
            ciphertext_size=ciphertext_size,
            shared_secret_size=shared_secret_size
        )