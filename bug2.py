


import tkinter as tk
import random

# A list of eco tips for students
tip_list = [
    "Bring your own water bottle to school.",
    "Switch off the lights and fans when you leave the classroom.",
    "Only take as much food as you can finish.",
    "Rinse bottles and cans before recycling them.",
    "Print double-sided, or don't print at all.",
    "Take the stairs instead of the lift.",
    "Say no to single-use plastic straws.",
]

# Show a random tip when the button is clicked
def show_tip():
    tip = random.choice(tip_list)
    tip_label.config(text=tip)

# Set up the app window
window = tk.Tk()
window.title("Eco Tip Generator")
window.geometry("360x640")
window.configure(bg="#E8F5E9")

title_label = tk.Label(window, text="Eco Tip Generator", font=("Arial", 22, "bold"),
                       bg="#E8F5E9", fg="#2E7D32")
title_label.pack(pady=40)

tip_label = tk.Label(window, text="Click the button for a green tip!",
                     font=("Arial", 15), bg="white", fg="#33691E",
                     wraplength=280, width=24, height=6, relief="groove")
tip_label.pack(pady=20)

tip_button = tk.Button(window, text="Show me a tip", font=("Arial", 16, "bold"),
                       bg="#43A047", fg="white", width=14, command=show_tip)
tip_button.pack(pady=30)

window.mainloop()
