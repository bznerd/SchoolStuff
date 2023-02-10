"""
Ben Campbell 10/19/22
PLTW 2.1.4 Step 26
Login window
"""

import tkinter as tk

# main window
root = tk.Tk()
root.wm_geometry("200x150")
root.title("Authorization")

#Login screen
frame_login = tk.Frame(root)
frame_login.grid(row=0, column=0, stick='news')

#Login label and button
lbl_username = tk.Label(frame_login, text='Username:')
lbl_username.pack()

ent_username = tk.Entry(frame_login, bd=2)
ent_username.pack(pady=5)

#Login label and button
lbl_password = tk.Label(frame_login, text="Password:")
lbl_password.pack()

ent_password = tk.Entry(frame_login, bd=2, show='*')
ent_password.pack(pady=5)

#Login button callback
def test_my_btn():
    frame_auth.tkraise()
    lbl_auth_user.config(text=ent_password.get())

#Login button
login_btn = tk.Button(frame_login, text='Login', command=test_my_btn)
login_btn.pack()

#Auth screen
frame_auth = tk.Frame(root)
frame_auth.grid(row=0, column=0, stick='news')

#Entered password label
lbl_auth_user = tk.Label(frame_auth)
lbl_auth_user.pack()

#Display login over auth
frame_login.tkraise()

#Mainloop
root.mainloop()
