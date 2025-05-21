import tkinter as tk
from tkinter import messagebox, ttk

from business_logic.hotel_manager import HotelManager
hotel_manager = HotelManager()

# Benutzer-Datenbank mit Benutzerrollen (Admin/Benutzer)
USERS = {
    "admin": {"password": "admin", "role": "admin"},
    "user": {"password": "user", "role": "user"}
}


def authenticate(username: str, password: str):
    user = USERS.get(username)
    if user and user["password"] == password:
        return user["role"]
    return None


def logout_and_return_to_login(current_window):
    current_window.destroy()  # Schließt das aktuelle Fenster
    login_window()  # Öffnet das Login-Fenster erneut


### Benutzer-Dashboard
def open_user_dashboard():
    root = tk.Tk()
    root.title("Hotelreservierungssystem - Benutzer")
    root.geometry("800x600")

    # Begrüßungstext
    label = tk.Label(root, text="Wilkommen im Hotelreservierungssystem der Gruppe B2!", font=("Arial", 18))
    label.pack(pady=10)

    # Suchfelder
    search_frame = tk.Frame(root)
    search_frame.pack(pady=10, padx=20, anchor="w")

    # Stadtfeld
    city_label = tk.Label(search_frame, text="Stadt:", font=("Arial", 12))
    city_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    city_entry = tk.Entry(search_frame, width=20)
    city_entry.grid(row=0, column=1, padx=5, pady=5)

    # Hotelnamefeld
    hotel_name_label = tk.Label(search_frame, text="Hotelname:", font=("Arial", 12))
    hotel_name_label.grid(row=0, column=4, padx=5, pady=5, sticky="w")
    hotel_name_entry = tk.Entry(search_frame, width=20)
    hotel_name_entry.grid(row=0, column=5, padx=5, pady=5)

    # Sterneauswahl
    stars_label = tk.Label(search_frame, text="Sterne (1-5):", font=("Arial", 12))
    stars_label.grid(row=0, column=2, padx=5, pady=5, sticky="w")
    selected_stars = tk.StringVar(value="Alle")
    stars_options = ["Alle", "1", "2", "3", "4", "5"]
    stars_dropdown = ttk.Combobox(search_frame, textvariable=selected_stars, values=stars_options, state="readonly", width=10)
    stars_dropdown.grid(row=0, column=3, padx=5, pady=5)

    # Suchergebnisse
    results_frame = tk.Frame(root)
    results_frame.pack(pady=10, padx=20)

    results_label = tk.Label(results_frame, text="Suchergebnisse:", font=("Arial", 14))
    results_label.pack(anchor="w")

    columns = ("Name", "Stadt", "Sterne", "Adresse", "Postleitzahl", "Land", "Zimmeranzahl")
    tree = ttk.Treeview(results_frame, columns=columns, show="headings", height=10)
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)
    tree.pack(pady=10)

    # Hotelsuche
    def search_hotels():
        # Stadt, Hotelname und Sterne aus den Suchfeldern abrufen
        city = city_entry.get()
        hotel_name = hotel_name_entry.get()
        stars = selected_stars.get()

        try:
            if city:
                results = hotel_manager.search_hotels_by_city(city)
            elif hotel_name:
                results = hotel_manager.search_hotels_by_name(hotel_name)
            elif stars and stars != "Alle":
                results = hotel_manager.search_hotels_by_stars(int(stars))
            else:
                messagebox.showwarning("Suche", "Bitte mindestens ein Kriterium eingeben!")
                return

            tree.delete(*tree.get_children())
            for hotel in results:
                tree.insert("", tk.END, values=(
                    hotel.hotel_name,
                    hotel.city,
                    hotel.stars,
                    hotel.street,
                    hotel.zip_code,
                    hotel.country,
                    hotel.rooms
                ))
                return f"{hotel.hotel_name}, {hotel.city}, {hotel.stars}, {hotel.street}, {hotel.zip_code}, {hotel.country}, {hotel.rooms}"

        except Exception as e:
            messagebox.showerror("Fehler", f"Fehler bei der Suche: {e}")

    # Suchbutton
    search_button = tk.Button(root, text="Hotels durchsuchen", command=search_hotels)
    search_button.pack(pady=10)

    # Logout-Button
    logout_button = tk.Button(root, text="Logout", command=lambda: logout_and_return_to_login(root))
    logout_button.pack(pady=10)

    root.mainloop()


### Admin-Dashboard: Daten verwalten und pflegen ###
def open_admin_dashboard():
    root = tk.Tk()
    root.title("Admin Dashboard - Hotelverwaltung")
    root.geometry("800x600")

    tk.Label(root, text="Admin Dashboard - Hotelverwaltung", font=("Arial", 18)).pack(pady=10)

    # Button zum erstellen eines neues Hotels
    tk.Button(root, text="Neues Hotel erstellen", command=lambda: create_hotel_form(root)).pack(pady=5)

    # Button zum Bearbeiten eines Hotels
    tk.Button(root, text="Hotel bearbeiten", command=lambda: update_hotel_form(root)).pack(pady=5)

    # Logout-Button
    logout_button = tk.Button(root, text="Logout", command=lambda: logout_and_return_to_login(root))
    logout_button.pack(pady=10)


def search_hotels_by_city(root):
    def perform_search():
        try:
            search_text = search_var.get().strip()
            if not search_text:
                raise ValueError("Bitte geben Sie einen Suchbegriff (Name oder Teil des Namens) ein!")

            # Ruft die Suchergebnisse aus dem Hotel Manager ab
            hotels = hotel_manager.search_hotels_by_city(search_text)

            # Ergebnisse in der Listbox aktualisieren
            result_listbox.delete(0, tk.END)  # Löscht die vorherigen Einträge
            if not hotels:
                result_listbox.insert(tk.END, "Keine Ergebnisse gefunden.")
                return

            # Ergebnisse mit Hotel-ID anzeigen
            for hotel in hotels:
                result_listbox.insert(
                    tk.END,
                    f"ID: {hotel.hotelid}, Name: {hotel.hotel_name}, Stadt: {hotel.city}, Sterne: {hotel.stars}"
                )

        except ValueError as v_err:
            messagebox.showerror("Eingabefehler", str(v_err))
        except Exception as e:
            messagebox.showerror("Fehler", f"Ein unerwarteter Fehler ist aufgetreten: {e}")

    # Fenster für die Hotelsuche öffnen
    search_window = tk.Toplevel(root)
    search_window.title("Hotelsuche (Admin)")

    # Eingabefeld für Suchtext erstellen
    tk.Label(search_window, text="Suchen Sie nach Hotelname:").pack(pady=5)
    search_var = tk.StringVar()
    tk.Entry(search_window, textvariable=search_var, width=50).pack(pady=5)

    # Such-Button hinzufügen
    tk.Button(search_window, text="Suchen", command=perform_search).pack(pady=5)

    # Listbox für die Darstellung der Ergebnisse
    result_listbox = tk.Listbox(search_window, width=80, height=20)
    result_listbox.pack(pady=10)

    # Button zum Schließen des Fensters
    tk.Button(search_window, text="Schließen", command=search_window.destroy).pack(pady=5)

def create_hotel_form(root):

    def save_hotel():
        hotel_name = hotel_name_var.get()
        street = street_var.get()
        city = city_var.get()
        zip_code = zip_code_var.get()
        country = country_var.get()
        stars = stars_var.get()
        number_of_rooms = number_of_rooms_var.get()

        try:
            # Validierung und Konvertierung der Eingaben
            if not hotel_name or not street or not city or not country or not zip_code or not stars or not number_of_rooms:
                raise ValueError("Alle Felder müssen ausgefüllt sein.")
            try:
                zip_code = int(zip_code)
                stars = int(stars)
                number_of_rooms = int(number_of_rooms)
            except ValueError:
                raise ValueError("PLZ, Sterne und Zimmeranzahl müssen korrekt definiert sein")

            if stars < 1 or stars > 5:
                raise ValueError("Die Sterne müssen zwischen 1 und 5 liegen.")
            if zip_code <= 0 or number_of_rooms <= 0:
                raise ValueError("PLZ und Zimmeranzahl müssen positive Zahlen sein.")

            # Hotel mit dem HotelManager erstellen
            new_hotel = hotel_manager.create_hotel(
                hotel_name=hotel_name,
                street=street,
                city=city,
                zip_code=zip_code,
                country=country,
                stars=stars,
                number_of_rooms=number_of_rooms,
            )
            messagebox.showinfo("Erfolg", f"Hotel '{new_hotel.hotel_name}' wurde erfolgreich erstellt!")
            form_window.destroy()
        except ValueError as v_err:
            messagebox.showerror("Validierungsfehler", str(v_err))
        except Exception as e:
            messagebox.showerror("Fehler", f"Fehler beim Erstellen des Hotels: {e}")

    # Erstelle das Formularfenster
    form_window = tk.Toplevel(root)
    form_window.title("Neues Hotel erstellen")

    # Eingabefelder und Labels
    tk.Label(form_window, text="Hotelname:").pack()
    hotel_name_var = tk.StringVar()
    tk.Entry(form_window, textvariable=hotel_name_var).pack()

    tk.Label(form_window, text="Straße:").pack()
    street_var = tk.StringVar()
    tk.Entry(form_window, textvariable=street_var).pack()

    tk.Label(form_window, text="Stadt:").pack()
    city_var = tk.StringVar()
    tk.Entry(form_window, textvariable=city_var).pack()

    tk.Label(form_window, text="Postleitzahl:").pack()
    zip_code_var = tk.StringVar()
    tk.Entry(form_window, textvariable=zip_code_var).pack()

    tk.Label(form_window, text="Land:").pack()
    country_var = tk.StringVar()
    tk.Entry(form_window, textvariable=country_var).pack()

    tk.Label(form_window, text="Sterne (1-5):").pack()
    stars_var = tk.StringVar()
    tk.Entry(form_window, textvariable=stars_var).pack()

    tk.Label(form_window, text="Zimmeranzahl:").pack()
    number_of_rooms_var = tk.StringVar()
    tk.Entry(form_window, textvariable=number_of_rooms_var).pack()

    # Speichern-Button
    tk.Button(form_window, text="Hotel speichern", command=save_hotel).pack()

def update_hotel_form(root):
    pass

    # Admin-Dashboard-Loop
    root.mainloop()

### Login-Fenster ###
def login_window():

    def attempt_login():
        username = username_entry.get()
        password = password_entry.get()

        role = authenticate(username, password)
        if role == "admin":
            messagebox.showinfo("Erfolg", "Willkommen Admin!")
            login.destroy()
            open_admin_dashboard()
        elif role == "user":
            messagebox.showinfo("Erfolg", "Willkommen Benutzer!")
            login.destroy()
            open_user_dashboard()
        else:
            messagebox.showerror("Fehler", "Ungültiger Benutzername oder Passwort!")

    login = tk.Tk()
    login.title("Login")
    login.geometry("300x200")

    tk.Label(login, text="Benutzername:").pack(pady=5)
    username_entry = tk.Entry(login)
    username_entry.pack(pady=5)

    tk.Label(login, text="Passwort:").pack(pady=5)
    password_entry = tk.Entry(login, show="*")
    password_entry.pack(pady=5)

    tk.Button(login, text="Login", command=attempt_login).pack(pady=10)

    login.mainloop()


# Hauptaufruf
if __name__ == "__main__":
    login_window()