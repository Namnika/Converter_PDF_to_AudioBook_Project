from tkinter import *
from tkinter.filedialog import askopenfilename
import PyPDF2
import pdfplumber
import pyttsx3 as tts

win = Tk()
win.geometry('400x200')
win.title('PDF to Audiobook')


def upload_file():
    file = askopenfilename()
    f = open(file, "rb")
    pdf_reader = PyPDF2.PdfFileReader(f)
    pages = pdf_reader.pages
    text = ""

    with pdfplumber.open(file) as pdf:
        for i in range(len(pages)):
            page = pdf.pages[i]
            text += page.extract_text()

        engine = tts.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voices', voices[0].id)
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 1.0)
        engine.save_to_file(text, 'Audiobook.mp3')
        engine.runAndWait()
        info_label = Label(text='DOWNLOADED', font=('Arial', 15))
        info_label.pack(pady=20)


title_label = Label(text="Choose any pdf file to convert", font=('Arial', 15))
title_label.pack(pady=10)

upload_file_button = Button(text='upload file', font=('Arial', 15), command=upload_file)
upload_file_button.pack(pady=10)

win.mainloop()
