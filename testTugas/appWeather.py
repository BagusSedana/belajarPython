import tkinter as tk
import requests
from tkinter import messagebox

def get_weather():
    city = ent_city.get()
    api_key = "c363dd130c03d548b6b74481d6f0cf11"  # API key Anda
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    # URL lengkap
    complete_url = base_url + "q=" + city + "&appid=" + api_key + "&units=metric"
    
    try:
        # Permintaan HTTP ke API
        response = requests.get(complete_url)
        data = response.json()
        
        if data.get("cod") == 200:
            main = data.get("main")
            weather = data.get("weather")
            
            if main and weather:
                temp = main.get("temp", "N/A")
                pressure = main.get("pressure", "N/A")
                humidity = main.get("humidity", "N/A")
                weather_desc = weather[0].get("description", "N/A")
                
                # Menampilkan hasil di GUI
                lbl_result.config(text=f"Cuaca di {city}:\n"
                                       f"Suhu: {temp}°C\n"
                                       f"Tekanan: {pressure} hPa\n"
                                       f"Kelembaban: {humidity}%\n"
                                       f"Deskripsi: {weather_desc.capitalize()}")
            else:
                messagebox.showerror("Error", "Data cuaca tidak lengkap!")
        else:
            messagebox.showerror("Error", f"Kota tidak ditemukan! (Kode: {data.get('cod')})")
    
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Permintaan gagal: {e}")

# Membuat jendela utama
root = tk.Tk()
root.title("Weather App")

# Menambahkan widget
lbl_city = tk.Label(root, text="Masukkan nama kota:", font=("Arial", 14))
lbl_city.pack(pady=10)

ent_city = tk.Entry(root, width=30, font=("Arial", 14))
ent_city.pack(pady=5)

btn_get_weather = tk.Button(root, text="Dapatkan Cuaca", command=get_weather, font=("Arial", 14))
btn_get_weather.pack(pady=10)

lbl_result = tk.Label(root, text="", font=("Arial", 14))
lbl_result.pack(pady=20)

# Menjalankan jendela utama
root.mainloop()
