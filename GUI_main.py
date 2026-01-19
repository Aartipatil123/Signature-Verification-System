import tkinter as tk
from PIL import Image, ImageTk

# Root window configuration
root = tk.Tk()
root.configure(background="#104E8B")
root.geometry("1300x1000")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Documentation Signature Detection")

# Background Image
image2 = Image.open('assets/s7.jpeg')
image2 = image2.resize((w, h), Image.LANCZOS)
background_image = ImageTk.PhotoImage(image2)
background_label = tk.Label(root, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0)

# Header (Title)
label = tk.Label(root, text="S𝕚𝕘𝕟𝕒𝕥𝕦𝕣𝕖 D𝕖𝕥𝕖𝕔𝕥𝕚𝕠𝕟", font=("Algerian", 40),
                 bg="#d6eaf8", fg='#17202a', width=50, height=1)
label.place(x=0, y=0)

# Navbar Frame
navbar_frame = tk.Frame(root, bg="#d4e6f1", height=50)
navbar_frame.place(x=0, y=70, width=w)

# Navbar Buttons
def about():
    from subprocess import call
    call(["python", "About Us.py"])

def contact():
    from subprocess import call
    call(["python", "contact_us.py"])

def log():
    from subprocess import call
    call(["python", "signature login.py"])

def reg():
    from subprocess import call
    call(["python", "signature registration.py"])

login_button = tk.Button(navbar_frame, text="​Log in​", command=log, font=('times', 18, 'bold'),
                         bg="#FFC107", fg="black", width=20)
login_button.pack(side="left", padx=40, pady=5)

register_button = tk.Button(navbar_frame, text="Registration", command=reg, font=('times', 18, 'bold'),
                            bg="#FFC107", fg="black", width=20)
register_button.pack(side="left", padx=40, pady=5)

about_button = tk.Button(navbar_frame, text="About Us", command=about, font=('times', 18, 'bold'),
                         bg="#28A745", fg="black", width=20)
about_button.pack(side="right", padx=40, pady=5)

contact_button = tk.Button(navbar_frame, text="Contact Us", command=contact, font=('times', 18, 'bold'),
                           bg="#28A745", fg="black", width=20)
contact_button.pack(side="right", padx=40, pady=5)

# Main Content Frame
#frame_alpr = tk.LabelFrame(root, text=" --​🇱​​🇴​​🇬​​🇮​​🇳​ & ​🇷​​🇪​​🇬​​🇮​​🇸​​🇹​​🇪​​🇷​--", 
#                           width=500, height=300, bd=0, font=('times', 20, 'bold'), bg="black", fg="orange")
#frame_alpr.place(x=60, y=300)
#button1 = tk.Button(frame_alpr, text="Login", command=log, width=15, height=1,
 #                   font=('times', 14, 'bold'), bg="#0d73d1", fg="black")
#button1.pack(pady=20)

#utton2 = tk.Button(frame_alpr, text="Registration", command=reg, width=15, height=1,
 #                   font=('times', 14, 'bold'), bg="#0d73d1", fg="black")
#button2.pack(pady=10)

#button3 = tk.Button(frame_alpr, text="About", command=about, width=15, height=1,
#                    font=('times', 14, 'bold'), bg="#0d73d1", fg="black")
#button3.pack(pady=20)

#button4 = tk.Button(frame_alpr, text="Contact", command=contact, width=15, height=1,
 #                   font=('times', 14, 'bold'), bg="#0d73d1", fg="black")
#button4.pack(pady=20)

# Run the application
root.mainloop()

