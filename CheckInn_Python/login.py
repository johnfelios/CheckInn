import customtkinter
from Home import Home

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class Login:
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.geometry("800x600")
        self.frame = customtkinter.CTkFrame(master=self.root)
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)
        self.label = customtkinter.CTkLabel(master=self.frame, text="Login System")
        self.label.pack(pady=12, padx=10)
        self.entry1 = customtkinter.CTkEntry(master=self.frame, placeholder_text="Username")
        self.entry1.pack(pady=12, padx=10)
        self.entry2 = customtkinter.CTkEntry(master=self.frame, placeholder_text="Password", show="*")
        self.entry2.pack(pady=12, padx=10)
        self.button = customtkinter.CTkButton(master=self.frame, text="Login", command=self.login)
        self.button.pack(pady=12, padx=10)

##Log-In
    def login(self):
        username = self.entry1.get()
        password = self.entry2.get()
        if username == "admin" and password == "password":
            self.root.destroy()
            Home()   ##Opens Home Screen

        else:
            customtkinter.CTkMessageDialog(master=self.root, message="Invalid username or password", icon="error")

      

    def start(self):
        self.root.mainloop()

login_system = Login()
login_system.start()
