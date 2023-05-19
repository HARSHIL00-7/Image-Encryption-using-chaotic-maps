from tkinter import * 
import tkinter as tk 
from PIL import ImageTk,Image
from tkinter import messagebox,filedialog
import numpy as np

def show_frame(frame):
    frame.tkraise()
    
def handle_login():
    email = email_entry.get()
    password = password_entry1.get()

    if email == 'harshilkumar7@gmail.com' and password == 'HarshilMinorProject':
        messagebox.showinfo('Authorized','Login Successful')
        show_frame(frame2)

    else:
        messagebox.showerror('Not Authorized','Login Failed')

def logistic_map(x, r):
    return r * x * (1 - x)


def chaotic_encrypt(img_array, key):
    x, y, z = key
    for i in range(100):
        x = logistic_map(x, 3.8)
        y = logistic_map(y, 3.9)
        z = logistic_map(z, 4.0)

    encrypted_img = np.zeros_like(img_array)
    rows, cols, channels = img_array.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(channels):
                x = logistic_map(x, 3.8)
                y = logistic_map(y, 3.9)
                z = logistic_map(z, 4.0)
                r = int(round(logistic_map(x, 3.7) * 1000)) % 256
                encrypted_img[i, j, k] = img_array[i, j, k] ^ r
                key[k] = x

    return encrypted_img, key

def chaotic_decrypt(img2_array, key):
    x, y, z = key
    for i in range(100):
        x = logistic_map(x, 3.8)
        y = logistic_map(y, 3.9)
        z = logistic_map(z, 4.0)

    decrypted_img = np.zeros_like(img2_array)
    rows, cols, channels = img2_array.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(channels):
                x = logistic_map(x, 3.8)
                y = logistic_map(y, 3.9)
                z = logistic_map(z, 4.0)
                r = int(round(logistic_map(x, 3.7) * 1000)) % 256
                decrypted_img[i, j, k] = img2_array[i, j, k] ^ r
                key[k] = x

    return decrypted_img

window = tk.Tk()
window.state('zoomed')

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

frame1 = tk.Frame(window)
frame2 = tk.Frame(window)
frame3 = tk.Frame(window)

for frame in (frame1, frame2, frame3):
    frame.grid(row=0,column=0,sticky='nsew')
    
#==================Frame 1 code
frame1_title=  tk.Label(frame1, text='Page 1', font='times 35')
frame1_title.pack(fill='both', expand=True)

design_frame1 = Listbox(frame1, bg='#0c71b9', width=115, height=50, highlightthickness=0, borderwidth=0)
design_frame1.place(x=0, y=0)

design_frame2 = Listbox(frame1, bg='#1e85d0', width=115, height=50, highlightthickness=0, borderwidth=0)
design_frame2.place(x=676, y=0)

design_frame3 = Listbox(frame1, bg='#1e85d0', width=100, height=33, highlightthickness=0, borderwidth=0)
design_frame3.place(x=75, y=106)

design_frame4 = Listbox(frame1, bg='#FFFFFF', width=100, height=33, highlightthickness=0, borderwidth=0)
design_frame4.place(x=676, y=106)


photo=Image.open('MUJBackground.jpeg')
img=ImageTk.PhotoImage(photo)
lbl_bk=tk.Label(design_frame4,image=img)
lbl_bk.image=img
lbl_bk.place(relx=0.45,rely=0.5,anchor='center')

email_entry = Entry(design_frame4, fg="#FFFFFF",bg="#1e85d0", font=("yu gothic ui semibold", 12), highlightthickness=0.2)
email_entry.place(x=134, y=170, width=256, height=34)
email_entry.config(highlightbackground="white", highlightcolor="black")
email_label = Label(design_frame4, text='• Email account', fg="#89898b", bg='#FFFFFF', font=("yu gothic ui", 11, 'bold'))
email_label.place(x=130, y=140)


password_entry1 = Entry(design_frame4, fg="#FFFFFF",bg="#1e85d0", font=("yu gothic ui semibold", 12), show='•', highlightthickness=0.2)
password_entry1.place(x=134, y=250, width=256, height=34)
password_entry1.config(highlightbackground="white", highlightcolor="black")
password_label = Label(design_frame4, text='• Password', fg="#89898b", bg='#FFFFFF', font=("yu gothic ui", 11, 'bold'))
password_label.place(x=130, y=220)

# ==== LOGIN  down button ============
loginBtn1 = Button(design_frame4, fg='black', text='Login', bg='#1e85d0', font=("yu gothic ui bold", 15),
                   cursor='hand2', activebackground='#1e85d0',command=handle_login)
loginBtn1.place(x=133, y=340, width=256, height=50)


# ===== Email icon =========
email_icon = Image.open('email-icon.png')
photo = ImageTk.PhotoImage(email_icon)
emailIcon_label = Label(design_frame4, image=photo, bg='#f8f8f8')
emailIcon_label.image = photo
emailIcon_label.place(x=105, y=174)
# ===== password icon =========
password_icon = Image.open('pass-icon.png')
photo = ImageTk.PhotoImage(password_icon)
password_icon_label = Label(design_frame4, image=photo, bg='#FFFFFF')
password_icon_label.image = photo
password_icon_label.place(x=105, y=254)

# function for show and hide password
def password_command():
    if password_entry1.cget('show') == '•':
        password_entry1.config(show='')
    else:
        password_entry1.config(show='•')


# ====== checkbutton ==============
checkButton = Checkbutton(design_frame4, bg='#f8f8f8',fg="#000000" ,command=password_command, text='Show Password')
checkButton.place(x=140, y=288)

# ===== Left Side Picture ============
side_image = Image.open('TKINTERlogin.jpeg')
photo = ImageTk.PhotoImage(side_image)
side_image_label = Label(design_frame3, image=photo, bg='#1e85d0')
side_image_label.image = photo
side_image_label.place(x=30, y=110)

# ===== Welcome Label ==============
welcome_label = Label(design_frame4, text='Manipal University Jaipur Minor Project', font=('Arial', 20, 'bold'), bg='#33A1C9')
welcome_label.place(x=70, y=35)
welcome_label = Label(design_frame4, text='Image encryption and decryption', font=('Arial', 18, 'bold'), bg='#33A1C9')
welcome_label.place(x=70, y=70)
welcome_label = Label(design_frame4, text='By Harshil Kumar', font=('Arial', 15, 'bold'), bg='#33A1C9')
welcome_label.place(x=70, y=102.5)


#Frame 2 code
frame2_title=  tk.Label(frame2, bg='#33A1C9')
frame2_title.pack(fill='both', expand=True)
welcome_label = Label(frame2, text='Manipal University Jaipur Minor Project', font=('Arial', 45, 'bold'),fg='black',bg='pink')
welcome_label.place(x=75, y=19)

enc_label = Label(frame2, text='Encryption', font=('Arial', 35, 'bold'),fg='black',bg='pink')
enc_label.place(x=185, y=125)

#creating frame 1
image_frame1 = Listbox(frame2, bg='#FFFFFF', width=30, height=15, highlightthickness=0, borderwidth=0.3)
image_frame1.place(x=200, y=195)

def select_image():
    filename = filedialog.askopenfilename(initialdir="/", title="Select Image",
                                          filetypes=(("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*")))
    image_frame1.insert(END, filename)
    img = Image.open(filename)
    img = img.resize((300, 300), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    label = Label(image_frame1, image=img)
    label.image = img
    label.place(x=0, y=0)

select_button = Button(frame2, text="Select Plain Image", font=('Arial', 10), bg='#FFFFFF', fg='#000000', command=select_image)
select_button.place(x=20, y=300)

#frame 1 over

pimage_label = Label(frame2, text='Plain Image', font=('Arial', 25, 'bold'),fg='black',bg='pink')
pimage_label.place(x=260, y=460)

dec_label = Label(frame2, text='Decryption', font=('Arial', 35, 'bold'),fg='black',bg='pink')
dec_label.place(x=185, y=515)

#creating frame 2

image_frame2 = Listbox(frame2, bg='#FFFFFF', width=30, height=15, highlightthickness=0, borderwidth=0.3)
image_frame2.place(x=200, y=575)

#Upload image in frame 2

def select_image():
    filename = filedialog.askopenfilename(initialdir="/", title="Select Image",
                                          filetypes=(("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*")))
    image_frame2.insert(END, filename)
    img = Image.open(filename)
    img = img.resize((300, 300), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    label = Label(image_frame2, image=img)
    label.image = img
    label.place(x=0, y=0)

select_button = Button(frame2, text="Select Encrypted Image", font=('Arial', 10), bg='#FFFFFF', fg='#000000', command=select_image)
select_button.place(x=20, y=700)

enc_label = Label(frame2, text='Encrypted Image', font=('Arial', 25, 'bold'),fg='black',bg='pink')
enc_label.place(x=225, y=845)

img = Image.open('filetobeencrypted.png')
img_array = np.array(img)
rows, cols, channels = img_array.shape
key = np.array([0.1, 0.2, 0.3])

encrypted_img, key_enc = chaotic_encrypt(img_array, key.copy())
encrypted_img = np.uint8(encrypted_img)
encrypted_img = Image.fromarray(encrypted_img)
encrypted_img.save("encrypted_image.png")

encrypted_array=np.array(encrypted_img)

decrypted_img = chaotic_decrypt(encrypted_array, key.copy())
decrypted_img = np.uint8(decrypted_img)
decrypted_img = Image.fromarray(decrypted_img)
decrypted_img.save("decrypted_image.png")

#frame 2 over
def show_encrypted_image():
    # Load the encrypted image and display it in image_frame3
    img = Image.open("encrypted_image.png")
    img = img.resize((300, 300), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    label = Label(image_frame3, image=img)
    label.image = img
    label.place(x=0, y=0)

#encryption Techniques
algo_label = Label(frame2, text='Choose Encryption Technique', font=('Arial', 25, 'bold'),fg='black',bg='pink')
algo_label.place(x=600, y=125)
#logistic Map
Algo1Btn = Button(frame2, fg='black', text='Logistic Map', bg='#1e85d0', font=("yu gothic ui bold", 15),
                   cursor='hand2', activebackground='#1e85d0',command=show_encrypted_image)
Algo1Btn.place(x=760, y=200, width=120, height=50)

#Arnold Map
Algo2Btn = Button(frame2, fg='black', text='Arnold Map', bg='#1e85d0', font=("yu gothic ui bold", 15),
                   cursor='hand2', activebackground='#1e85d0',command=lambda:[show_frame(frame2),handle_login])
Algo2Btn.place(x=760, y=300, width=120, height=50)

#DNA Encoding
Algo3Btn = Button(frame2, fg='black', text='DNA Encoding', bg='#1e85d0', font=("yu gothic ui bold", 15),
                   cursor='hand2', activebackground='#1e85d0',command=lambda:[show_frame(frame2),handle_login])
Algo3Btn.place(x=760, y=400, width=120, height=50)

#frame 3
image_frame3 = Listbox(frame2, bg='#FFFFFF', width=30, height=15, highlightthickness=0, borderwidth=0.3)
image_frame3.place(x=1100, y=195)
enc_label = Label(frame2, text='Encrypted Image', font=('Arial', 25, 'bold'),fg='black',bg='pink')
enc_label.place(x=1100, y=460)

#decryption tech.
algod_label = Label(frame2, text='Choose Decryption Technique', font=('Arial', 25, 'bold'),fg='black',bg='pink')
algod_label.place(x=600, y=515)
#logi
Algo1dBtn = Button(frame2, fg='black', text='Logistic Map', bg='#1e85d0', font=("yu gothic ui bold", 15),
                   cursor='hand2', activebackground='#1e85d0' )
Algo1dBtn.place(x=760, y=580, width=120, height=50)
#arnold
Algo2dBtn = Button(frame2, fg='black', text='Arnold Map', bg='#1e85d0', font=("yu gothic ui bold", 15),
                   cursor='hand2', activebackground='#1e85d0',command=lambda:[show_frame(frame2),handle_login])
Algo2dBtn.place(x=760, y=680, width=120, height=50)
#DNA Endo.
Algo3dBtn = Button(frame2, fg='black', text='DNA Encoding', bg='#1e85d0', font=("yu gothic ui bold", 15),
                   cursor='hand2', activebackground='#1e85d0',command=lambda:[show_frame(frame2),handle_login])
Algo3dBtn.place(x=760, y=780, width=120, height=50)

#IF4

image_frame4 = Listbox(frame2, bg='#FFFFFF', width=30, height=15, highlightthickness=0, borderwidth=0.3)
image_frame4.place(x=1100, y=575)
dec_label = Label(frame2, text='Decrypted Image', font=('Arial', 25, 'bold'),fg='black',bg='pink')
dec_label.place(x=1100, y=845)

#==================Frame 3 code
frame3_title=  tk.Label(frame3, text='Page 3',font='times 35', bg='green')
frame3_title.pack(fill='both', expand=True)

frame3_btn = tk.Button(frame3, text='Enter',command=lambda:show_frame(frame1))
frame3_btn.pack(fill='x',ipady=15)

show_frame(frame1)

window.mainloop()