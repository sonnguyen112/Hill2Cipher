from tkinter import *
from tkinter import messagebox
import numpy as np

reciprocal = {
    1:1,
    3:9,
    5:21,
    7:15,
    9:3,
    11:19,
    15:7,
    17:23,
    19:11,
    21:5,
    23:17,
    25:25
}

def reciprocalModulo26(n):
    global reciprocal
    return reciprocal[n]

def charToInt(c):
    if c == "Z": return 0
    return ord(c) - ord("A") + 1

def intToChar(n):
    if n == 0: return "Z"
    return chr(n - 1 + 65)

def encode():
    def encipher(event):
        a1 = int(keyEntry1.get())
        a2 = int(keyEntry2.get())
        a3 = int(keyEntry3.get())
        a4 = int(keyEntry4.get())
        A = np.array([[a1, a2], [a3, a4]])
        if (reciprocalModulo26(round(np.linalg.det(A))) != -1):
            plaintext = plainTextEntry.get()
            plaintext = plaintext.upper()
            plaintext = plaintext.replace(" ", "")
            if (len(plaintext) % 2 != 0): plaintext += plaintext[len(plaintext) - 1]
            i = 0
            res = ""
            while i <= len(plaintext) - 1:
                p1 = charToInt(plaintext[i])
                p2 = charToInt(plaintext[i + 1])
                p = np.array([[p1],[p2]])
                c = np.dot(A, p)
                c1 = c[0][0]
                if c1 > 25: c1 = c1 % 26
                c2 = c[1][0]
                if c2 > 25: c2 = c2 % 26
                print(c1, c2)
                res += intToChar(c1) + intToChar(c2)
                i += 2
            print(res)
            resultLabel.config(text="Ciphertext: " + res)
        else:
            print(messagebox.showerror(title = "ERROR", message="The key is invalid"))



    encodeWin = Tk()
    encodeWin.geometry("2000x2000")
    canvas = Canvas(encodeWin, width = 2000, height = 2000)

    canvas.pack()
    plainTextLabel = Label(encodeWin, text = "PlainText:", fg = "red", font = ("Ink Free",40, "italic"))
    keyLabel = Label(encodeWin, text = "Key:", fg = "red", font = ("Ink Free",40, "italic"))
    plainTextEntry = Entry(encodeWin, font = ("Arial", 40), width = 100)
    keyEntry1 = Entry(encodeWin, font = ("Arial", 40, "bold"), width = 2)
    keyEntry2 = Entry(encodeWin, font=("Arial", 40, "bold"), width = 2)
    keyEntry3 = Entry(encodeWin, font=("Arial", 40, "bold"), width = 2)
    keyEntry4 = Entry(encodeWin, font=("Arial", 40, "bold"), width = 2)
    calculateBut = Button(encodeWin, text = "CALCULATE", bd = 10, bg = "black", fg = "#00ff00", font = ("Int Free", 40, "bold"))
    resultLabel = Label(encodeWin, font=("Arial", 40, "bold"))

    plainTextLabel.place(x = 0, y = 0)
    plainTextEntry.place(x = 300, y = 0)
    keyLabel.place(x = 0, y = 200)
    canvas.create_line(280, 130, 280, 340, width = 10)
    canvas.create_line(480, 130, 480, 340, width = 10)
    canvas.create_line(280, 130, 300, 130, width = 10)
    canvas.create_line(280, 340, 300, 340, width = 10)
    canvas.create_line(480, 130, 460, 130, width = 10)
    canvas.create_line(480, 340, 460, 340, width = 10)
    keyEntry1.place(x = 300, y = 150)
    keyEntry2.place(x = 400, y = 150)
    keyEntry3.place(x = 300, y = 250)
    keyEntry4.place(x = 400, y = 250)
    calculateBut.place(x = 600, y = 400)
    resultLabel.place(x=0, y = 600)
    encodeWin.bind("<Return>", encipher)
    calculateBut.bind("<Button-1>", encipher)


def decode():
    def decipher(event):
        a1 = int(keyEntry1.get())
        a2 = int(keyEntry2.get())
        a3 = int(keyEntry3.get())
        a4 = int(keyEntry4.get())
        A = np.array([[a1, a2], [a3, a4]])
        if (reciprocalModulo26(round(np.linalg.det(A))) != -1):
            detAInvert = reciprocalModulo26(round(np.linalg.det(A)))
            adjA = np.array([[A[1][1],-A[0][1]],[-A[1][0],A[0][0]]])
            Ainvert = detAInvert * adjA
            if Ainvert[0][0] > 25 or Ainvert[0][0] < 0: Ainvert[0][0] %= 26
            if Ainvert[0][1] > 25 or Ainvert[0][1] < 0 : Ainvert[0][1] %= 26
            if Ainvert[1][0] > 25 or Ainvert[1][0] < 0: Ainvert[1][0] %= 26
            if Ainvert[1][1] > 25 or Ainvert[1][1] < 0: Ainvert[1][1] %= 26
            ciphertext = CipherTextEntry.get()
            ciphertext = ciphertext.upper()
            ciphertext = ciphertext.replace(" ", "")
            if (len(ciphertext) % 2 != 0): ciphertext += ciphertext[len(ciphertext) - 1]
            i = 0
            res = ""
            while i <= len(ciphertext) - 1:
                c1 = charToInt(ciphertext[i])
                c2 = charToInt(ciphertext[i + 1])
                c = np.array([[c1], [c2]])
                p = np.dot(Ainvert, c)
                print(p)
                p1 = p[0][0]
                if p1 > 25: p1 = p1 % 26
                p2 = p[1][0]
                if p2 > 25: p2 = p2 % 26
                print(p1, p2)
                res += intToChar(p1) + intToChar(p2)
                i += 2
            print(res)
            resultLabel.config(text="PlainText: " + res)
        else:
            print(messagebox.showerror(title="ERROR", message="The key is invalid"))


    decodeWin = Tk()
    decodeWin.geometry("2000x2000")

    canvas = Canvas(decodeWin, width = 2000, height = 2000)
    canvas.pack()
    CipherTextLabel = Label(decodeWin, fg = "red", text="CypherText:", font=("Ink Free", 40, "italic"))
    keyLabel = Label(decodeWin, fg = "red", text="Key:", font=("Ink Free", 40, "italic"))
    CipherTextEntry = Entry(decodeWin, font=("Arial", 40), width=100)
    keyEntry1 = Entry(decodeWin, font=("Arial", 40, "bold"), width=2)
    keyEntry2 = Entry(decodeWin, font=("Arial", 40, "bold"), width=2)
    keyEntry3 = Entry(decodeWin, font=("Arial", 40, "bold"), width=2)
    keyEntry4 = Entry(decodeWin, font=("Arial", 40, "bold"), width=2)
    calculateBut = Button(decodeWin,bd = 10, bg = "black", fg = "#00ff00", text="CALCULATE", font=("Int Free", 40, "bold"))
    resultLabel = Label(decodeWin, font=("Arial", 40, "bold"))

    CipherTextLabel.place(x=0, y=0)
    CipherTextEntry.place(x=300, y=0)
    keyLabel.place(x=0, y=200)
    canvas.create_line(280, 130, 280, 340, width=10)
    canvas.create_line(480, 130, 480, 340, width=10)
    canvas.create_line(280, 130, 300, 130, width=10)
    canvas.create_line(280, 340, 300, 340, width=10)
    canvas.create_line(480, 130, 460, 130, width=10)
    canvas.create_line(480, 340, 460, 340, width=10)
    keyEntry1.place(x=300, y=150)
    keyEntry2.place(x=400, y=150)
    keyEntry3.place(x=300, y=250)
    keyEntry4.place(x=400, y=250)
    calculateBut.place(x=600, y=400)
    resultLabel.place(x=0, y=600)
    decodeWin.bind("<Return>", decipher)
    calculateBut.bind("<Button-1>", decipher)

if __name__ == "__main__":
    window = Tk()
    window.title("Cipher")
    window.config(bg = "black")
    encodeBut = Button(window, bd = 10, bg = "black", fg = "#00ff00", text = "ENCODE",  font = ("Ink Free", 40, "bold"), command = encode)
    decodeBut = Button(window, bd = 10, bg = "black", fg = "#00ff00", text = "DECODE", font = ("Ink Free", 40, "bold"), command = decode)
    label = Label(window, text = "Vs" ,fg = "red", bg = "black",  font = ("Ink Free", 40, "bold"))
    encodeBut.grid(row = 0, column = 0)
    label.grid(row = 0, column = 1)
    decodeBut.grid(row = 0, column = 2)
    window.mainloop()