import tkinter as tk
from tkinter import messagebox


def start_gui():
    # Fenster erstellen
    root = tk.Tk()
    root.title("Hotelreservierungssystem")
    root.geometry("400x300")

    # Begrüßungstext hinzufügen
    label = tk.Label(root, text="Willkommen im Hotelreservierungssystem!", font=("Arial", 12))
    label.pack(pady=10)

    # Button mit Aktion hinzufügen
    def on_button_click():
        messagebox.showinfo("Aktion", "Reservierung gestartet!")

    button = tk.Button(root, text="Reservierung starten", command=on_button_click)
    button.pack(pady=10)

    # Event-Loop starten
    root.mainloop()


# Überprüfen, ob die Datei direkt ausgeführt wird
if __name__ == "__main__":
    start_gui()