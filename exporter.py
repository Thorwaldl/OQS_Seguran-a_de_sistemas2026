import csv


class CsvExporter:

    @staticmethod
    def export(results, file_name):

        with open(
            file_name,
            "w",
            newline="",
            encoding="utf-8"
        ) as csvfile:

            writer = csv.writer(csvfile)

            writer.writerow([
                "Algorithm",
                "Iterations",
                "Avg KeyGen",
                "Avg Encap",
                "Avg Decap",
                "Min KeyGen",
                "Max KeyGen",
                "Public Key",
                "Ciphertext",
                "Shared Secret"
            ])

            for r in results:

                writer.writerow([
                    r.algorithm,
                    r.iterations,
                    r.avg_keygen_ms,
                    r.avg_encap_ms,
                    r.avg_decap_ms,
                    r.min_keygen_ms,
                    r.max_keygen_ms,
                    r.public_key_size,
                    r.ciphertext_size,
                    r.shared_secret_size
                ])