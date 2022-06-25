from tkinter import *
from tkinter import filedialog as fd
import hashlib

root = Tk()
root.title("Encrypt Files")
root.configure(background="gold")
root.geometry("250x190")

def apply_md5():
    print("MD5 function")
    text_file = fd.askopenfilename(title="Open Text File", filetypes=(("Text Files", "*.txt"),))
    print(text_file)
    file = open(text_file, "r")
    paragraph = file.read()
    hashed_data = hashlib.md5(paragraph.encode())
    hexd_data = hashed_data.hexdigest()
    md5_file = open("md5.txt", "w")
    md5_file.write(hexd_data)
    md5_file.close()

def apply_sha256():
    text_file = fd.askopenfilename(title="Open Text File", filetypes=(("Text Files", "*.txt"),))
    print(text_file)
    file = open(text_file, "r")
    paragraph = file.read()
    hashed_data = hashlib.sha256(paragraph.encode())
    hexd_data = hashed_data.hexdigest()
    sha256_file = open("sha256.txt", "w")
    sha256_file.write(hexd_data)
    sha256_file.close()

btn1 = Button(root, text="Apply MD5", bg="SteelBlue1", command=apply_md5)
btn1.place(relx=0.3, rely=0.5, anchor=CENTER)

btn2 = Button(root, text="Apply SHA256", bg="SteelBlue1", command=apply_sha256)
btn2.place(relx=0.7, rely=0.5, anchor=CENTER)

root.mainloop()