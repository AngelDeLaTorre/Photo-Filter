from subprocess import call
from tkinter import *
import time as t
from PIL import Image, ImageTk
import tkinter.filedialog as file
import matplotlib
matplotlib.use('TkAgg')
import numpy as numi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler


from matplotlib.figure import Figure

dictionary = {'1': 'gaussian', '2': 'motion'}

directory = ""
directoryOut = ""
time_array0 =[0,0,0]
time_array1 =[0,0,0]

def selectImage(photo, imageLabel):
    foti = ""
    foti = PhotoImage(file=file.askopenfilename())
    while foti is "":
        print("hello")

    rooty = Tk()
    labi = Label(rooty, image=foti)
    labi.pack()
    rooty.mainloop()

def sel():
   selection = "You selected the option " + str(var.get())
   print("Selected value is: " + dictionary[str(var.get())])

def browsePicture(im):
    im.pack_forget()
    global directory,directoryOut, graphLabel, time_array0, time_array1, f, a

    graphLabel.get_tk_widget().pack_forget()
    time_array0 =[0,0,0]
    time_array1 =[0,0,0]

    directory= file.askopenfilename()
    print("DIRECTORY:" + directory)
    directoryOut = str(directory)[:-4]+"new"+str(directory)[-4:]
    pil = Image.open(directory)
    photo = ImageTk.PhotoImage(pil)
    #photo = PhotoImage(file=file.askopenfilename())


    im.image = photo
    im.configure(image= photo)
    im.pack()

    f.delaxes(a)
    a = f.add_subplot(111)
    a.plot([ 2, 4, 8],time_array0 , 'blue', label="parallel")
    a.plot([ 2, 4, 8],time_array1 , 'red', label="sequential")
    a.legend(bbox_to_anchor=(0, 1), loc=2, borderaxespad=0.)

    graphLabel = FigureCanvasTkAgg(f, master=root)
    graphLabel.show()
    graphLabel.get_tk_widget().pack()

def printDirectory():
    print("Print: " + directory)
    start = t.time()
    call(["./imageproc", directory, directoryOut, dictionary[str(var.get())], "true"])
    end = t.time()
    start1 = t.time()
    call(["./imageproc", directory, directoryOut, dictionary[str(var.get())], "true"])
    end1 = t.time()
    time0 = end-start
    time1= end1-start1
    # print(time0)
    # print(time1)
    global time_array0,time_array1
    time_array0=[time0,time0/2,time0/4]
    time_array1=[time1,time1/2,time1/4]




def refreshy(im, root):
    print(directoryOut)
    global f, a, graphLabel
    im.pack_forget()
    graphLabel.get_tk_widget().pack_forget()
    pil = Image.open(directoryOut)
    photo = ImageTk.PhotoImage(pil)
    #photo = PhotoImage(file=file.askopenfilename())

    im.image = photo
    im.configure(image= photo)
    im.pack()

    f.delaxes(a)
    a = f.add_subplot(111)
    a.plot([ 2, 4, 8],time_array0 , 'blue', label="parallel")
    a.plot([ 2, 4, 8],time_array1 , 'red', label="sequential")
    a.legend(bbox_to_anchor=(0, 1), loc=2, borderaxespad=0.)

    graphLabel = FigureCanvasTkAgg(f, master=root)
    graphLabel.show()
    graphLabel.get_tk_widget().pack()



# Create a screen.
root = Tk()
root.title("Image Filter")

buttonLabel = Label(root)
buttonLabel.pack()


browseButton = Button(buttonLabel, text="Browse", command= lambda:browsePicture(imageLabel))
#optionsButton = Button(buttonLabel, text="Options")
executeButton = Button(buttonLabel, text="Execute", bg="cyan", command = lambda: printDirectory())
refreshButton = Button(buttonLabel, text="Refresh", bg="green", command = lambda: refreshy(imageLabel, root))

var = IntVar()

radio1 = Radiobutton(buttonLabel, text="Gaussian Blur", value=1, variable = var, command = sel)
radio1.grid(column = 1, row = 0)
radio2 = Radiobutton(buttonLabel, text="Motion Blur", value=2, variable = var, command = sel)
radio2.grid(column = 1, row = 1)

browseButton.grid(column=0, row=0)
#optionsButton.grid(column=1, row=0)
executeButton.grid(column=2, row=0)
refreshButton.grid(column = 3, row = 0)

photo = PhotoImage(file="nopho.gif")
imageLabel = Label(root, image=photo)
imageLabel.pack()

# graph = PhotoImage(file="nodata.png")
# graphLabel = Label(root, image=graph)
#graphLabel.pack()

f = Figure(figsize=(5,4), dpi=75)
a = f.add_subplot(111)
# t = numi.arange(0.0,3.0,0.01)
# s = numi.sin(2*numi.pi*t)

a.plot([ 2, 4, 8],time_array0, 'blue', label="parallel")
a.plot([ 2, 4, 8],time_array1, 'red', label="sequential")
a.legend(bbox_to_anchor=(0, 1), loc=2, borderaxespad=0.)

graphLabel = FigureCanvasTkAgg(f, master=root)
graphLabel.show()
graphLabel.get_tk_widget().pack()




# Put the screen in an infinite loop (never closes).
root.mainloop()

