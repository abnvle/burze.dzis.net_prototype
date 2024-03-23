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
label.grid(row=1, column=0, columnspan=6)

def load_image(image_url):
    response = requests.get(image_url)
    image_data = response.content
    image = Image.open(BytesIO(image_data))
    image_tk = ImageTk.PhotoImage(image)
    label.configure(image=image_tk)
    label.image = image_tk  # Zachowanie referencji, aby obraz nie został usunięty przez garbage collector

# Funkcje obsługujące zdarzenia kliknięcia przycisków
def load_general_map():
    load_image("https://burze.dzis.net/burze.gif")

def load_nw_map():
    load_image("https://burze.dzis.net/burze_polska_nw.gif")

def load_ne_map():
    load_image("https://burze.dzis.net/burze_polska_ne.gif")

def load_center_map():
    load_image("https://burze.dzis.net/burze_polska_c.gif")

def load_sw_map():
    load_image("https://burze.dzis.net/burze_polska_sw.gif")

def load_se_map():
    load_image("https://burze.dzis.net/burze_polska_se.gif")

# Wybór mapy na podstawie konfiguracji
initial_map_functions = {
    'general': load_general_map,
    'nw': load_nw_map,
    'ne': load_ne_map,
    'center': load_center_map,
    'sw': load_sw_map,
    'se': load_se_map
}

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

# Legenda
legend_frame = tk.Frame(window)
legend_frame.grid(row=2, column=0, columnspan=6, pady=10)

legend_label = tk.Label(legend_frame, text="Liczba minut jaka upłynęła od wyładowania atmosferycznego:")
legend_label.pack()

colors = ["#FF0000", "#FFA500", "#FFFF00", "#00FF00", "#00CED1", "#87CEFA", "#0000FF", "#8A2BE2"]
color_names = ["0-10", "10-25", "25-40", "40-55", "55-70", "70-85", "85-100", "100-115"]

for color, name in zip(colors, color_names):
    legend_square = tk.Label(legend_frame, text=" ", bg=color, padx=5)
    legend_square.pack(side=tk.LEFT)
    legend_name = tk.Label(legend_frame, text=name)
    legend_name.pack(side=tk.LEFT)

# Uruchomienie pętli głównej
window.mainloop()