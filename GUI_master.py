import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image , ImageTk 
from tkinter.filedialog import askopenfilename
import cv2
import numpy as np
import time
import os
#import tfModel_CPU 
import data_process as dt_proc
global fn
import smtplib
from email.message import EmailMessage
import imghdr
import pickle
from sklearn.preprocessing import LabelEncoder
from skimage import feature

fn=""

# basepath= os.path.normpath(r'C:\Users\91749\Desktop\Tushar SCT\Extracted File\signature detection\finalcode')

##############################################+=============================================================
root = tk.Tk()
root.configure(background="seashell2")
#root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Signature Detection System")


#430

#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 =Image.open('C:/Users/91749/Desktop/Tushar SCT/Extracted File/signature detection/final code/Signature.jpg')
image2 =image2.resize((w,h), Image.LANCZOS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)
#


lb9 = tk.Label(root, text="Signature Detection System", font=('times', 35,' bold '), height=1, width=32,bg="Royal Blue",fg="white")
lb9.place(x=200, y=20)


frame_display = tk.LabelFrame(root, text=" --Process-- ", width=220, height=350, bd=5, font=('times', 14, ' bold '),bg="SeaGreen1")
frame_display.grid(row=0, column=0, sticky='nw')
frame_display.place(x=10, y=100)
################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 

# def clear_img():
    
#     img11 = tk.Label(frame_display, background='seashell2',width=160,height=120)
#     img11.place(x=0, y=0)

def update_label(str_T):
    
    result_label = tk.Label(root, text=str_T, width=50, font=("bold", 25),bg='seashell2',fg='black' )
    result_label.place(x=500, y=200)



def CL_CNN():


    update_label("CNN Training Process Start...............")
    
    start = time.time()

    X=dt_proc.CNN_Model()
    
    end = time.time()
        
    ET="Execution Time: {0:.5} seconds \n".format(end-start)
    
    msg=X+'\n'+ET

    update_label(msg)
    
    
# Email function with success message update in GUI
def send_email_with_image(image_path):
    try:
        Sender_Email = "pragati.code@gmail.com"
        Receiver_Email = "ankita.sctcode@gmail.com"
        Password = 'grqheqzoutabdfzd'

        newMessage = EmailMessage()
        newMessage['Subject'] = "Signature Forgery Detected"
        newMessage['From'] = Sender_Email
        newMessage['To'] = Receiver_Email

        # Email body
        newMessage.set_content(
            f"Dear User,\n\nThe system detected a forged signature. Please find the attached image for reference.\n\nBest Regards,\nSignature Detection Team"
        )

        # Attach the image
        with open(image_path, 'rb') as f:
            image_data = f.read()
            image_type = imghdr.what(f.name)
            image_name = f.name
        newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=os.path.basename(image_name))

        # Send the email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(Sender_Email, Password)
            smtp.send_message(newMessage)

        # Display success message in the GUI
        update_label("Email sent successfully with the forged image attached!")

    except Exception as e:
        update_label(f"Error in sending email: {str(e)}")


# Modified test_model_proc function
def test_model_proc(fn):
    from keras.preprocessing.image import load_img
    from keras.preprocessing.image import img_to_array
    from keras.models import load_model

    # Load and prepare the image
    def load_image(filename):
        img = load_img(filename, target_size=(32, 32))
        img = img_to_array(img)
        img = img.reshape(1, 32, 32, 3)
        img = img.astype('float32')
        return img

    # Load an image and predict the class
    def run_example():
        img = load_image(fn)
        model = load_model("CNN_model.h5")
        result = model.predict(img)
        print(result)
        return result.argmax(axis=1)

    preds = run_example()

    if preds == 1:
        label = "Signature is Real !!!"
    else:
        label = "Signature is Forged !!!"
       
        send_email_with_image(fn)  # Send email if forged signature is detected
        
      

    return label



# def test_model_proc(fn):
#     from keras.preprocessing.image import load_img
#     from keras.preprocessing.image import img_to_array
#     from keras.models import load_model

#     # load and prepare the image
#     def load_image(filename):
#         # load the image
#         img = load_img(filename, target_size=(32, 32))
#         # convert to array
#         img = img_to_array(img)
#         # reshape into a single sample with 3 channels
#         img = img.reshape(1, 32, 32, 3)
#         # center pixel data
#         img = img.astype('float32')
# #        img = img - [123.68, 116.779, 103.939]
#         return img
    
#     # load an image and predict the class
#     def run_example():
#         # load the image
#         img = load_image(fn)
#         # load model
#         model = load_model(basepath + '/CNN_model.h5')
#         # predict the class
#         result = model.predict(img)
#         print(result)
#         return (result.argmax(axis=1))
#     # entry point, run the example
    
#     preds=run_example()

    
#     if preds==1:
#         label="Signature is Real !!!"
#     else:
#         label="Signature is Forged !!!"


#     return label

# # def clear_img():
    
# #     img11 = tk.Label(frame_display, background='lightblue4',width=160,height=120)
# #     img11.place(x=0, y=0)

def update_label(str_T):
    #clear_img()
    result_label = tk.Label(root, text=str_T, width=40, font=("bold", 25), bg='bisque2', fg='black')
    result_label.place(x=300, y=420)
# def train_model():
    
#     update_label("Model Training Start...............")
    
#     start = time.time()

#     X=Model_frm.main()
    
#     end = time.time()
        
#     ET="Execution Time: {0:.4} seconds \n".format(end-start)
    
#     msg="Model Training Completed.."+'\n'+ X + '\n'+ ET

#     update_label(msg)

def test_model():
    global fn
    if fn!="":
        update_label("Model Testing Start...............")
        
        start = time.time()
    
        X=test_model_proc(fn)
        
        X1="Selected Image {0}".format(X)
        
        end = time.time()
            
        ET="Execution Time: {0:.4} seconds \n".format(end-start)
        
        msg="Image Testing Completed.."+'\n'+ X1 + '\n'+ ET
        fn=""
    else:
        msg="Please Select Image For Prediction...."
        
    update_label(msg)
    

def openimage():
   
    global fn
    fn=""
#    clear_img()
    fileName = askopenfilename(initialdir='/dataset', title='Select image for Aanalysis ',
                               filetypes=[("all files", "*.*")])
    IMAGE_SIZE=300
    imgpath = fileName
    fn = fileName
    
    if fn!="":
    
        img = Image.open(imgpath)
        img = img.resize((IMAGE_SIZE,IMAGE_SIZE))
        img = np.array(img)
    
    
        x1 = int(img.shape[0])
        y1 = int(img.shape[1])
    
        
        im = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=im)
        img = tk.Label(root, image=imgtk, height=250, width=250)
        img.image = imgtk
        img.place(x=300, y=100)
    else:
        msg="Please Select Image ..........."    
        #update_label(msg)
    
def convert_grey():
    
    global fn    
    if fn !="":
        IMAGE_SIZE=300
        
        img = Image.open(fn)
        img = img.resize((IMAGE_SIZE,IMAGE_SIZE))
        img = np.array(img)
        
        x1 = int(img.shape[0])
        y1 = int(img.shape[1])
    
        gs = cv2.cvtColor(cv2.imread(fn, 1), cv2.COLOR_RGB2GRAY)
    
        gs = cv2.resize(gs, (x1, y1))
    
        retval, threshold = cv2.threshold(gs, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    
        im = Image.fromarray(gs)
        imgtk = ImageTk.PhotoImage(image=im)
        
        img2 = tk.Label(root, image=imgtk, height=250, width=250,bg='white')
        img2.image = imgtk
        img2.place(x=580, y=100)

        im = Image.fromarray(threshold)
        imgtk = ImageTk.PhotoImage(image=im)

        img3 = tk.Label(root, image=imgtk, height=250, width=250)
        img3.image = imgtk
        img3.place(x=880, y=100)
    
        
    
        
    else:
        
        msg="Please Select Image ..........."    
        #update_label(msg)




#################################################################################################################
def window():
    root.destroy()




button1 = tk.Button(frame_display, text=" Select Image ", command=openimage,width=12, height=1, font=('times', 15, ' bold '),bg="yellow4",fg="white")
button1.place(x=10, y=20)

button2 = tk.Button(frame_display, text="Image Process", command=convert_grey, width=12, height=1, font=('times', 15, ' bold '),bg="yellow4",fg="white")
button2.place(x=10, y=100)

#button3 = tk.Button(frame_display, text="Train SVM Model", command=CL_SVM, width=12, height=1, font=('times', 15, ' bold '),bg="yellow4",fg="white")
#button3.place(x=400, y=20)
#
#button4 = tk.Button(frame_display, text="Train CNN Model", command=CL_CNN,width=12, height=1,bg="yellow4",fg="white", font=('times', 15, ' bold '))
#button4.place(x=5, y=140)
#
#
#button5 = tk.Button(frame_display, text="SVM Prediction", command=testSVM_model,width=12, height=1, font=('times', 15, ' bold '),bg="yellow4",fg="white")
#button5.place(x=800, y=20)

button6 = tk.Button(frame_display, text="CNN Prediction", command=test_model,width=12, height=1, font=('times', 15, ' bold '),bg="yellow4",fg="white")
button6.place(x=10, y=180)

exit = tk.Button(frame_display, text="Exit", command=window, width=10, height=1, font=('times', 15, ' bold '),bg="red",fg="white")
exit.place(x=10, y=260)



root.mainloop()