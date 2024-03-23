import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import configparser

# Utworzenie okna
window = tk.Tk()
window.title("burze.dzis.net")

# Wczytanie konfiguracji
config = configparser.ConfigParser()
config.read('config.ini')
initial_map = config.get('DEFAULT', 'initial_map')

# Funkcja do obsługi zdarzenia kliknięcia przycisku
label = tk.Label(window)
label.grid(row=1, column=0, columnspan=7)

# Legenda
legend_frame = tk.Frame(window)

legend_label = tk.Label(legend_frame, text="Liczba minut jaka upłynęła od wyładowania atmosferycznego:")
legend_label.pack()

colors = ["#FF0000", "#FFA500", "#FFFF00", "#00FF00", "#00CED1", "#87CEFA", "#0000FF", "#8A2BE2"]
color_names = ["0-10", "10-25", "25-40", "40-55", "55-70", "70-85", "85-100", "100-115"]

for color, name in zip(colors, color_names):
    legend_square = tk.Label(legend_frame, text=" ", bg=color, padx=5)
    legend_square.pack(side=tk.LEFT)
    legend_name = tk.Label(legend_frame, text=name)
    legend_name.pack(side=tk.LEFT)

# Objasnienie skali ostrzeżeń
warning_explanation_frame = tk.Frame(window)

# Utworzenie przycisku objaśnienia skali ostrzeżeń
warning_explanation_button = tk.Button(warning_explanation_frame, text="Objaśnienie skali ostrzeżeń")

# Funkcja do obsługi zdarzenia kliknięcia przycisku
def load_image(image_url):
    response = requests.get(image_url)
    image_data = response.content
    image = Image.open(BytesIO(image_data))
    image_tk = ImageTk.PhotoImage(image)
    label.configure(image=image_tk)
    label.image = image_tk

# Funkcje obsługujące zdarzenia kliknięcia przycisków
def load_general_map():
    load_image("https://burze.dzis.net/burze.gif")
    show_legend()
    hide_warning_explanation_button()

def load_nw_map():
    load_image("https://burze.dzis.net/burze_polska_nw.gif")
    show_legend()
    hide_warning_explanation_button()

def load_ne_map():
    load_image("https://burze.dzis.net/burze_polska_ne.gif")
    show_legend()
    hide_warning_explanation_button()

def load_center_map():
    load_image("https://burze.dzis.net/burze_polska_c.gif")
    show_legend()
    hide_warning_explanation_button()

def load_sw_map():
    load_image("https://burze.dzis.net/burze_polska_sw.gif")
    show_legend()
    hide_warning_explanation_button()

def load_se_map():
    load_image("https://burze.dzis.net/burze_polska_se.gif")
    show_legend()
    hide_warning_explanation_button()

def load_warnings_map():
    load_image("https://burze.dzis.net/zagrozenia.gif")
    hide_legend()
    show_warning_explanation_button()

def show_image_window():
    image_window = tk.Toplevel(window)
    image_window.title("Objaśnienie skali ostrzeżeń")
    img = Image.open("img/objasnienie.png")
    img_tk = ImageTk.PhotoImage(img)
    image_label = tk.Label(image_window, image=img_tk)
    image_label.image = img_tk
    image_label.pack()

# Wybór mapy na podstawie konfiguracji
initial_map_functions = {
    'general': load_general_map,
    'nw': load_nw_map,
    'ne': load_ne_map,
    'center': load_center_map,
    'sw': load_sw_map,
    'se': load_se_map,
    'warnings': load_warnings_map  # Dodanie mapy ostrzeżeń
}

def show_legend():
    legend_frame.grid(row=2, column=0, columnspan=7)

def hide_legend():
    legend_frame.grid_forget()

def show_warning_explanation_button():
    warning_explanation_frame.grid(row=3, column=0, columnspan=7)
    warning_explanation_button.config(command=show_image_window)
    warning_explanation_button.pack()

def hide_warning_explanation_button():
    warning_explanation_frame.grid_forget()

if initial_map in initial_map_functions:
    initial_map_functions[initial_map]()

# Tworzenie przycisków
button_general = tk.Button(window, text="Mapa ogólna", command=load_general_map)
button_general.grid(row=0, column=0, padx=5, pady=5)

button_nw = tk.Button(window, text="Północny-Zachód", command=load_nw_map)
button_nw.grid(row=0, column=1, padx=5, pady=5)

button_ne = tk.Button(window, text="Północny-Wschód", command=load_ne_map)
button_ne.grid(row=0, column=2, padx=5, pady=5)

button_center = tk.Button(window, text="Centrum", command=load_center_map)
button_center.grid(row=0, column=3, padx=5, pady=5)

button_sw = tk.Button(window, text="Południowy-Zachód", command=load_sw_map)
button_sw.grid(row=0, column=4, padx=5, pady=5)

button_se = tk.Button(window, text="Południowy-Wschód", command=load_se_map)
button_se.grid(row=0, column=5, padx=5, pady=5)

# Dodanie przycisku "Mapa ostrzeżeń"
button_warnings = tk.Button(window, text="Mapa ostrzeżeń", command=load_warnings_map)
button_warnings.grid(row=0, column=6, padx=5, pady=5)

# Uruchomienie pętli głównej
window.mainloop()
