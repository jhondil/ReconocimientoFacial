import cv2
import face_recognition as fr
import numpy as np
import mediapipe as mp
import os
from tkinter import *
from PIL import Image, ImageTk
import  imutils 
import math

def log_biometric():
    global screen2, conteo, parpadeo, img_info, step , lblVideo
    
    #check cap
    if cap is not None:
        ret, frame = cap.read()
        
        #resize
        
        frame = imutils.resize(frame,width=1280)
        
        #frame show
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        
        #convertir video
        img= Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        
        #show video
        lblVideo.configure(image=imgtk)
        lblVideo.image = imgtk
        lblVideo.after(10,log_biometric)
        
    else:
        cap.release()
    
def Login():
    print("HOla")
    
def Register():
    global RegName, RegUser, RegPass, InputNameRegisterEntry, InputUserRegisterEntry, InputPasswordRegisterEntry,cap,lblVideo,screen2
    #get data from user
    RegName,RegUser,RegPass = InputNameRegisterEntry.get(),InputUserRegisterEntry.get(),InputPasswordRegisterEntry.get()
    
    #incomplete info
    if len(RegName)==0 or len(RegUser)==0 or len(RegPass)==0:
        print("Formlario Incopleto")
    else:
        #check list user 
        userList = os.listdir(PathUserCheck)
        #name Users
        UserNames = [user.split(".")[0] for user in userList]
        # UserName=[]
        # for user in userList:
        #     UserName.append(user.split(".")[0])
            
        #check if user is already registered
        if RegUser in UserNames:
            print("Usuario ya registrado")
        else:   
            info.append(RegName)
            info.append(RegUser)
            info.append(RegPass)
            
            f = open(f"{OutFolderPathUser}/{RegUser}.txt","w")
            f.write(RegName+","+RegUser+","+RegPass)
            # f.write(RegName+",")
            # f.write(RegUser+",")
            # f.write(RegPass)
            f.close()
            
            InputNameRegisterEntry.delete(0,END)
            InputUserRegisterEntry.delete(0,END)
            InputPasswordRegisterEntry.delete(0,END)
            
            #screen2
            screen2 = Toplevel(screen)
            screen2.title("Login Biometric")
            screen2.geometry("1280x720")
            
            #label video
            lblVideo =Label(screen2)
            lblVideo.place(x=0,y=0)
            
            #Capture Video
            cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
            cap.set(3,1280)
            cap.set(4,720)
            log_biometric()
            
            
    


OutFolderPathUser="E:/PC-MIO/estudio/proyecto-python/reconocimiento_facial/DataBase/Users"
PathUserCheck="E:/PC-MIO/estudio/proyecto-python/reconocimiento_facial/DataBase/Users/"
OutFolderPathFace="E:/PC-MIO/estudio/proyecto-python/reconocimiento_facial/DataBase/Faces"

#enviroment

parpadeo = False
conteo = 0
muestra = 0
step = 0

#offset
offsety = 30
offsetx = 20

#threshold
confThreshold = 0.5

#tool draw
mpDraw = mp.solutions.drawing_utils
ConfigDraw = mpDraw.DrawingSpec(thickness=1, circle_radius=1)

#object face mesh

faceMeshObject = mp.solutions.face_mesh
faceMesh = faceMeshObject.FaceMesh(max_num_faces=1)

#object face Detect

faceObject = mp.solutions.face_detection
detector = faceObject.FaceDetection(min_detection_confidence=0.5, model_selection=1)




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











