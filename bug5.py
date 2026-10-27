import tkinter as tk


# Add up the food waste from recess and lunch
def calculate_total():
    recess = float(recess_entry.get())
    lunch = float(lunch_entry.get())
    total = recess + lunch
    result_label.config(text=f"Total waste today: {total} g")


# Set up the app window
window = tk.Tk()
window.title("Canteen Waste Calculator")
window.geometry("360x640")
window.configure(bg="#FFF3E0")

title_label = tk.Label(window, text="Canteen Waste\nCalculator", font=("Arial", 22, "bold"),
                       bg="#FFF3E0", fg="#E65100")
title_label.pack(pady=30)

tk.Label(window, text="Food wasted at recess (grams):", font=("Arial", 14),
         bg="#FFF3E0").pack(pady=5)
recess_entry = tk.Entry(window, font=("Arial", 16), justify="center")
recess_entry.pack(pady=5)

tk.Label(window, text="Food wasted at lunch (grams):", font=("Arial", 14),
         bg="#FFF3E0").pack(pady=5)
lunch_entry = tk.Entry(window, font=("Arial", 16), justify="center")
lunch_entry.pack(pady=5)

calc_button = tk.Button(window, text="Calculate", font=("Arial", 16, "bold"),
                        bg="#FB8C00", fg="white", width=14, command=calculate_total)
calc_button.pack(pady=25)

result_label = tk.Label(window, text="", font=("Arial", 16, "bold"),
                        bg="#FFF3E0", fg="#BF360C", wraplength=300)
result_label.pack(pady=10)

window.mainloop()
