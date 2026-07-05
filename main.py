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

button_frame = tk.Frame(window)
button_frame.pack(fill="both", expand=True, padx=10, pady=10)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row_index, row in enumerate(buttons):
    for column_index, button_text in enumerate(row):
        button = tk.Button(
            button_frame,
            text=button_text,
            font=("Arial", 18),
            width=5,
            height=2
        )
        button.grid(
            row=row_index,
            column=column_index,
            padx=5,
            pady=5,
            sticky="nsew"
        )

for i in range(4):
    button_frame.grid_rowconfigure(i, weight=1)
    button_frame.grid_columnconfigure(i, weight=1)

window.mainloop()