from security import security_test
import os


def read_file(relativer_pfad: str) -> str:
    """
    Gibt die genauen Inhalte einer Datei zurück.

    Args:
        relativer_pfad: Der Pfad einer Datei realtiv zum Projektordner
    """

    try:

        if os.path.isdir(security_test(relativer_pfad)):
            return "Relativer Pfad zeigt auf einen Ordner und keine Datei, benutze list_files für den Inhalt!"

        with open(security_test(relativer_pfad), "r", encoding="utf-8") as file_to_read:
            content = file_to_read.read()
        return content
    except Exception:
        return "Dateipfad gibt es nicht oder Zugriff ist nicht erlaubt"