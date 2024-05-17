# import cv2
import face_recognition as fr
import numpy as np
import mediapipe as mp
import os
from tkinter import *
from PIL import Image, ImageTk
import  imutils 
import math

def Login():
    print("HOla")
def Register():
    print("HOla")


OutFolderPathUser="E:/PC-MIO/estudio/proyecto-python/reconocimiento_facial/DataBase/Users"
PathUserCheck="E:/PC-MIO/estudio/proyecto-python/reconocimiento_facial/DataBase/Users/"
OutFolderPathFace="E:/PC-MIO/estudio/proyecto-python/reconocimiento_facial/DataBase/Faces"

#info list

info  = []

#Interfase
#Main window

screen = Tk()
screen.title(" Face Recognition System") 
screen.geometry("1920x1080")

#background

backgroundimage = PhotoImage(file="E:/PC-MIO/estudio/proyecto-python/reconocimiento_facial/setUp/a.png")
background = Label(image=backgroundimage,text="Face Recognition System")
background.place(relwidth=1,relheight=1,x=0,y=0)


##read data from user Register
#name
InputNameRegisterLabel = Label(screen,text="Nombre")
InputNameRegisterEntry = Entry(screen)
InputNameRegisterLabel.place(x=200,y=180)
InputNameRegisterEntry.place(x=200,y=200)
#user
InputUserRegisterLabel = Label(screen,text="User")
InputUserRegisterEntry = Entry(screen)
InputUserRegisterLabel.place(x=200,y=280)
InputUserRegisterEntry.place(x=200,y=300)
#Pass
InputPasswordRegisterLabel = Label(screen,text="Password")
InputPasswordRegisterEntry = Entry(screen)
InputPasswordRegisterLabel.place(x=200,y=380)
InputPasswordRegisterEntry.place(x=200,y=400)

##read data from user log

InputUserLoginLabel = Label(screen,text="User")
InputUserLoginEntry = Entry(screen)
InputUserLoginLabel.place(x=700,y=280)
InputUserLoginEntry.place(x=700,y=300)
#Pass
InputPasswordLoginLabel = Label(screen,text="Password")
InputPasswordLoginEntry = Entry(screen)
InputPasswordLoginLabel.place(x=700,y=480)
InputPasswordLoginEntry.place(x=700,y=500)


###buttons
#register
butonRegisterImage=PhotoImage(file="E:/PC-MIO/estudio/proyecto-python/reconocimiento_facial/setUp/buton_register.png")
ButtonRegister = Button(screen,image=butonRegisterImage,command=Register,height="167",width="320")
ButtonRegister.place(x=200,y=500)

#login
butonLoginImage=PhotoImage(file="E:/PC-MIO/estudio/proyecto-python/reconocimiento_facial/setUp/buton_login.png")
ButtonLogin = Button(screen,image=butonLoginImage,command=Login,height="167",width="320")
ButtonLogin.place(x=700,y=550)


screen.mainloop()











