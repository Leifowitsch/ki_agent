import os 
from security import security_test

def write_files(relativer_pfad: str,content: str) -> str:
    """
    Überschreibt die datei die unter dem Pfad angegeben ist mit dem angegebenem Content!


    Args:
        relativer_pfad: Der Pfad einer Datei realtiv zum Projektordner.
        content: Der Inhalt der in die Datei geschrieben werden soll.


    """


    try:

        if os.path.isdir(security_test(relativer_pfad)):
            return 'Relativer Pfad zeigt auf ein Ordner, dieser kann nicht "überschrieben" werden'

        with open(security_test(relativer_pfad), "w", encoding="utf-8") as file_to_write:
            file_to_write.write(content)
    except Exception:
        return f"Datei ist nicht vorhanden oder zugriff ist nicht erlaubt. Datei: {security_test(relativer_pfad)}"
