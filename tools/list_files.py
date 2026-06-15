import os
from security import security_test


def list_files(relativer_pfad: str) -> str:
    """
    Gibt die Dateien in einem Ordner zurück

    Args:
        relativer_pfad: Der Pfad eines Ordners realtiv zum Projektordner.

    """

    try:

        if not os.path.isdir(security_test(relativer_pfad)):
            return "Zielpfad zeigt auf keinen Ordner"
        
        return ",".join(os.listdir(security_test(relativer_pfad)))
    except Exception:
        return f"Es ist ein fehler bei der Auslesung des Ordners: {security_test(relativer_pfad)} passiert"