import os

os.environ["hotel_reservation_db"] = "/path/to/your/database.db"
from ui import gui  # Import der GUI-Funktionalität aus gui.py



def main():
    # Starte die Anwendung mit dem Login-Fenster
    gui.login_window()  # Ändere den Startpunkt auf die Login-Funktion


# Überprüfen, ob die Datei direkt ausgeführt wird
if __name__ == "__main__":
    main()