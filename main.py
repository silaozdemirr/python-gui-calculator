import tkinter as tk

window = tk.Tk()

window.title("Calculator")

window.geometry("320x450")

window.resizable(False, False)

display = tk.Entry(
    window,
    font=("Arial", 24),
    justify="right",
    bd=10
)

display.pack(fill="both", padx=10, pady=10, ipady=10)

window.mainloop()