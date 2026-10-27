
import tkinter as tk
import matplotlib.pyplot as plt


# Draw a chart of how many hours the lights and fans were left on
def show_chart():
    lights = float(lights_entry.get())
    fans = float(fans_entry.get())

    total = lights + fans
    if total > 2:
        message_label.config(text="Remember to switch off before you leave!")
    else:
        message_label.config(text="Great job saving energy!")

    plt.bar(["Lights", "Fans"], [lights, fans], color=["#FBC02D", "#29B6F6"])
    plt.title("Hours left on in an empty classroom")
    plt.ylabel("Hours")
    plt.show()


# Set up the app window
window = tk.Tk()
window.title("Classroom Energy Tracker")
window.geometry("360x640")
window.configure(bg="#FFFDE7")

title_label = tk.Label(window, text="Energy Tracker", font=("Arial", 22, "bold"),
                       bg="#FFFDE7", fg="#F57F17")
title_label.pack(pady=30)

tk.Label(window, text="Hours lights were left on:", font=("Arial", 14),
         bg="#FFFDE7").pack(pady=5)
lights_entry = tk.Entry(window, font=("Arial", 16), justify="center")
lights_entry.pack(pady=5)

tk.Label(window, text="Hours fans were left on:", font=("Arial", 14),
         bg="#FFFDE7").pack(pady=5)
fans_entry = tk.Entry(window, font=("Arial", 16), justify="center")
fans_entry.pack(pady=5)

chart_button = tk.Button(window, text="Show chart", font=("Arial", 16, "bold"),
                         bg="#FB8C00", fg="white", width=14, command=show_chart)
chart_button.pack(pady=25)

message_label = tk.Label(window, text="", font=("Arial", 14, "bold"),
                         bg="#FFFDE7", fg="#2E7D32", wraplength=300)
message_label.pack(pady=10)

window.mainloop()
