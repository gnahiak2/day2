


import tkinter as tk

LITRES_PER_MINUTE = 9  # rough estimate for a typical shower


def calculate():
    minutes = float(minutes_entry.get())
    litres = minutes * LITRES_PER_MINUTE
    result_label.config(text=f"Your shower used about {litres:g} litres of water.")
    if minutes > 5:
        tip_label.config(text="Tip: try to keep your shower under 5 minutes!")
    else:
        tip_label.config(text="Great job saving water!")


# Set up the app window
window = tk.Tk()
window.title("Shower Timer")
window.geometry("360x640")
window.configure(bg="#E3F2FD")

title_label = tk.Label(window, text="Shower Timer", font=("Arial", 22, "bold"),
                       bg="#E3F2FD", fg="#1565C0")
title_label.pack(pady=30)

question_label = tk.Label(window, text="How many minutes was your shower?",
                          font=("Arial", 14), bg="#E3F2FD")
question_label.pack(pady=10)

minutes_entry = tk.Entry(window, font=("Arial", 16), justify="center")
minutes_entry.pack(pady=10)

calc_button = tk.Button(window, text="Calculate", font=("Arial", 16, "bold"),
                        bg="#1E88E5", fg="white", width=14, command=calculate)
calc_button.pack(pady=20)

result_label = tk.Label(window, text="", font=("Arial", 15, "bold"),
                        bg="#E3F2FD", wraplength=300)
result_label.pack(pady=10)

tip_label = tk.Label(window, text="", font=("Arial", 13),
                     bg="#E3F2FD", fg="#2E7D32", wraplength=300)
tip_label.pack(pady=10)

window.mainloop()
