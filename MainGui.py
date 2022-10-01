import PIL.Image
import PIL.ImageTk
import matplotlib
from PIL import Image
from PIL import ImageTk
import tkinter.font as font
from instabot import Bot

import funcs

matplotlib.use( "TkAgg" )

global imageDisplay1
global second_image

import PIL.Image, PIL.ImageTk

import tkinter as tk
from tkinter import *
from tkinter import filedialog

maintk = tk.Tk()
maintk.title( "Space Apps Challenge 2022" )
maintk.geometry( "800x600" )
maintk.configure( background='#001e35' )
bgcolor = "#001e35";
button_font = "Helvetica 10 bold"


import tkinter as tk
from tkinter import ttk

import tkinter as tk
import tkinter.font as font
from tkinter import filedialog
from tkinter import ttk
import matplotlib
from PIL import Image, ImageTk
import PIL.Image, PIL.ImageTk

matplotlib.use( "TkAgg" )
import funcs

global imageDisplay1
global second_image
import cv2 as cv

import tkinter as tk
import tkinter.font as font
from tkinter import *
from tkinter import filedialog

import matplotlib
import matplotlib.image as img
import numpy as np
from PIL import Image, ImageTk

matplotlib.use( "TkAgg" )
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from matplotlib.figure import Figure
import funcs

global imageDisplay1
global second_image


class CustomScale( ttk.Scale ):
    def __init__(self, master=None, **kw):
        kw.setdefault( "orient", "horizontal" )
        self.variable = kw.pop( 'variable', tk.DoubleVar( master ) )
        ttk.Scale.__init__( self, master, variable=self.variable, **kw )
        self._style_name = '{}.custom.{}.TScale'.format( self, kw[
            'orient'].capitalize() )  # unique style name to handle the text
        self['style'] = self._style_name

trough = b'iVBORw0KGgoAAAANSUhEUgAAAH4AAAAmCAYAAAF1+R+EAAAACXBIWXMAAC4jAAAuIwF4pT92AAABrklEQVR42u2avUrDUBzFT0JeILMiZgoK4tQPaAf7AD6Ag28QqVvddNRN0QcQBTtJQZ2lxQ7VzS1ZklLaNRH7ANep2mqlNIGmuff8IBBCwj/nnJv7kUQTQiAJOhJiAIAXROLq4mzui51qraKlLkFbDhMPDo9i3cbl+akmgYlJ0ZEyxmjHCyKxv7e7sMK39ceKbZlNRpCqA7qy1utL8dg9v7yLxn19IUWdag22ZWrfxd86bbx22gsrztauZvHU+3ilxxeKT7uTH59jSa65YltmEwAghJjYXD8UAKTcnGpNuH64M9JqTLPG9UMlmj17e4pXEDZ7iqd4iqd4iufCRi5sy9T+FQ8Acb4jLTv5Qgn5Ynny4O9V3c3dg7SrOtcPxbjWP8nni2XkCiXpkt/Y3Jo9vVXpmefcnuIpnuIpnuIlR+mhjq2eMHjC4AmDJwyeSIEx6wQviE5oU6a5ti2zO3fwAI7pXaZpAogVPAAgt72O4fCTNmaExlNr6geaucb4Qb/H0DPGoN9LNsYDwMrqmjI/onJy90OLNmWaj2kH+a6e63jC4AmDJwyeMHjC4Ekm+QLnzR2vM7KDdAAAAABJRU5ErkJggg=='
slider = b'iVBORw0KGgoAAAANSUhEUgAAADIAAAAxCAYAAAHvrMqJAAAACXBIWXMAAC4jAAAuIwF4pT92AAADcElEQVRo3u2YSUxTQRjH/99rgSYtSHEJoLS2QlVssZhqRaltVFokKmhIrNGAEg8qRIMLqDHBk1FUbgLe0Kg0uKAmrokHiQtipG54UCOrvShKNEJbwfFgYtzAQlqpOJO8w3vz/vOf33zzvZl5xBhDf0XAAMX3yryC4h89GGPfLgCW7+9pyB3qVykMurlvFRu2lrBbFatYADwGBB3SAAxKRET6DVtL2P7Sg8xn0Yq1m5wAkJ2dPcxMg3YSAt6tYRJk5+az12/eMiKK/KOAiNbMGvMMBw+UYtv2ond/FDDGqpoxB4syMpC5bPmv9t/n7k95rf/d85EQuCFN87+SFtzE55KcnJxHRPqABN6et5nJ5V/zMd1sgMNRjU2btyDFaCC/kBBRllweicmiOgDA5UuXkDPzM2rPnPIvCRFlZdrX1cbExsI2z4BXLhcKNq6XM8a6eJ78eyY8JtyEm/yrJjabrSRgGW+2Zn3SJGrFk+LGwbrAgrKyQ+3Hjx1V+I1ElZD4JFE3XdzR8gL6JB0OlO6DTCqNU6nVG33Ri315STcjZZqIuUFEePDoMdIXWOD2eDBNpzsMoNwvJoJIhBdN9ej88HU5F4kEeD8L6O7+6L/AP7x3syksUgVDihkAcP3GbdjtK1FZWZ7vN5Pm50+1rlcd3t6+Prh7erDQakXhlsL25pcvy31C6e8AMMDBwDJYDV+0uAk3CZLN3YgZLQ7CQTgIB+EgIxZEHIhGiShSodY44lSa+bLwiBCNajzSrWlobLzvPXP6VMUDZ+MeX36PDdvKTkR608KlTqU6ATKZFF6PG6FhEihjR2O2QY9qRw3mpppw4fxZhIaEtJ08cVwZdFOLiPRpS+zOqdokvO96AwAIDZMAACRhEmi1OhDrQ9MjJ8ZERWHnrt2K1Tm5bUEXEaPRWBs+dmJWdEw0oj/VY3WGBruqeyENj4A6Lgas143l8S4YZ47FuWutuNMZj1STGUsXL6KgikhDQ0OhIAiQyiLwTmbBkbtqKNUaeD0eyKOiUFRUjKr7UuyoDkF9ZzxycteipsbRHrQ5Mi8t855CFS+WyaRwdbQidoISERJCR1sz5sw14dqViygq3on9+/a2XDh/ThXU23gimqhQayonKBNs4aNGIWnKJFjMJly9crmrru7G0aD/avEFkYNwEA7CQf47kC+LIql+SPOngAAAAABJRU5ErkJggg=='

img_trough = tk.PhotoImage( master=maintk, data=trough )
img_slider = tk.PhotoImage( master=maintk, data=slider )
style = ttk.Style( maintk )
# create scale elements
style.element_create( 'custom.Scale.trough', 'image', img_trough )
style.element_create( 'custom.Scale.slider', 'image', img_slider )
# create custom layout
style.layout( 'custom.Horizontal.TScale',
              [('custom.Scale.trough', {'sticky': 'ew'}),
               ('custom.Scale.slider',
                {'side': 'left', 'sticky': '',
                 'children': [('custom.Horizontal.Scale.label', {'sticky': ''})]
                 })] )

toggler_color = '#EBF1FF'

image1 = PIL.Image.open( "D:\Projects\Space Apps\photos\minimizig trial.png" )
test = ImageTk.PhotoImage( image1 )

label1 = Label( image=test, borderwidth=0, highlightthickness=0, bg='#001e35' )
label1.image = test
label1.place( x=250, y=500 )

def light_choices(light_Thtottle):
    global cvim
    value = int( light_Thtottle )
    print( "this is value", value )
    prevoius = cvim
    cvim = funcs.brightness( cvim, original, value )
    printlabel( cvim )

def multiply_choice(multiply_Thtottle):
    global cvim
    value = int( multiply_Thtottle )
    previous = cvim
    cvim = funcs.arthmultiply( cvim, value )
    printlabel( cvim )
def divsion_choice(divsion_Thtottle):
    global cvim
    value = int( divsion_Thtottle )
    previous = cvim
    cvim = funcs.arthdivison( cvim, value )
    printlabel( cvim )

def onclickhisto():
    global histo_toggle
    global light_Thtottle

    histo_toggle = Frame( maintk, width=210, height=200, bg=toggler_color )
    histo_toggle.place( x=20, y=0 )

    def getlight_Thtottle(event):
        light_choices( light_Thtottle.get() )




    brightness_label = tk.Label( histo_toggle, text="brightness", bg=toggler_color, fg=bgcolor,font=button_font )
    brightness_label.place( x=10, y=8 )
    light_Thtottle = CustomScale( histo_toggle, from_=0, to=10, command=getlight_Thtottle )
    light_Thtottle.set( 0 )
    light_Thtottle.place( x=10, y=25 )

    def getmultiply_Throttle(event):
        multiply_choice( multiply_Throttle.get() )


    multiply_label = tk.Label( histo_toggle, text="multiply", bg=toggler_color, fg=bgcolor,font=button_font )
    multiply_label.place( x=10, y=60 )
    multiply_Throttle = CustomScale( histo_toggle, from_=0, to=10, command= getmultiply_Throttle )
    multiply_Throttle.set( 0 )
    multiply_Throttle.place( x=10, y=85)

    def getdivsion_Throttle(event):
        divsion_choice( divsion_Throttle.get() )
    #divison label
    divsion_label = tk.Label( histo_toggle, text="divsion", bg=toggler_color, fg=bgcolor,font=button_font )
    divsion_label.place( x=10, y=120 )
    divsion_Throttle = CustomScale( histo_toggle, from_=1, to=3, command= getdivsion_Throttle )
    divsion_Throttle.set( 0 )
    divsion_Throttle.place( x=10, y=145 )


def get_equal(cvim):
    cvim = funcs.histogram_equalization( cvim )
    printlabel( cvim )

def on_clickequalization():
    global equal_toggle
    global cvim
    equal_toggle = Frame( maintk, width=210, height=500, bg=bgcolor )
    equal_toggle.place( x=20, y=0 )
    histogram_equalization = tk.Button( equal_toggle, width=20, text="histogram equalization", height=2,
                                        highlightthickness=0, borderwidth=0, foreground=bgcolor, background=bgcolor, command=get_equal( cvim ) )
    histogram_equalization.place( x=10, y=20 )

def mean_filter():
    global cvim
    cvim = funcs.bilateral( cvim )
    printlabel( cvim )

def median_filter():
    global cvim
    cvim = funcs.median_filter( cvim )
    printlabel( cvim )
def average_filter():
    global cvim
    cvim = funcs.average_filter( cvim )
    printlabel( cvim )

def gaussian_filter():
    global cvim
    cvim = funcs.gaussian_filter( cvim )
    printlabel( cvim )

def onclick_filters():
    global cvim
    filters_toggler = Frame( maintk, width=210, height=150, bg=toggler_color )
    filters_toggler.place( x=20, y=0 )
    median = tk.Button( filters_toggler, width=15, text="median filter", height=2,
                                        highlightthickness=0, borderwidth=0, foreground=bgcolor, background=toggler_color,
                                        command=median_filter(),font=button_font )
    median.place( x=10, y=20 )
    bilateral = tk.Button( filters_toggler, width=15, text="bilateral filter", height=2, highlightthickness=0, borderwidth=0, foreground=bgcolor, background=toggler_color,
                                        command=mean_filter(),font=button_font )
    bilateral.place( x=10, y=50)
    average = tk.Button( filters_toggler, width=15, text="average filter", height=2, highlightthickness=0, borderwidth=0, foreground=bgcolor, background=toggler_color,
                                        command=average_filter(),font=button_font )
    average.place( x=10, y=80)
    gaussian = tk.Button( filters_toggler, width=15, text="gaussian filter", height=2, highlightthickness=0, borderwidth=0, foreground=bgcolor, background=toggler_color,
                                        command=gaussian_filter(),font=button_font )
    gaussian.place( x=10, y=110)

#
def thresh1():
    global cvim
    cvim = funcs.image_negative( cvim )
    printlabel( cvim )

def sharpner():
    global cvim
    cvim = funcs.sharpening( cvim )
    printlabel( cvim )

def onclick_thresh():
    global cvim
    thresh_toggler = Frame( maintk, width=210, height=100, bg=toggler_color )
    thresh_toggler.place( x=20, y=0 )
    threshone = tk.Button( thresh_toggler, width=15, text="Negative", height=2,
                                        highlightthickness=0, borderwidth=0, foreground=bgcolor, background=toggler_color,
                                        command=thresh1(),font=button_font )
    threshone.place( x=10, y=20 )
    sharpne = tk.Button( thresh_toggler, width=15, text="sharpner", height=2, highlightthickness=0, borderwidth=0, foreground=bgcolor, background=toggler_color,
                                        command=sharpner(),font=button_font )
    sharpne.place( x=10, y=50)


def onclick_guide():
    global cvim
    guide_toggler = Frame( maintk, width=210, height=230, bg=toggler_color )
    guide_toggler.place( x=20, y=0 )
    #text box to show one line of text
    text = Text(guide_toggler, height=5, width=20)
    label1 = Label(guide_toggler, text="Click on the image to select it")
    label2 = Label(guide_toggler, text="Choose a moon to apply the filter")
    label3 = Label(guide_toggler, text="first moon (light enhancments)")
    label4 = Label(guide_toggler, text="second moon (contrast)")
    label5 = Label(guide_toggler, text="third moon (color)")
    label6 = Label(guide_toggler, text="fourth moon (Guide)")
    label7 = Label(guide_toggler, text="fifth moon (blurring filters)")
    label8 = Label(guide_toggler, text="sixth moon (sharpening filters)")
    label9 = Label(guide_toggler, text="seventh moon (negative )")
    label1.place(x=10, y=20)
    label2.place(x=10, y=40)
    label3.place(x=10, y=60)
    label4.place(x=10, y=80)
    label5.place(x=10, y=100)
    label6.place(x=10, y=120)
    label7.place(x=10, y=140)
    label8.place(x=10, y=160)
    label9.place(x=10, y=180)




from PIL import Image as Img
from PIL import ImageTk
canvas2 = Canvas( maintk, width="370", height="365", bd=2, highlightthickness=2 )
canvas2.configure( bg=bgcolor )
canvas2.place( x=700, y=20 )
def printlabel(image):
    res = cv.resize( image, dsize=(370, 370), interpolation=cv.INTER_CUBIC )
    im = Img.fromarray( res )
    # im = PIL.Image.open(image)
    ph = ImageTk.PhotoImage( im )
    canvas2.create_image( 190, 190, image=ph )
    canvas2.image = ph
#

#



moon_image = PhotoImage( file="D:\Projects\Space Apps\photos/icon1.png" )
filters_btn = tk.Button( maintk, background=bgcolor, highlightthickness=0, bd=0, width=90, height=90, borderwidth=0,
                         command=onclickhisto, image=moon_image )
filters_btn.place( x=180, y=570 )

moon2 = PhotoImage( file="D:\Projects\Space Apps\photos/icon2.png" )
filters_btn2 = tk.Button( maintk, background=bgcolor, highlightthickness=0, bd=0, width=90, height=90, borderwidth=0,
                          command=on_clickequalization, image=moon2 )
filters_btn2.place( x=290, y=490 )
moon3 = PhotoImage( file="D:\Projects\Space Apps\photos/icon3.png" )
filters_btn3 = tk.Button( maintk, background=bgcolor, highlightthickness=0, bd=0, width=90, height=90, borderwidth=0,
                          command=onclick_filters, image=moon3 )
filters_btn3.place( x=440, y=430 )
moon4 = PhotoImage( file="D:\Projects\Space Apps\photos/icon4.png" )
filters_btn4 = tk.Button( maintk, background=bgcolor, highlightthickness=0, bd=0, width=90, height=90, borderwidth=0,
                          command=onclick_guide(), image=moon4 )
filters_btn4.place( x=610, y=410 )
moon5 = PhotoImage( file="D:\Projects\Space Apps\photos/icon5.png" )
filters_btn5 = tk.Button( maintk, background=bgcolor, highlightthickness=0, bd=0, width=90, height=90, borderwidth=0,
                          command=onclickhisto, image=moon5 )
filters_btn5.place( x=820, y=430 )

moon6 = PhotoImage( file="D:\Projects\Space Apps\photos/icon6.png" )
filters_btn6 = tk.Button( maintk, background=bgcolor, highlightthickness=0, bd=0, width=90, height=90, borderwidth=0,
                          command=onclickhisto, image=moon6 )
filters_btn6.place( x=970, y=500 )

moon7 = PhotoImage( file="D:\Projects\Space Apps\photos/icon7.png" )
filters_btn7 = tk.Button( maintk, background=bgcolor, highlightthickness=0, bd=0, width=90, height=90, borderwidth=0,
                          command=onclick_thresh, image=moon7 )
filters_btn7.place( x=1090, y=590 )

uploadicon= PhotoImage( file="D:\Projects\Space Apps\photos\iconn.png" )
uploadfirst = tk.Button( maintk,  width=150,height=30, bg=bgcolor,borderwidth=0, command=lambda: selected(),image=uploadicon )
uploadfirst.place( x=1160, y=50 )

sharingicon= PhotoImage( file="D:\Projects\Space Apps\photos/upload (3).png" )
sharing = tk.Button( maintk,  width=50,height=30, bg=bgcolor,borderwidth=0,image=sharingicon )
sharing.place( x=1235, y=100 )

downloadingicon= PhotoImage( file="D:\Projects\Space Apps\photos/upload (2).png" )
downloading = tk.Button( maintk,  width=50,height=30, bg=bgcolor,borderwidth=0,image=downloadingicon )
downloading.place( x=1195, y=100 )




def selected():
    global image_path, imageprosses
    global image1
    global img1
    global imgpil
    global previous
    global cvim
    global f_types, imagerestore
    global original
    f_types = [('Jpg Files', '*.jpg'), ('Jpeg Files', '*.jpeg'), ('PNG Files', '*.png'), ('SVG Files', '*.svg'),
               ('WebP Files', '*.webp')]
    imageDisplay1 = filedialog.askopenfilename( filetypes=f_types )
    imgpil = PIL.Image.open( imageDisplay1 )
    img_resized = imgpil.resize( (370, 370) )
    img1 = ImageTk.PhotoImage( img_resized )
    image_display = tk.Label( maintk, image=img1, borderwidth=1, highlightthickness=1, bg=toggler_color )
    image_display.image = img1
    image_display.place( x=300, y=20 )
    cvim = cv.imread( imageDisplay1, 0 )
    original = cvim
    previous= cvim


#
# bot = Bot()
# bot.login(username="demo.773",  # the username from the text box -- Demo app i made --> demo.773
#           password="demoapphaha")  # the password from the text box -- pass --> demoapphaha
# bot.upload_photo("cvim.png", caption="Test")

maintk.mainloop()
