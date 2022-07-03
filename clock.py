from tkinter import *
from tkinter.ttk import *

import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
const firebaseConfig = {
  apiKey: "AIzaSyDDLa5cEOzSUhT254XbqnqH-y9lPLY6nlI",
  authDomain: "clock-c8409.firebaseapp.com",
  projectId: "clock-c8409",
  storageBucket: "clock-c8409.appspot.com",
  messagingSenderId: "1021173176267",
  appId: "1:1021173176267:web:1b7e370bdb64bba48d484e",
  measurementId: "G-MN83M18X46"
};
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

from time import strftime

root = Tk()
root.title("Clock")

def time():
    string = strftime('%I:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)


label = Label(root, font=("ds-digital", 80), background = "black", foreground = "cyan")
label.pack(anchor='center')
time()
mainloop()