import customtkinter

class Button(customtkinter.CTkButton):
    def __init__(self, master, value, posiX, posiY):

        self.value = value

        super().__init__(master, text=value, command=self.button_callback, width=70, height=70)
        self.grid(row=posiX, column=posiY, padx=2, pady=2)

    def button_callback(self):
        print(f"button {self.value} pressed")

class TextBox(customtkinter.CTkTextbox):
    def __init__(self, master):
        super().__init__(master, width=400, corner_radius=0, height=100)
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.grid(row=0, column=0, columnspan=4, sticky="nsew")
        self.insert("0.0", "Some example text!\n")


app = customtkinter.CTk()
app.title("my app")
app.geometry("400x450")

for i in range(4):
    app.grid_columnconfigure(i, weight=1)

# region Numbered Buttons
button_9 = Button(app, "9", 2, 0)
button_8 = Button(app, "8", 2, 1)
button_7 = Button(app, "7", 2, 2)
button_6 = Button(app, "6", 3, 0)
button_5 = Button(app, "5", 3, 1)
button_4 = Button(app, "4", 3, 2)
button_3 = Button(app, "3", 4, 0)
button_2 = Button(app, "2", 4, 1)
button_1 = Button(app, "1", 4, 2)
button_0 = Button(app, "0", 5, 1)
# endregion

# region Operation Buttons
button_AC = Button(app, "AC", 1, 0)
button_Percent = Button(app, "%", 1, 1)
button_Del = Button(app, "Del", 1, 2)
button_Div = Button(app, "÷", 1, 3)
button_Mult = Button(app, "X", 2, 3)
button_Minus = Button(app, "-", 3, 3)
button_Plus = Button(app, "+", 4, 3)
button_Double0 = Button(app, "00", 5, 0)
button_Comma = Button(app, ",", 5, 2)
button_Equal = Button(app, "=", 5, 3)
# endregion

text = TextBox(app)

app.mainloop()