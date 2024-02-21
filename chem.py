from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image, ImageEnhance, ImageDraw
import string
      
window=Tk()

window.title('Organic Chemistry Product Predictor')
window.geometry("1200x800+10+20")          

compounds = [
    "./compounds/ketone.png",
    "./compounds/cyclohexene.png",
    "./compounds/-ene.png",
    "./compounds/pentene.png",
    "./compounds/benzaldehyde.png",
    "./compounds/nitrobenzene.png",
    "./compounds/ethene.png",
    "./compounds/cyclohexane.png",
    "./compounds/vertical-line.png"
]

reagents = [
    "./reagents/bromination.png",
    "./reagents/ch3cocl.png",
    "./reagents/grignard.png",
    "./reagents/hydrogenation.png",
    "./reagents/lialh4.png",
    "./reagents/oso4.png",
    "./reagents/ozonolysis.png",
    "./reagents/THF.png",
    "./reagents/kmno4.png"
]

products = []

selected_compound = 0
selected_reagents = 0

def highlight_compounds (self, index):
    global selected_compound 
    selected_compound = index
    show_product()
    self.config(borderwidth=3, command=lambda:unhighlight_compounds(self, index))
def unhighlight_compounds (self, index):
    global selected_compound
    selected_compound = 0
    self.config(borderwidth=0, command=lambda:highlight_compounds(self, index))

def highlight_reagents (self, index):
    global selected_reagents
    selected_reagents = index
    show_product()
    self.config(borderwidth=3, command=lambda:unhighlight_reagents(self, index))
def unhighlight_reagents (self, index):
    global selected_reagents
    selected_reagents = 0
    self.config(borderwidth=0, command=lambda:highlight_reagents(self, index))

def show_product ():
    global products, window, btnproduct, imgproduct
    if selected_compound == 0 or selected_reagents == 0:
        return
    productimage = Image.open(f'./products/{selected_compound}_{selected_reagents}.png')
    resized_productimage = productimage.resize((600,200), Image.ADAPTIVE)
    imgproduct = ImageTk.PhotoImage(resized_productimage)
    btnproduct = tk.Button(window, image=imgproduct)
    btnproduct.place(x=300, y=550)

# Creating image for ketone thing
ketoneimage = Image.open(compounds[0])
resized_image1= ketoneimage.resize((200,100), Image.ADAPTIVE)
img1 = ImageTk.PhotoImage(resized_image1)

btn1 = tk.Button(window, width=200, height=100, image=img1, borderwidth=0, highlightthickness=0, highlightbackground = 'red', 
                command=lambda:highlight_compounds(btn1, 1))
btn1.place(x=10, y=35)

#Creating image for cyclohexene

hexeneimage = Image.open(compounds[1])
resized_image2= hexeneimage.resize((105,105), Image.ADAPTIVE)
img2 = ImageTk.PhotoImage(resized_image2)

btn2 = tk.Button(window, width=105, height=105, image=img2, borderwidth=0, highlightthickness=0, highlightbackground = 'red',
                 command=lambda:highlight_compounds(btn2, 2))
btn2.place(x=230, y=30)

#Creating image for two double bond thing
eneimage = Image.open(compounds[2])
resized_image3= eneimage.resize((220,40), Image.ADAPTIVE)
img3 = ImageTk.PhotoImage(resized_image3)

btn3 = tk.Button(window, width=220, height=40, image=img3, borderwidth=0, highlightthickness=0, highlightbackground = 'red', 
                 command=lambda:highlight_compounds(btn3, 3))
btn3.place(x=350, y=60)

#Creating image for pentene
penteneimage = Image.open(compounds[3])
resized_image4= penteneimage.resize((200,75), Image.ADAPTIVE)
img4 = ImageTk.PhotoImage(resized_image4)

btn4 = tk.Button(window, width=200, height=75, image=img4, borderwidth=0, highlightthickness=0, highlightbackground = 'red', 
                 command=lambda:highlight_compounds(btn4, 4))
btn4.place(x=100, y=200)

#Creating image for benzaldehyde
benzaldehydeimage = Image.open(compounds[4])
resized_image5= benzaldehydeimage.resize((175,116), Image.ADAPTIVE)
img5 = ImageTk.PhotoImage(resized_image5)

btn5 = tk.Button(window, width=175, height=116, image=img5, borderwidth=0, highlightthickness=0, highlightbackground = 'red', 
                 command=lambda:highlight_compounds(btn5, 5))
btn5.place(x=350, y=200)

#Creating image for nitrobenzene
nitrobenzeneimage = Image.open(compounds[5])
resized_image6= nitrobenzeneimage.resize((116,175), Image.ADAPTIVE)
img6 = ImageTk.PhotoImage(resized_image6)

btn6 = tk.Button(window, width=116, height=175, image=img6, borderwidth=0, highlightthickness=0, highlightbackground = 'red', 
                 command=lambda:highlight_compounds(btn6, 6))
btn6.place(x=15, y=350)

#Creating image for ethene
etheneimage = Image.open(compounds[6])
resized_image7= etheneimage.resize((175,100), Image.ADAPTIVE)
img7 = ImageTk.PhotoImage(resized_image7)

btn7 = tk.Button(window, width=200, height=114, image=img7, borderwidth=0, highlightthickness=0, highlightbackground = 'red', 
                 command=lambda:highlight_compounds(btn7, 7))
btn7.place(x=150, y=375)

#Creating image for cyclohexane thing
cyclohexaneimage = Image.open(compounds[7])
resized_image8= cyclohexaneimage.resize((200,200), Image.ADAPTIVE)
img8 = ImageTk.PhotoImage(resized_image8)

btn8 = tk.Button(window, width=200, height=150, image=img8, borderwidth=0, highlightthickness=0, highlightbackground = 'red', 
                 command=lambda:highlight_compounds(btn8, 8))
btn8.place(x=375, y=360)

#Creating a line
frame9 = Frame(window, width=10, height=5)
frame9.pack()
frame9.place(anchor='center', x='600', y='280')

lineimage = Image.open(compounds[8])
resized_image9= lineimage.resize((10,500), Image.ADAPTIVE)
img9 = ImageTk.PhotoImage(resized_image9)

label9 = Label(frame9, image = img9)
label9.pack()

#####################################################################################################################################

#Creating bromination reagent
brominationimage = Image.open(reagents[0])
resized_image10= brominationimage.resize((150,150), Image.ADAPTIVE)
img10 = ImageTk.PhotoImage(resized_image10)

btn10 = tk.Button(window, width=150, height=150, image=img10, borderwidth=0, highlightthickness=0, highlightbackground = 'red', 
                 command=lambda:highlight_reagents(btn10, 1))
btn10.place(x=625, y=15)

#Creating ch3cocl reagent
ch3coclimage = Image.open(reagents[1])
resized_image11= ch3coclimage.resize((150,150), Image.ADAPTIVE)
img11 = ImageTk.PhotoImage(resized_image11)

btn11 = tk.Button(window, width=150, height=150, image=img11, borderwidth=0, highlightthickness=0, highlightbackground = 'red', 
                 command=lambda:highlight_reagents(btn11, 2))
btn11.place(x=825, y=15)

#Creating grignard reagent
grignardimage = Image.open(reagents[2])
resized_image12= grignardimage.resize((150,150), Image.ADAPTIVE)
img12 = ImageTk.PhotoImage(resized_image12)

btn12 = tk.Button(window, width=150, height=150, image=img12, borderwidth=0, highlightthickness=0, highlightbackground = 'red', 
                 command=lambda:highlight_reagents(btn12, 3))
btn12.place(x=1025, y=15)

#Creating hydrogenation reagent
hydrogenationimage = Image.open(reagents[3])
resized_image13= hydrogenationimage.resize((150,150), Image.ADAPTIVE)
img13 = ImageTk.PhotoImage(resized_image13)

btn13 = tk.Button(window, width=150, height=150, image=img13, borderwidth=0, highlightthickness=0, highlightbackground = 'red', 
                 command=lambda:highlight_reagents(btn13, 4))
btn13.place(x=625, y=175)

#Creating lialh4 reagent
lialh4image = Image.open(reagents[4])
resized_image14= lialh4image.resize((150,150), Image.ADAPTIVE)
img14 = ImageTk.PhotoImage(resized_image14)

btn14 = tk.Button(window, width=150, height=150, image=img14, borderwidth=0, highlightthickness=0, highlightbackground = 'red', 
                 command=lambda:highlight_reagents(btn14, 5))
btn14.place(x=825, y=175)

#Creating oso4 reagent
oso4image = Image.open(reagents[5])
resized_image15= oso4image.resize((150,150), Image.ADAPTIVE)
img15 = ImageTk.PhotoImage(resized_image15)

btn15 = tk.Button(window, width=150, height=150, image=img15, borderwidth=0, highlightthickness=0, highlightbackground = 'red', 
                 command=lambda:highlight_reagents(btn15, 6))
btn15.place(x=1025, y=175)

#Creating ozonolysis reagent
ozonolysisimage = Image.open(reagents[6])
resized_image16= ozonolysisimage.resize((150,150), Image.ADAPTIVE)
img16 = ImageTk.PhotoImage(resized_image16)

btn16 = tk.Button(window, width=150, height=150, image=img16, borderwidth=0, highlightthickness=0, highlightbackground = 'red', 
                 command=lambda:highlight_reagents(btn16, 7))
btn16.place(x=625, y=335)

#Creating thf reagent
thfimage = Image.open(reagents[7])
resized_image17= thfimage.resize((150,150), Image.ADAPTIVE)
img17 = ImageTk.PhotoImage(resized_image17)

btn17 = tk.Button(window, width=150, height=150, image=img17, borderwidth=0, highlightthickness=0, highlightbackground = 'red', 
                 command=lambda:highlight_reagents(btn17, 8))
btn17.place(x=825, y=335)

#Creating kmno4 reagent
kmno4image = Image.open(reagents[8])
resized_image18 = kmno4image.resize((150,150), Image.ADAPTIVE)
img18 = ImageTk.PhotoImage(resized_image18)

btn18 = tk.Button(window, width=150, height=150, image=img18, borderwidth=0, highlightthickness=0, highlightbackground = 'red', 
                 command=lambda:highlight_reagents(btn18, 9))
btn18.place(x=1025, y=335)

window.mainloop() 