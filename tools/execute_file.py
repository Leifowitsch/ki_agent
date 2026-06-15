import os
import sys
import subprocess
from security import security_test

def execute_file(relativer_pfad: str) -> str:
    """
    Führt die Datei des realtiven Pfades aus!

    Args:
        relativer_pfad: Der Pfad einer Datei realtiv zum Projektordner.

    """

    try:

        if os.path.isdir(security_test(relativer_pfad)):
            return f'Datei "{security_test(relativer_pfad)}" ist ein Ordner und kann nicht ausgeführt werden. Zum anzeigen der Inhalte benutz list_files'
        
        result = subprocess.run(
            [sys.executable, security_test(relativer_pfad)],
            capture_output=True
            text=True
            timeout=5
        )

        if result.returncode == 0:
            return f"Ausführung der Datei war Erfolgreich, Konsolenausgabe: \n{result.stdout}"
        else:
            return f"Ausführung fehlgeschlagen! Fehlermeldung: \n{result.stderr}"
        
    except subprocess.TimeoutExpired:
        return "Fehler: Die Ausführung wurde wegen einees Timouts abegbrochen nach 5 sek um eine mögliche Endlosschleife zu verhindern"
    
    except Exception as e:
        return f"Fehler bei der Ausführung: {e}"
