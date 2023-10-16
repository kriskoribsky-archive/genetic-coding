import tkinter as tk       #tkinter
from tkinter import font   #tkinter font
import tkinter
import re                  #for text managing (splitting)
import os
from PIL import Image, ImageTk

WIDTH = 700
HEIGHT = 600

#amino-acid lists
fenylalanín = ["UUU", "UUC"]
leucín = ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"]     
isoleucín = ["AUU", "AUC", "AUA"]
methionín = ["AUG"]                                     #start codon
valín = ["GUU", "GUC", "GUA", "GUG"]
serín = ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"]      
prolín = ["CCU", "CCC", "CCA", "CCG"]
treonín = ["ACU", "ACC", "ACA", "ACG"]
alanín = ["GCU", "GCC", "GCA", "GCG"]
tyrozín = ["UAU", "UAC"]
koniec1 = ["UAA", "UAG"]                                #stop codon
histidín = ["CAU", "CAC"]
glutamín = ["CAA", "CAG"]
asparagín = ["AAU", "AAC"]
lyzín = ["AAA", "AAG"]
kys_asparágová = ["GAU", "GAC"]
kys_glutámová = ["GAA", "GAG"]
cysteín = ["UGU", "UGC"]
koniec2 = ["UGA"]                                       #stop codon
tryptofán = ["UGG"]
arginín = ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"]    
glycín = ["GGU", "GGC", "GGA", "GGG"] 



#definitons for conversions
def start_Conversion(entry):

     text_DNA.delete(1.0, tk.END)
     text_RNA.delete(1.0, tk.END)
     text_ANK.delete(1.0, tk.END)
     
     all_list = list(entry)

     if "U" in all_list and "T" in all_list:
          text_DNA.insert(tk.INSERT, "Chyba! Reťazec nesmie obsahovať U a T naraz!")
          text_RNA.insert(tk.INSERT, "Chyba! Reťazec nesmie obsahovať U a T naraz!")
          text_ANK.insert(tk.INSERT, "Chyba! Reťazec nesmie obsahovať U a T naraz!")

     elif "U" in all_list or "A" in all_list or "T" in all_list or "G" in all_list or "C" in all_list:
          to_DNA(entry)
          to_RNA(entry)
          to_ANK(entry)
          
     elif "U" not in all_list and "A" not in all_list and "T" not in all_list and "G" not in all_list and "C" not in all_list:
          to_RNA_from_ANK(entry)

     return


def to_DNA(entry):
     
     conversion = ""
     for i in range (0,len(entry)):
         if entry[i] == "A":
              conversion = conversion + "T"
              
         elif entry[i] == "T":
              conversion = conversion + "A"

         elif entry[i] == "C":
              conversion = conversion + "G"

         elif entry[i] == "G":
              conversion = conversion + "C"

         elif entry[i] == "U":
              conversion = conversion + "A"

         elif entry[i] == "-":
              conversion = conversion + "-"

         elif entry[i] == ".":
              conversion = conversion + "."

         elif entry[i] == " ":
              continue

         elif entry[i] == "\t":
              continue

         elif entry[i].islower():
              continue

         else:
              conversion = ""
              text_DNA.insert(tk.INSERT, "Chyba v zápise vlákien DNA/RNA!")
              text_RNA.insert(tk.INSERT, "Chyba v zápise vlákien DNA/RNA!")
              text_ANK.insert(tk.INSERT, "Chyba v zápise vlákien DNA/RNA!")

              break
     

     text_DNA.insert(tk.INSERT, conversion)
     return
     

def to_RNA(entry):
     
     conversion = ""
     for i in range (0,len(entry)):
         if entry[i] == "A":
              conversion = conversion + "U"
              
         elif entry[i] == "T":
              conversion = conversion + "A"

         elif entry[i] == "C":
              conversion = conversion + "G"

         elif entry[i] == "G":
             conversion = conversion + "C"

         elif entry[i] == "U":
              conversion = conversion + "A"

         elif entry[i] == "-":
              conversion = conversion + "-"

         elif entry[i] == ".":
              conversion = conversion + "."

         elif entry[i] == " ":
              continue

         elif entry[i] == "\t":
              continue

         elif entry[i].islower():
              continue

         else:
              conversion = ""
              break

        
     text_RNA.insert(tk.INSERT, conversion)
     return


def to_RNA_from_ANK(entry):

     conversion = []
     conversion.clear()
     ANK_list = re.split("[-]", entry)
     for i in range(0, len(ANK_list)):
          if ANK_list[i] == "fenylalanín":
               conversion.append("UUU/UUC")

          elif ANK_list[i] == "leucín":
               conversion.append("UUA/UUG/CUU/CUC/CUA/CUG")

          elif ANK_list[i] == "isoleucín":
               conversion.append("AUU/AUC/AUA")

          elif ANK_list[i] == "methionín" or ANK_list[i] == "metionín":
               conversion.append("AUG")

          elif ANK_list[i] == "valín":
               conversion.append("GUU/GUC/GUA/GUG")

          elif ANK_list[i] == "serín":
               conversion.append("UCU/UCC/UCA/UCG/AGU/AGC")

          elif ANK_list[i] == "prolín":
               conversion.append("CCU/CCC/CCA/CCG")

          elif ANK_list[i] == "treonín":
               conversion.append("ACU/ACC/ACA/ACG")

          elif ANK_list[i] == "alanín":
               conversion.append("GCU/GCC/GCA/GCG")

          elif ANK_list[i] == "tyrozín":
               conversion.append("UAU/UAC")

          elif ANK_list[i] == "koniec":
               conversion.append("UAA/UAG/UGA")

          elif ANK_list[i] == "histidín":
               conversion.append("CAU/CAC")

          elif ANK_list[i] == "glutamín":
               conversion.append("CAA/CAG")

          elif ANK_list[i] == "asparagín":
               conversion.append("AAU/AAC")

          elif ANK_list[i] == "lyzín":
               conversion.append("AAA/AAG")

          elif ANK_list[i] == "kys.asparágová":
               conversion.append("GAU/GAC")

          elif ANK_list[i] == "kys.glutámová":
               conversion.append("GAA/GAG")

          elif ANK_list[i] == "cysteín":
               conversion.append("UGU/UGC")

          elif ANK_list[i] == "tryptofán":
               conversion.append("UGG")

          elif ANK_list[i] == "arginín":
               conversion.append("CGU/CGC/CGA/CGG/AGA/AGG")

          elif ANK_list[i] == "glycín":
               conversion.append("GGU/GGC/GGA/GGG")

          else:
               conversion.clear()
               conversion.append("Chyba v zápise aminokyselín!")
               text_DNA.insert(tk.INSERT, "Chyba v zápise aminokyselín!")
               text_ANK.insert(tk.INSERT, "Chyba v zápise aminokyselín!")
               
               break

          
     text_RNA.insert(tk.INSERT, "-".join(conversion))
     return


def to_ANK(entry):

     conversion = []
     conversion.clear()
     codon_list = re.split("[- .]", entry)
     for i in range (0, (len(codon_list))):
          if codon_list[i] in fenylalanín:
               conversion.append("fenylalanín")

          elif codon_list[i] in leucín:
               conversion.append("leucín")

          elif codon_list[i] in isoleucín:
               conversion.append("isoleucín")

          elif codon_list[i] in methionín:
               conversion.append("metionín(začiatok)")

          elif codon_list[i] in valín:
               conversion.append("valín")

          elif codon_list[i] in serín:
               conversion.append("serín")

          elif codon_list[i] in prolín:
               conversion.append("prolín")

          elif codon_list[i] in treonín:
               conversion.append("treonín")

          elif codon_list[i] in alanín:
               conversion.append("alanín")

          elif codon_list[i] in tyrozín:
               conversion.append("tyrozín")

          elif codon_list[i] in koniec1:
               conversion.append("koniec reťazca")

          elif codon_list[i] in histidín:
               conversion.append("histidín")

          elif codon_list[i] in glutamín:
               conversion.append("glutamín")

          elif codon_list[i] in asparagín:
               conversion.append("asparagín")

          elif codon_list[i] in lyzín:
               conversion.append("lyzín")

          elif codon_list[i] in kys_asparágová:
               conversion.append("kys.asparágová")

          elif codon_list[i] in kys_glutámová:
               conversion.append("kys.glutámová")

          elif codon_list[i] in cysteín:
               conversion.append("cysteín")

          elif codon_list[i] in koniec2:
               conversion.append("koniec reťazca")

          elif codon_list[i] in tryptofán:
               conversion.append("tryptofán")

          elif codon_list[i] in arginín:
               conversion.append("arginín")

          elif codon_list[i] in glycín:
               conversion.append("glycín")

          elif "T" in entry:
               conversion.clear()

               break


     text_ANK.insert(tk.INSERT, "-".join(conversion))
     return


#tkinter GUI
window = tk.Tk()
window.resizable(False, False)
window.title("Kódovanie nukleotidov [Kristián Koribský]")

canvas = tk.Canvas(window, height=HEIGHT, width=WIDTH)
canvas.pack()

dir_path = os.path.dirname(os.path.realpath(__file__))

#icon
icon = Image.open(os.path.join(dir_path, "window icon.png"))
icon.thumbnail((16, 16))
icon = ImageTk.PhotoImage(icon)
window.iconphoto(False, icon)




background_image = tk.PhotoImage(file=os.path.join(dir_path, "background_image 1.png"))
background_label = tk.Label(window, image=background_image)
background_label.place(relwidth=1, relheight=1)

#first frame (instructions/enter values/button)
entry_frame = tk.Frame(window, bg="#a4b897")
entry_frame.place(relx=0.5, rely=0.1, relwidth=0.7, relheight=0.15, anchor="c", )

instructions = tk.Label(entry_frame, bg="#e6d4aa", text="Poradie nukleotidov v jednom vlákne DNA/RNA alebo poradie ANK:", font=("Arial Rounded MT Bold", 10), anchor="w")
instructions.place(relx=0.01, rely=0.1, relwidth=0.98, relheight=0.37, anchor="nw")

entry = tk.Entry(entry_frame, bg="#e6d4aa", font=("Corbel", 12))
entry.place(relx=0.01, rely=0.9, relwidth=0.75, relheight=0.37, anchor="sw")

button = tk.Button(entry_frame, bg="#e6d4aa", text="Genetický prepis", font=("Arial Rounded MT Bold", 9), command=lambda: start_Conversion(entry.get()))
button.place(relx=0.99, rely=0.9, relwidth=0.22, relheight=0.37, anchor="se")

#second frame (DNA conversion output)
second_frame = tk.Frame(window, bg="#a4b897")
second_frame.place(relx=0.5, rely=0.3, relwidth=0.7, relheight=0.1, anchor="c")

label_DNA = tk.Label(second_frame, bg="#e6d4aa", text="Komplementárna časť druhého vlákna: (DNA)", font=("Arial Rounded MT Bold", 10))
label_DNA.place(relx=0.5, rely=0.3, relwidth=0.7, relheight=0.38, anchor="c")

text_DNA = tk.Text(second_frame, bg="#e6d4aa", font=("Corbel", 12))
text_DNA.place(relx=0.5, rely=0.7, relwidth=0.98, relheight=0.38, anchor="c")

#third frame (RNA conversion output)
third_frame = tk.Frame(window, bg="#a4b897")
third_frame.place(relx=0.5, rely=0.5, relwidth=0.7, relheight=0.1, anchor="c")

label_RNA = tk.Label(third_frame, bg="#e6d4aa", text="Komplementárna časť druhého vlákna: (RNA)", font=("Arial Rounded MT Bold", 10))
label_RNA.place(relx=0.5, rely=0.3, relwidth=0.7, relheight=0.38, anchor="c")

text_RNA = tk.Text(third_frame, bg="#e6d4aa", font=("Corbel", 12))
text_RNA.place(relx=0.5, rely=0.7, relwidth=0.98, relheight=0.38, anchor="c")

#fourth frame (ANK conversion output)
fourth_frame = tk.Frame(window, bg="#a4b897")
fourth_frame.place(relx=0.5, rely=0.7, relwidth=0.7, relheight=0.1, anchor="c")

label_ANK = tk.Label(fourth_frame, bg="#e6d4aa", text="Komplementárna časť druhého vlákna: (ANK)", font=("Arial Rounded MT Bold", 10))
label_ANK.place(relx=0.5, rely=0.3, relwidth=0.7, relheight=0.38, anchor="c")

text_ANK = tk.Text(fourth_frame, bg="#e6d4aa", font=("Corbel", 12))
text_ANK.place(relx=0.5, rely=0.7, relwidth=0.98, relheight=0.38, anchor="c")

#fifth frame (example)
fifth_frame = tk.Frame(window, bg="#a4b897")
fifth_frame.place(relx=0.35, rely=0.87, relwidth=0.4, relheight=0.14, anchor="c")

example_DNA = tk.Label(fifth_frame, bg="#e6d4aa", text=("Vzor(DNA): ...TCA-TGG-CTA-TGA-GCT-AAT-GCG..."), font=("Calibri Light", 10), anchor="w")
example_DNA.place(relx=0.5, rely=0.2, relwidth=0.95, relheight=0.31, anchor="c")

example_RNA = tk.Label(fifth_frame, bg="#e6d4aa", text=("Vzor(RNA): ...CAC-CGT-ACA-GAA-TCG-CTT-ATT..."), font=("Calibri Light", 10), anchor="w")
example_RNA.place(relx=0.5, rely=0.5, relwidth=0.95, relheight=0.31, anchor="c")

example_ANK = tk.Label(fifth_frame, bg="#e6d4aa", text=("Vzor(ANK): methionín-kys.asparágová-lyzín-koniec"), font=("Calibri Light", 10), anchor="w")
example_ANK.place(relx=0.5, rely=0.8, relwidth=0.95, relheight=0.31, anchor="c")

window.mainloop()
