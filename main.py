import customtkinter

class Button(customtkinter.CTkButton):
    def __init__(self, value, posiX, posiY):

        if value.isdigit() or value == ",":
            back_color = "#525150"
            txt_color = "#ffffff"
            hv_color = "#363534"
        elif value == "=":
            back_color = "#d47e06"
            txt_color = "#FFFFFF"
            hv_color = "#905503"
        else:
            back_color = "#c4c3c0"
            txt_color = "#525150"
            hv_color = "#747471"

        super().__init__(app, text=value, font=("arial",25), command=self.button_callback, width=70,
                        height=70, fg_color=back_color, text_color=txt_color, hover_color=hv_color)
        self.grid(row=posiX, column=posiY, padx=2, pady=2, sticky="nsew")

        self.value = value

    def button_callback(self):
        print(f"button {self.value} pressed")

class Label(customtkinter.CTkLabel):
    def __init__(self, master, posiX, posiY, label_size, font_size):
        super().__init__(master, height=label_size, anchor="e", padx=10, font=("arial", font_size))

        self.grid(row=posiX, column=posiY, columnspan=4, sticky="nsew")
        self.configure(text = "Some example text!")

customtkinter.set_appearance_mode("dark")
app = customtkinter.CTk()
app.title("my app")
app.geometry("300x480")
app.minsize(width=200, height=300)

for i in range(4):
    app.grid_columnconfigure(i, weight=1)

for i in range(6):
    app.grid_rowconfigure(i, weight=1)

Input = Label(app, 0, 0, 60, 35)
Output = Label(app, 1, 0, 40, 20)

button_layouts = { # value, posiX, posiY
    "b9": ("9", 3, 0),
    "b8": ("8", 3, 1),
    "b7": ("7", 3, 2),
    "b6": ("6", 4, 0),
    "b5": ("5", 4, 1),
    "b4": ("4", 4, 2),
    "b3": ("3", 5, 0),
    "b2": ("2", 5, 1),
    "b1": ("1", 5, 2),
    "b0": ("0", 6, 1),
    "AC": ("AC", 2, 0),
    "percent": ("%", 2, 1),
    "del": ("Del", 2, 2),
    "div": ("÷", 2, 3),
    "mult": ("x", 3, 3),
    "minus": ("–", 4, 3),
    "plus": ("+", 5, 3),
    "double0": ("00", 6, 0),
    "comma": (",", 6, 2),
    "equal": ("=", 6, 3)
}

for layout in button_layouts.items():
    val, x, y = layout[1]
    Button(val, x, y)

app.mainloop()
