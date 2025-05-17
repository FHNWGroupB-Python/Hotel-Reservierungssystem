import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from business_logic import hotel_manager

def start_gui():
    # Fenster erstellen
    root = tk.Tk()
    root.title("Hotelreservierungssystem")
    root.geometry("600x400")

    # Begrüßungstext hinzufügen
    label = tk.Label(root, text="Willkommen im Hotelreservierungssystem der Gruppe B2!", font=("Arial", 18))
    label.pack(pady=10)

    # Suchfeld erstellen
    search_frame = tk.Frame(root)
    search_frame.pack(pady=10, padx=20, anchor="w")

    #Feld für Stadtsuche
    city_label = tk.Label(search_frame, text="Stadt:", font=("Arial", 12))
    city_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    city_entry = tk.Entry(search_frame, width=20)
    city_entry.grid(row=0, column=1, padx=5, pady=5)

    # Sterneauswahl Dropdown
    stars_label = tk.Label(search_frame, text="Sterne (1-5):", font=("Arial", 12))
    stars_label.grid(row=0, column=2, padx=5, pady=5, sticky="w")
    selected_stars = tk.StringVar(value="Alle")
    stars_options = ["Alle", "1", "2", "3", "4", "5"]
    stars_dropdown = ttk.Combobox(search_frame, textvariable=selected_stars, values=stars_options, state="readonly", width=10)
    stars_dropdown.grid(row=0, column=3, padx=5, pady=5)

    # Suchergebnisse hinzufügen (Treeview)
    results_frame = tk.Frame(root)
    results_frame.pack(pady=10, padx=20)

    results_label = tk.Label(results_frame, text="Suchergebnisse:", font=("Arial", 14))
    results_label.pack(anchor="w")

    columns = ("Name", "Stadt", "Sterne", "Adresse")
    tree = ttk.Treeview(results_frame, columns=columns, show="headings", height=10)
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)
    tree.pack(pady=10)

    # Funktion, um Hotels zu suchen
    def search_hotels():
        city = city_entry.get()
        stars = selected_stars.get()

        try:
            if city:
                results = hotel_manager.search_hotels_by_city(city)
            elif stars and stars != "Alle":
                results = hotel_manager.search_hotels_by_stars(int(stars))
            else:
                messagebox.showwarning("Suche", "Bitte mindestens ein Kriterium eingeben!")
                return

            # Update der Ergebnisse in der Treeview
            tree.delete(*tree.get_children())
            for hotel in results:
                tree.insert("", tk.END, values=(
                    hotel.hotel_name,
                    hotel.city,
                    hotel.stars,
                    f"{hotel.street}, {hotel.zip_code}, {hotel.country}"
                ))

        except Exception as e:
            messagebox.showerror("Fehler", f"Fehler bei der Suche: {e}")

    # Suchbutton hinzufügen
    search_button = tk.Button(root, text="Hotels durchsuchen", command=search_hotels)
    search_button.pack(pady=10)

    # Event-Loop starten
    root.mainloop()


# Überprüfen, ob die Datei direkt ausgeführt wird
if __name__ == "__main__":
    start_gui()