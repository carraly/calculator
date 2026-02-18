import customtkinter

class Button(customtkinter.CTkButton):
    
    def __init__(self, master, value, posiX, posiY):

        self.value = value

        super().__init__(master, text=value, command=self.button_callback, width=70, height=70)
        self.grid(row=posiX, column=posiY, padx=2, pady=2)

    def button_callback(self):
        print(f"button {self.value} pressed")

app = customtkinter.CTk()
app.title("my app")
app.geometry("400x450")

for i in range(4):
    app.grid_columnconfigure(i, weight=1)

button1 = Button(app, 1, 0, 0)
button2 = Button(app, 2, 0, 1)
button3 = Button(app, 3, 0, 2)
button4 = Button(app, 4, 1, 0)



app.mainloop()