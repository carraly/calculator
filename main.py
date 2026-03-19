import customtkinter

class Button(customtkinter.CTkButton):
    value = 0

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

        self.value = value

        super().__init__(app, text=value, font=("arial",25), command=self.button_callback, width=70,
                        height=70, fg_color=back_color, text_color=txt_color, hover_color=hv_color)
        self.grid(row=posiX, column=posiY, padx=2, pady=2, sticky="nsew")

    def validate(self):
        user_input = input_label.cget("text")
        if user_input == "":
            if self.value.isdigit() or self.value == "–":
                return True
            else:
                return False
        elif user_input == "0":
            if self.value in ["0", "00", "="]:
                return False
            else:
                return True
        elif user_input[-1] in ["–", "+", ","]:
            if self.value.isdigit():
                return True
            else: 
                return False
        elif user_input[-1] in ["x", "÷"]:
            if (self.value.isdigit()) or (self.value == "–"):
                return True
            else:
                return False
        else:
            return True

    def button_callback(self):
        if self.value.isdigit():
            self.validate()


class Label(customtkinter.CTkLabel):
    def __init__(self, master, posiX, posiY, label_size, font_size):
        super().__init__(master, height=label_size, anchor="e", padx=10, font=("arial", font_size))

        self.grid(row=posiX, column=posiY, columnspan=4, sticky="nsew")
        self.configure(text = "")

customtkinter.set_appearance_mode("dark")
app = customtkinter.CTk()
app.title("my app")
app.geometry("300x480")
app.minsize(width=200, height=300)

for i in range(4):
    app.grid_columnconfigure(i, weight=1)

for i in range(6):
    app.grid_rowconfigure(i, weight=1)

input_label = Label(app, 0, 0, 60, 35)
output_label = Label(app, 1, 0, 40, 20)

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
