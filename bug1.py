import tkinter as tk

# Check which bin the item goes into
def check_bin():
    item = item_entry.get().lower().strip()
    if item == "can":
        result_label.config(text="Blue recycling bin!", fg="#1565C0")
    elif item == "paper":
        result_label.config(text="Blue recycling bin!", fg="#1565C0")
    elif item == "plastic bottle":
        result_label.config(text="Blue recycling bin! Rinse it first.", fg="#1565C0")
    elif item == "food":
        result_label.config(text="Food waste bin", fg="#6D4C41")
    else:
        result_label.config(text="General waste bin", fg="#424242")

# Set up the app window
window = tk.Tk()
window.title("Recycle Sorter")
window.geometry("360x640")
window.configure(bg="#E8F5E9")

title_label = tk.Label(window, text="Recycle Sorter", font=("Arial", 22, "bold"),
                       bg="#E8F5E9", fg="#2E7D32")
title_label.pack(pady=30)

question_label = tk.Label(window, text="What are you throwing away?",
                          font=("Arial", 14), bg="#E8F5E9")
question_label.pack(pady=10)

item_entry = tk.Entry(window, font=("Arial", 16), justify="center")
item_entry.pack(pady=10)

check_button = tk.Button(window, text="Which bin?", font=("Arial", 16, "bold"),
                         bg="#43A047", fg="white", width=14, command=check_bin)
check_button.pack(pady=20)

result_label = tk.Label(window, text="", font=("Arial", 16, "bold"),
                        bg="#E8F5E9", wraplength=300)
result_label.pack(pady=20)

hint_label = tk.Label(window, text="Try: can, paper, plastic bottle, food",
                      font=("Arial", 11), bg="#E8F5E9", fg="#616161")
hint_label.pack(side="bottom", pady=20)

window.mainloop()
