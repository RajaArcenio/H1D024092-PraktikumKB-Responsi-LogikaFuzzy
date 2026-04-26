import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import tkinter as tk
from tkinter import ttk, messagebox

class FuzzyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Smart Inventory Optimizer v3.0")
        self.geometry("700x820")
        self.configure(bg="#ffffff")

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.stok_val = tk.DoubleVar(value=50)
        self.ems_val = tk.DoubleVar(value=30) 
        self.speed_val = tk.DoubleVar(value=50) 
        self.diskon_hasil = "0.0"

        self.setup_fuzzy_logic()

        self.frames = {}
        for F in (WelcomePage, InputPage, OutputPage):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("WelcomePage")

    def setup_fuzzy_logic(self):
        self.stok = ctrl.Antecedent(np.arange(0, 101, 1), 'stok')
        self.ems = ctrl.Antecedent(np.arange(0, 731, 1), 'ems')
        self.speed = ctrl.Antecedent(np.arange(0, 101, 1), 'speed')
        self.diskon = ctrl.Consequent(np.arange(0, 51, 1), 'diskon')

        self.stok['Sedikit'] = fuzz.trimf(self.stok.universe, [0, 0, 40])
        self.stok['Sedang'] = fuzz.trimf(self.stok.universe, [20, 50, 80])
        self.stok['Banyak'] = fuzz.trimf(self.stok.universe, [60, 100, 100])
        
        self.ems['Kritis'] = fuzz.trapmf(self.ems.universe, [0, 30, 30, 75])
        self.ems['Aman'] = fuzz.trimf(self.ems.universe, [60, 120, 180])
        self.ems['Lama'] = fuzz.trapmf(self.ems.universe, [150, 300, 730, 730])

        self.speed['Lambat'] = fuzz.trimf(self.speed.universe, [0, 0, 25])
        self.speed['Normal'] = fuzz.trimf(self.speed.universe, [20, 50, 80])
        self.speed['Cepat'] = fuzz.trimf(self.speed.universe, [60, 100, 100])

        self.diskon['Sedikit'] = fuzz.trimf(self.diskon.universe, [0, 0, 20])
        self.diskon['Sedang'] = fuzz.trimf(self.diskon.universe, [10, 25, 40])
        self.diskon['Besar'] = fuzz.trimf(self.diskon.universe, [30, 50, 50])

        r1 = ctrl.Rule(self.stok['Sedikit'] & self.ems['Kritis'] & self.speed['Lambat'], self.diskon['Sedang'])
        r2 = ctrl.Rule(self.stok['Sedikit'] & self.ems['Kritis'] & self.speed['Normal'], self.diskon['Sedang'])
        r3 = ctrl.Rule(self.stok['Sedikit'] & self.ems['Kritis'] & self.speed['Cepat'], self.diskon['Sedikit'])
        r4 = ctrl.Rule(self.stok['Sedikit'] & self.ems['Aman'] & self.speed['Lambat'], self.diskon['Sedang'])
        r5 = ctrl.Rule(self.stok['Sedikit'] & self.ems['Aman'] & self.speed['Normal'], self.diskon['Sedikit'])
        r6 = ctrl.Rule(self.stok['Sedikit'] & self.ems['Aman'] & self.speed['Cepat'], self.diskon['Sedikit'])
        r7 = ctrl.Rule(self.stok['Sedikit'] & self.ems['Lama'] & self.speed['Lambat'], self.diskon['Sedikit'])
        r8 = ctrl.Rule(self.stok['Sedikit'] & self.ems['Lama'] & self.speed['Normal'], self.diskon['Sedikit'])
        r9 = ctrl.Rule(self.stok['Sedikit'] & self.ems['Lama'] & self.speed['Cepat'], self.diskon['Sedikit'])

        r10 = ctrl.Rule(self.stok['Sedang'] & self.ems['Kritis'] & self.speed['Lambat'], self.diskon['Besar'])
        r11 = ctrl.Rule(self.stok['Sedang'] & self.ems['Kritis'] & self.speed['Normal'], self.diskon['Besar'])
        r12 = ctrl.Rule(self.stok['Sedang'] & self.ems['Kritis'] & self.speed['Cepat'], self.diskon['Sedang'])
        r13 = ctrl.Rule(self.stok['Sedang'] & self.ems['Aman'] & self.speed['Lambat'], self.diskon['Sedang'])
        r14 = ctrl.Rule(self.stok['Sedang'] & self.ems['Aman'] & self.speed['Normal'], self.diskon['Sedang'])
        r15 = ctrl.Rule(self.stok['Sedang'] & self.ems['Aman'] & self.speed['Cepat'], self.diskon['Sedikit'])
        r16 = ctrl.Rule(self.stok['Sedang'] & self.ems['Lama'] & self.speed['Lambat'], self.diskon['Sedang'])
        r17 = ctrl.Rule(self.stok['Sedang'] & self.ems['Lama'] & self.speed['Normal'], self.diskon['Sedikit'])
        r18 = ctrl.Rule(self.stok['Sedang'] & self.ems['Lama'] & self.speed['Cepat'], self.diskon['Sedikit'])

        r19 = ctrl.Rule(self.stok['Banyak'] & self.ems['Kritis'] & self.speed['Lambat'], self.diskon['Besar'])
        r20 = ctrl.Rule(self.stok['Banyak'] & self.ems['Kritis'] & self.speed['Normal'], self.diskon['Besar'])
        r21 = ctrl.Rule(self.stok['Banyak'] & self.ems['Kritis'] & self.speed['Cepat'], self.diskon['Besar'])
        r22 = ctrl.Rule(self.stok['Banyak'] & self.ems['Aman'] & self.speed['Lambat'], self.diskon['Besar'])
        r23 = ctrl.Rule(self.stok['Banyak'] & self.ems['Aman'] & self.speed['Normal'], self.diskon['Sedang'])
        r24 = ctrl.Rule(self.stok['Banyak'] & self.ems['Aman'] & self.speed['Cepat'], self.diskon['Sedang'])
        r25 = ctrl.Rule(self.stok['Banyak'] & self.ems['Lama'] & self.speed['Lambat'], self.diskon['Besar'])
        r26 = ctrl.Rule(self.stok['Banyak'] & self.ems['Lama'] & self.speed['Normal'], self.diskon['Sedang'])
        r27 = ctrl.Rule(self.stok['Banyak'] & self.ems['Lama'] & self.speed['Cepat'], self.diskon['Sedikit'])

        self.engine = ctrl.ControlSystem([
            r1, r2, r3, r4, r5, r6, r7, r8, r9, 
            r10, r11, r12, r13, r14, r15, r16, r17, r18, 
            r19, r20, r21, r22, r23, r24, r25, r26, r27
        ])
        self.sim = ctrl.ControlSystemSimulation(self.engine)

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        if page_name == "OutputPage":
            frame.update_output()
        frame.tkraise()

    def calculate(self):
        try:
            self.sim.input['stok'] = self.stok_val.get()
            self.sim.input['ems'] = self.ems_val.get()
            self.sim.input['speed'] = self.speed_val.get()
            self.sim.compute()
            self.diskon_hasil = f"{round(self.sim.output['diskon'], 1)}"
            self.show_frame("OutputPage")
        except ValueError:
            messagebox.showwarning("Fuzzy Error", "Sistem tidak dapat menentukan diskon karena kombinasi nilai input berada di luar cakupan Rule yang didefinisikan. Tambahkan Rule baru untuk menangani kasus ini.")

class WelcomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#2c3e50")
        
        tk.Label(self, text="Selamat Datang di\nSmart Pricing System", font=("Arial", 32, "bold"), fg="white", bg="#2c3e50").pack(pady=(120, 30))
        tk.Label(self, text="Optimalkan Diskon Produk Anda\nBerdasarkan Data Inventaris Terkini", font=("Arial", 16), fg="#bdc3c7", bg="#2c3e50").pack(pady=(0, 100))
        
        tk.Button(self, text="Mulai Analisis", font=("Arial", 22, "bold"), bg="#27ae60", fg="white", activebackground="#2ecc71", activeforeground="white", relief="flat",padx=40, pady=15, command=lambda: controller.show_frame("InputPage")).pack()

class InputPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="white")
        self.controller = controller
        
        tk.Label(self, text="Input Data Produk", font=("Arial", 24, "bold"), bg="white", fg="#2c3e50").pack(pady=(40, 20))

        self.create_input_group(
            "Stok Saat Ini (%)", 
            controller.stok_val, 
            "Persentase jumlah produk saat ini dibandingkan dengan kapasitas maksimal gudang (0-100%)."
        )
        self.create_input_group(
            "Sisa Masa Simpan (Hari)", 
            controller.ems_val, 
            "Estimasi sisa waktu sebelum produk kedaluwarsa atau dianggap usang (0-730 Hari)."
        )
        self.create_input_group(
            "Kecepatan Penjualan (Unit/Mgg)", 
            controller.speed_val, 
            "Rata-rata persentase jumlah produk yang berhasil terjual dalam waktu satu minggu (0-100%)."
        )

        tk.Button(self, text="Hitung Rekomendasi", bg="#2980b9", fg="white", font=("Arial", 16, "bold"), 
                  relief="flat", pady=15, activebackground="#3498db", activeforeground="white",
                  command=self.validate_input).pack(fill="x", padx=60, pady=40)

    def create_input_group(self, label_text, var, help_text):
        frame = tk.Frame(self, bg="white")
        frame.pack(fill="x", padx=60, pady=10)
        
        lbl_head = tk.Label(frame, text=label_text, bg="white", font=("Arial", 14, "bold"), fg="#2c3e50")
        lbl_head.pack(anchor="w", pady=(0, 2))
        
        lbl_help = tk.Label(frame, text=help_text, bg="white", font=("Arial", 10, "italic"), fg="#7f8c8d", wraplength=380, justify="left")
        lbl_help.pack(anchor="w", pady=(0, 8))
        
        ent_input = tk.Entry(frame, textvariable=var, font=("Arial", 18), bg="#f8f9fa", fg="#2c3e50", 
                             relief="solid", bd=1, justify="center")
        ent_input.pack(fill="x", ipady=10)

    def validate_input(self):
        try:
            stok = float(self.controller.stok_val.get())
            ems = float(self.controller.ems_val.get())
            speed = float(self.controller.speed_val.get())

            if not (0 <= stok <= 100):
                messagebox.showwarning("Input Tidak Valid", "Stok harus berada di rentang 0% hingga 100%.")
                return 
            if not (0 <= ems <= 730):
                messagebox.showwarning("Input Tidak Valid", "Masa Simpan maksimal adalah 730 Hari.")
                return
            if not (0 <= speed <= 100):
                messagebox.showwarning("Input Tidak Valid", "Kecepatan Penjualan maksimal adalah 100 Unit/Minggu.")
                return

            self.controller.calculate()

        except ValueError:
            messagebox.showerror("Error Format", "Pastikan semua form telah diisi dengan format angka yang benar!")

class OutputPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#ecf0f1")
        self.controller = controller
        
        tk.Label(self, text="Hasil Analisis Strategi", font=("Arial", 24, "bold"), bg="#ecf0f1", fg="#2c3e50").pack(pady=(60, 30))
        
        self.res_box = tk.Frame(self, bg="white", padx=50, pady=50, highlightbackground="#dcdde1", highlightthickness=2)
        self.res_box.pack(pady=20, fill="x", padx=60)
        
        tk.Label(self.res_box, text="Diskon yang Disarankan:", bg="white", font=("Arial", 14, "bold"), fg="#7f8c8d").pack(pady=(0, 15))
        
        self.lbl_final = tk.Label(self.res_box, text="0.0%", font=("Arial", 64, "bold"), fg="#e74c3c", bg="white")
        self.lbl_final.pack()

        tk.Button(self, text="Ulangi Analisis", font=("Arial", 16, "bold"), bg="#95a5a6", fg="white", 
                  relief="flat", pady=12, command=lambda: controller.show_frame("InputPage")).pack(fill="x", padx=60, pady=(30, 10))
        
        tk.Button(self, text="Keluar Program", font=("Arial", 16, "bold"), bg="#c0392b", fg="white", 
                  relief="flat", pady=12, command=controller.quit).pack(fill="x", padx=60)

    def update_output(self):
        self.lbl_final.config(text=f"{self.controller.diskon_hasil}%")

if __name__ == "__main__":
    app = FuzzyApp()
    app.mainloop()