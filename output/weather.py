# made by: Hassan Zafar

import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Weather App")
window.geometry("778x400")
window.configure(bg="lightblue")


def verify_login():
    username = username_entry.get()
    password = password_entry.get()

    with open("logins.txt", "r") as logins:
        for line in logins:
            stored_username, stored_password = line.strip().split(",")

            if username == stored_username and password == stored_password:
                messagebox.showinfo(
                    "Login Successful", "You have successfully logged in!"
                )
                return
    messagebox.showerror("Invalid Login", "Username or Password is Incorrect!")


def new_user():
    username = username_entry.get()
    password = password_entry.get()

    with open("logins.txt", "r") as logins:
        content = logins.read()

    if username in content or password in content:
        messagebox.showerror("Invalid Login", "Username or Password is Incorrect!")

    else:
        logins.create()
        logins.write(f"{username},{password}\n")
        messagebox.showinfo(
            "New User Created", "You have successfully created a new user!"
        )


username_label = tk.Label(
    window, text="Username", font=("Arial", 14), fg="darkgreen", bg="lightblue"
)
username_label.grid(row=0, column=0)
username_entry = tk.Entry(window, font=("Arial", 14))
username_entry.grid(row=0, column=1)

password_label = tk.Label(
    window, text="Password", font=("Arial", 14), fg="darkgreen", bg="lightblue"
)
password_label.grid(row=1, column=0)
password_entry = tk.Entry(window, show="*", font=("Arial", 14))
password_entry.grid(row=1, column=1)

login_button = tk.Button(
    window,
    text="Login",
    command=verify_login,
    width=10,
    height=2,
    bg="lightgreen",
    fg="black",
)
login_button.grid(row=4, column=1)

new_user_button = tk.Button(
    window,
    text="New User",
    command=new_user,
    width=10,
    height=2,
    bg="lightgreen",
    fg="black",
)
new_user_button.grid(row=4, column=0)


def login(self):
    self.root.destroy()
    main_window = tk.Tk()
    main_window.title("Weather App - Main Window")
    main_window.geometry("800x400")
    main_window.configure(bg="lightblue")

    city_label = tk.Entry(
        main_window,
        text="Enter City:",
        font=("Arial", 14),
        fg="darkgreen",
        bg="lightblue",
    )
    city_label.pack(pady=10)


window.mainloop()
