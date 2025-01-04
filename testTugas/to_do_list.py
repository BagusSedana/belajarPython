import tkinter as tk

# Membuat fungsi untuk menangani input angka dan operasi
def tekan(tombol):
    if tombol == "=":
        try:
            hasil = eval(layar.get())
            layar.delete(0, tk.END)
            layar.insert(tk.END, str(hasil))
        except Exception as e:
            layar.delete(0, tk.END)
            layar.insert(tk.END, "Error")
    elif tombol == "C":
        layar.delete(0, tk.END)
    else:
        layar.insert(tk.END, tombol)

# Membuat jendela utama
root = tk.Tk()
root.title("Kalkulator")

# Membuat widget layar
layar = tk.Entry(root, width=16, font=("Arial", 24), bd=8, insertwidth=2, justify="right")
layar.grid(row=0, column=0, columnspan=4)

# Daftar tombol kalkulator
tombol_list = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

# Membuat tombol kalkulator
baris = 1
kolom = 0
for tombol in tombol_list:
    action = lambda x=tombol: tekan(x)
    tk.Button(root, text=tombol, padx=20, pady=20, font=("Arial", 18), command=action).grid(row=baris, column=kolom)
    kolom += 1
    if kolom > 3:
        kolom = 0
        baris += 1

# Menjalankan jendela utama
root.mainloop()
