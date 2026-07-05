import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.geometry("320x450")
window.resizable(False, False)
window.configure(bg="#1e1e1e")

display = tk.Entry(
    window,
    font=("Arial", 24),
    justify="right",
    bd=10,
    bg="#2b2b2b",
    fg="white",
    insertbackground="white"
)
display.pack(fill="both", padx=10, pady=10, ipady=10)

def button_click(value):
    display.insert(tk.END, value)

def clear():
    display.delete(0, tk.END)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

def add_hover(btn, base, hover):
    def on_enter(e):
        btn['bg'] = hover
    def on_leave(e):
        btn['bg'] = base
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

button_frame = tk.Frame(window, bg="#1e1e1e")
button_frame.pack(fill="both", expand=True, padx=10, pady=10)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for r, row in enumerate(buttons):
    for c, text in enumerate(row):

        base_color = "#333333"
        hover_color = "#555555"
        special_color = "#ff9500"

        if text == "C":
            btn = tk.Button(button_frame, text=text, font=("Arial", 18),
                            bg="#d9534f", fg="white", activebackground="#c9302c",
                            command=clear)

        elif text == "=":
            btn = tk.Button(button_frame, text=text, font=("Arial", 18),
                            bg=special_color, fg="white", activebackground="#e08900",
                            command=calculate)

        else:
            btn = tk.Button(button_frame, text=text, font=("Arial", 18),
                            bg=base_color, fg="white", activebackground="#444444",
                            command=lambda v=text: button_click(v))
            add_hover(btn, base_color, hover_color)

        btn.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")

for i in range(4):
    button_frame.grid_rowconfigure(i, weight=1)
    button_frame.grid_columnconfigure(i, weight=1)

window.mainloop()