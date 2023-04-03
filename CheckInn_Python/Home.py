import customtkinter
from CheckIn import CheckIn


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class Home:
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.geometry("800x600")
        self.frame = customtkinter.CTkFrame(master=self.root)
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)



        #add backround
        #bg_image = customtkinter.CTkImage(file="back.png")
        #bg_label = customtkinter.CTkLabel(master=self.frame, image=bg_image)
        #bg_label.place(relx=0.5, rely=0.5, anchor="center")

        button1 = customtkinter.CTkButton(master=self.frame, text="Check In", command=self.go_to_check_in)
        button1.pack(pady=12, padx=10)

        button2 = customtkinter.CTkButton(master=self.frame, text="Check Out")
        button2.pack(pady=12, padx=10)

        button3 = customtkinter.CTkButton(master=self.frame, text="Housekeeping")
        button3.pack(pady=12, padx=10)

        button4 = customtkinter.CTkButton(master=self.frame, text="Requests")
        button4.pack(pady=12, padx=10)

        


    def go_to_check_in(self):
        check_in_window = CheckIn()
        self.root.destroy()
        check_in_window.root.mainloop()


    def start(self):
        self.root.mainloop()

