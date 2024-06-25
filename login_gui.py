import tkinter as tk
from tkinter import messagebox

class LoginGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Login GUI")
        self.root.geometry("500x300")

        self.caseIDLabel = tk.Label(root, text="CaseID")
        self.caseIDLabel.place(x=50, y=20, width=80, height=25)

        self.caseIDText = tk.Entry(root)
        self.caseIDText.place(x=160, y=20, width=250, height=25)

        self.passwordLabel = tk.Label(root, text="Password")
        self.passwordLabel.place(x=50, y=70, width=80, height=25)

        self.passwordText = tk.Entry(root, show="*")
        self.passwordText.place(x=160, y=70, width=250, height=25)

        self.phoneNumberLabel = tk.Label(root, text="Phone Number")
        self.phoneNumberLabel.place(x=50, y=120, width=120, height=25)

        self.phoneNumberText = tk.Entry(root)
        self.phoneNumberText.place(x=160, y=120, width=250, height=25)

        self.loginButton = tk.Button(root, text="Login", command=self.login)
        self.loginButton.place(x=185, y=170, width=200, height=25)

        self.user = None
        self.password = None
        self.phoneNumber = None

    def login(self):
        self.user = self.caseIDText.get()
        self.password = self.passwordText.get()
        self.phoneNumber = self.phoneNumberText.get()

        if self.user and self.password and self.phoneNumber:
            messagebox.showinfo("Login Successful", "Enrollment successful!")
            self.run_auto_enroll()
        else:
            messagebox.showerror("Error", "All fields are required!")

    def run_auto_enroll(self):
        # Placeholder for the actual enrollment logic
        # You can replace this with the actual function call, e.g.,
        # CWRUAutoEnroll.main()
        print(f"User: {self.user}")
        print(f"Password: {self.password}")
        print(f"Phone Number: {self.phoneNumber}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginGUI(root)
    root.mainloop()
