import os

def security_test(relativer_pfad: str, pflicht_pfad: str | None = None):
    if pflicht_pfad is None:
        pflicht_pfad = os.environ.get("PFLICHT_PFAD")
        
    echter_pfad = os.path.abspath(relativer_pfad)
    gleicher_pfad = os.path.commonpath([echter_pfad, pflicht_pfad])
    sicher = gleicher_pfad == pflicht_pfad
    if sicher:
        return echter_pfad
    else:
        raise PermissionError("Zugriff außerhalb der erlaubten Ordner-Struktur")
