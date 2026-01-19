# Signature Verification System 

A **Machine Learning–based Signature Verification System** that verifies handwritten signatures using **Convolutional Neural Networks (CNN)**.  
The system helps in detecting **genuine vs forged signatures** through an easy-to-use GUI.

---

## Problem Statement
Manual verification of handwritten signatures is time-consuming and prone to errors.  
This project automates the process using **Deep Learning**, improving accuracy and reliability.

---

## Features
- Handwritten signature verification using **CNN**
- GUI-based application
- User **Login & Registration**
- Signature image upload and verification
- Stores verification data in database
- Trained ML models for prediction

---

## Tech Stack
- **Programming Language:** Python  
- **Deep Learning:** CNN  
- **Libraries:** TensorFlow, Keras, NumPy, Pandas, OpenCV  
- **GUI:** Tkinter  
- **Database:** SQLite  

---

## How It Works
1. User registers and logs in  
2. Uploads a handwritten signature image  
3. Image preprocessing is applied  
4. CNN model analyzes the signature  
5. System predicts **Genuine / Forged** result  

---

## Project Structure
Signature-Verification-System/
│
├── assets/ # Images & UI assets
├── GUI_main.py # Main GUI
├── GUI_master.py # GUI controller
├── data_process.py # Data preprocessing
├── CNN_model.h5 # Trained CNN model
├── clf_SVM.pkl # ML classifier
├── evaluation.db # Database
├── signature_login.py # Login module
├── signature_registration.py # Registration module
└── README.md


---

## Outcome
- Accurate signature verification using CNN  
- Reduced manual effort and human error  

---

## Future Scope
- Improve accuracy using larger datasets  
- Add real-time camera-based verification  
- Deploy as a web application using Flask/Django  

---

## Author
**Aarti Patil**  
MCA Graduate | Frontend & Python Full Stack Developer  
Pune  
LinkedIn: https://linkedin.com/in/aarti-patil

