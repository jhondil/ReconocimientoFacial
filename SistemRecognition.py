import cv2
import face_recognition as fr
import numpy as np
import mediapipe as mp
import os
from tkinter import *
from PIL import Image, ImageTk
import  imutils 
import math


def Profile():
    
    global sept, conteo, Username, OutFolderPathUser
    
    step = 0
    conteo = 0
    
    screen4 = Toplevel(screen)
    screen4.title("Profile")
    screen4.geometry("1280x720")
    
    #background

    backgroundimage = PhotoImage(file="E:/PC-MIO/estudio/proyecto-python/reconocimiento_facial/setUp/a.png")
    background = Label(image=backgroundimage,text="Face Recognition System")
    background.place(relwidth=1,relheight=1,x=0,y=0)
    
    #file
    
    UserFile = open(f"{OutFolderPathUser}/{Username}.txt","r")
    InfoUser = UserFile.read().split(",")
    Name=InfoUser[0]
    User=InfoUser[0]
    Pass=InfoUser[0]
    
    #check User
    
    if User in clases:
        texto1 =Label(screen4,text=f"Nombre: {Name}",font=("Arial",20))
        texto1.place(x=580,y=50)
        
        ##label img
        
        lblimage = Label(screen4)
        lblimage.place(x=490,y=80)
        
        ##imagen
        img = cv2.imread(f"{OutFolderPathFace}/{Username}.png")
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        
        IMG = ImageTk.PhotoImage(image=img)
        
        lblimage.configure(image=IMG)   
        lblimage.image = IMG    
    
    

def Code_face(images):
    #face code
    FaceCode = []
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = fr.face_encodings(img)[0]
        FaceCode.append(encode)
    return FaceCode

def sign_biometric():
    global LogUser, LogPass, OutFolderPath,cap,lblVideo,screen3, FaceCode,clases,images, screen2,step,parpadeo,conteo,Username
    
        
    #check cap
    if cap is not None:
        ret, frame = cap.read()
        
        #resize
        frameSave = frame.copy()
        
        frame = imutils.resize(frame,width=1280)
        #rgb
        frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        #copia foto
        
        if ret== True:
            ##inference face mesh
            
            res = faceMesh.process(frameRGB)
            
            #result list
            px = []
            py= []
            lista = []
            
            if res.multi_face_landmarks:
                #extraer feca mesh  
                
                for rostros in res.multi_face_landmarks:
                    #draw face mesh
                    mpDraw.draw_landmarks(frame,rostros,faceMeshObject.FACEMESH_TESSELATION,ConfigDraw,ConfigDraw)
                    
                    #extraer puntos
                    for id, points in enumerate(rostros.landmark):
                        
                        #información de la imagen
                        h,w,c = frame.shape
                        px.append(int(points.x*w))
                        py.append(int(points.y*h))
                        lista.append([id,px[-1],py[-1]])
                        
                        
                        #468 points
                        if len(lista) == 468:
                            #ojo right
                            x1,y1 = lista[145][1:]
                            x2,y2 = lista[159][1:]
                            longitud1 = math.hypot(x2-x1,y2-y1)
                            
                            #ojo left
                            x3,y3 = lista[374][1:]
                            x4,y4 = lista[386][1:]
                            longitud2 = math.hypot(x4-x3,y4-y3)
                            
                            
                            #parietal derecho                            
                            x5,y5 = lista[139][1:]                          
                            
                            #parietal izquierdo                            
                            x6,y6 = lista[368][1:]
                            
                            #ceja derecha
                            x7,y7 = lista[70][1:]
                             
                            #ceja izq
                            x8,y8 = lista[300][1:]
                      
                            
                            
                            
                            faces = detector.process(frameRGB)
                            
                            if faces.detections is not None:
                                for face in faces.detections:
                                    
                                    #bBox: ID,BBOX, score
                                    
                                    score = face.score[0]
                                    #recuadro al rededor dle rostro
                                    bbox = face.location_data.relative_bounding_box
                                    
                                    
                                    if score> confThreshold:
                                        x1,y1,anc,alt = bbox.xmin,bbox.ymin,bbox.width,bbox.height
                                        x1,y1,anc,alt = int(x1*w),int(y1*h),int(anc*w),int(alt*h)
                                        
                                    
                                    #offset x
                                        
                                    offsetan = (offsetx/100)*anc
                                    x1 = int(x1-int(offsetan/2))
                                    anc = int(anc+offsetan)  
                                    xf = x1+anc  
                                        
                                    #offset y    
                                    offsetalt = (offsety/100)*alt
                                    y1 = int(y1-offsetalt)
                                    alt = int(alt+offsetalt)    
                                    yf = y1+alt
                                    
                                    #error
                                    
                                    if  x1<0: x1=0
                                    if  y1<0: y1=0
                                    if  anc<0:anc=0
                                    if  alt<0: alt=0
                                    
                                    if step == 0:
                                        #draw                                        
                                        cv2.rectangle(frame,(x1,y1,anc,alt),(255,255,255),1)
                                        
                                        #img step0
                                        
                                        als0, anc0, c = img_step0.shape 
                                        frame[50:50+als0,50:50+anc0] = img_step0
                                        #img step1
                                        
                                        als1, anc1, c = img_step1.shape 
                                        frame[50:50+als1,1030:1030+anc1] = img_step1
                                        
                                         #img step2
                                        als2, anc2, c = img_step2.shape 
                                        frame[270:270+als2,1030:1030+anc2] = img_step2
                                        
                                        
                                        
                                        ##face center
                                        
                                        if x7 > x5 and x8 < x6:
                                            #img check
                                            alCheck, ancCheck, c = img_check.shape 
                                            frame[165:165+alCheck,1105:1105+ancCheck] = img_check
                                            
                                            
                                            #cont parpadeo
                                            if longitud1 <= 10 and longitud2 <= 10 and parpadeo == False:
                                                conteo += 1
                                                parpadeo = True
                                        
                                            elif longitud1 > 10 and longitud2 > 10 and parpadeo == True:
                                                parpadeo = False
                                            
                                            cv2.putText(frame,f"Conteo: {conteo}",(1070,375),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
                                            
                                            
                                            #total parpadeo
                                            if conteo >= 3:
                                                alCheck, ancCheck, c = img_check.shape 
                                                frame[165:165+alCheck,1105:1105+ancCheck] = img_check
                                                
                                                
                                                
                                                #open eyes
                                                if longitud1 > 14 and longitud2 > 14:
                                                
                                                    #setp 1
                                                    
                                                    step = 1
                                                    
                                                
                                        else :
                                            conteo = 0
                                    
                                    if step==  1:
                                        #draw
                                        cv2.rectangle(frame,(x1,y1,anc,alt),(0,255,0),1)
                                        
                                        alLi, anLi, c = img_linesCheck.shape 
                                        frame[50:50+alLi,50:50+anLi] = img_linesCheck
                                        
                                        
                                        ##find faces
                                        
                                        facess = fr.face_locations(frameRGB)
                                        facesEncode = fr.face_encodings(frameRGB,facess)
                                        
                                        #iteramos
                                        for faceCod, facesLoc  in zip(facesEncode,facess):
                                            #comparar matches
                                            matches = fr.compare_faces(FaceCode,facesEncode)
                                            
                                            #similitud
                                            
                                            sim1 = fr.face_distance(FaceCode,facesEncode)
                                            
                                            #comparacion minima
                                            minimo = np.argmin(sim1)
                                            
                                            if matches[minimo]:
                                                #user Name
                                                Usernames = clases[minimo].upper()
                                                
                                                Profile()
                                            
                                            
                                            
                            #close windows camera        
                            close=screen3.protocol("WM_DELETE_WINDOW",close_window2)
                                    
                            
                            
                            #cirvle
                            
                            cv2.circle(frame,(x7,y7),2,(0,0,255),cv2.FILLED)
                            cv2.circle(frame,(x8,y8),2,(0,0,255),cv2.FILLED)
                            
                        
                    
            
        
        
        #frame show
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        
        #convertir video
        img= Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        
        #show video
        lblVideo.configure(image=imgtk)
        lblVideo.image = imgtk
        lblVideo.after(10,sign_biometric)
        
    else:
        cap.release()
    
    

def close_windows():
    global step,conteo
    conteo = 0
    step = 0

    screen2.destroy()
    
def close_window2():
    global step,conteo
    conteo = 0
    step = 0

    screen3.destroy()

def log_biometric():
    global screen2, conteo, parpadeo, img_info, step , lblVideo,RegUser
    
    #check cap
    if cap is not None:
        ret, frame = cap.read()
        
        #resize
        frameSave = frame.copy()
        
        frame = imutils.resize(frame,width=1280)
        #rgb
        frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        #copia foto
        
        if ret== True:
            ##inference face mesh
            
            res = faceMesh.process(frameRGB)
            
            #result list
            px = []
            py= []
            lista = []
            
            if res.multi_face_landmarks:
                #extraer feca mesh  
                
                for rostros in res.multi_face_landmarks:
                    #draw face mesh
                    mpDraw.draw_landmarks(frame,rostros,faceMeshObject.FACEMESH_TESSELATION,ConfigDraw,ConfigDraw)
                    
                    #extraer puntos
                    for id, points in enumerate(rostros.landmark):
                        
                        #información de la imagen
                        h,w,c = frame.shape
                        px.append(int(points.x*w))
                        py.append(int(points.y*h))
                        lista.append([id,px[-1],py[-1]])
                        
                        
                        #468 points
                        if len(lista) == 468:
                            #ojo right
                            x1,y1 = lista[145][1:]
                            x2,y2 = lista[159][1:]
                            longitud1 = math.hypot(x2-x1,y2-y1)
                            
                            #ojo left
                            x3,y3 = lista[374][1:]
                            x4,y4 = lista[386][1:]
                            longitud2 = math.hypot(x4-x3,y4-y3)
                            
                            
                            #parietal derecho                            
                            x5,y5 = lista[139][1:]                          
                            
                            #parietal izquierdo                            
                            x6,y6 = lista[368][1:]
                            
                            #ceja derecha
                            x7,y7 = lista[70][1:]
                             
                            #ceja izq
                            x8,y8 = lista[300][1:]
                      
                            
                            
                            
                            faces = detector.process(frameRGB)
                            
                            if faces.detections is not None:
                                for face in faces.detections:
                                    
                                    #bBox: ID,BBOX, score
                                    
                                    score = face.score[0]
                                    #recuadro al rededor dle rostro
                                    bbox = face.location_data.relative_bounding_box
                                    
                                    
                                    if score> confThreshold:
                                        x1,y1,anc,alt = bbox.xmin,bbox.ymin,bbox.width,bbox.height
                                        x1,y1,anc,alt = int(x1*w),int(y1*h),int(anc*w),int(alt*h)
                                        
                                    
                                    #offset x
                                        
                                    offsetan = (offsetx/100)*anc
                                    x1 = int(x1-int(offsetan/2))
                                    anc = int(anc+offsetan)  
                                    xf = x1+anc  
                                        
                                    #offset y    
                                    offsetalt = (offsety/100)*alt
                                    y1 = int(y1-offsetalt)
                                    alt = int(alt+offsetalt)    
                                    yf = y1+alt
                                    
                                    #error
                                    
                                    if  x1<0: x1=0
                                    if  y1<0: y1=0
                                    if  anc<0:anc=0
                                    if  alt<0: alt=0
                                    
                                    if step == 0:
                                        #draw                                        
                                        cv2.rectangle(frame,(x1,y1,anc,alt),(255,255,255),1)
                                        
                                        #img step0
                                        
                                        als0, anc0, c = img_step0.shape 
                                        frame[50:50+als0,50:50+anc0] = img_step0
                                        #img step1
                                        
                                        als1, anc1, c = img_step1.shape 
                                        frame[50:50+als1,1030:1030+anc1] = img_step1
                                        
                                         #img step2
                                        als2, anc2, c = img_step2.shape 
                                        frame[270:270+als2,1030:1030+anc2] = img_step2
                                        
                                        
                                        
                                        ##face center
                                        
                                        if x7 > x5 and x8 < x6:
                                            #img check
                                            alCheck, ancCheck, c = img_check.shape 
                                            frame[165:165+alCheck,1105:1105+ancCheck] = img_check
                                            
                                            
                                            #cont parpadeo
                                            if longitud1 <= 10 and longitud2 <= 10 and parpadeo == False:
                                                conteo += 1
                                                parpadeo = True
                                        
                                            elif longitud1 > 10 and longitud2 > 10 and parpadeo == True:
                                                parpadeo = False
                                            
                                            cv2.putText(frame,f"Conteo: {conteo}",(1070,375),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
                                            
                                            
                                            #total parpadeo
                                            if conteo >= 3:
                                                alCheck, ancCheck, c = img_check.shape 
                                                frame[165:165+alCheck,1105:1105+ancCheck] = img_check
                                                
                                                
                                                
                                                #open eyes
                                                if longitud1 > 14 and longitud2 > 14:
                                                    cut = frameSave[y1:yf,x1:xf]
                                                    
                                                    #save img
                                                    
                                                    cv2.imwrite(f"{OutFolderPathFace}/{RegUser}.png",cut)
                                                    
                                                    #setp 1
                                                    
                                                    step = 1
                                                    
                                                
                                        else :
                                            conteo = 0
                                    
                                    if step==  1:
                                        #draw
                                        cv2.rectangle(frame,(x1,y1,anc,alt),(0,255,0),1)
                                        
                                        alLi, anLi, c = img_linesCheck.shape 
                                        frame[50:50+alLi,50:50+anLi] = img_linesCheck
                                        
                                    
                            #close windows camera        
                            close=screen2.protocol("WM_DELETE_WINDOW",close_windows)
                                    
                            
                            
                            #cirvle
                            
                            cv2.circle(frame,(x7,y7),2,(0,0,255),cv2.FILLED)
                            cv2.circle(frame,(x8,y8),2,(0,0,255),cv2.FILLED)
                            
                        
                    
            
        
        
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
    global LogUser, LogPass, OutFolderPathFace,cap,lblVideo,screen3, FaceCode,clases,images
    
    #get data from user
    LogUser,LogPass = InputUserLoginEntry.get(),InputPasswordLoginEntry.get()
    
    images=[]
    clases = []
    lista = os.listdir(OutFolderPathFace)
    
    #read mages
    
    for i in lista:
        img = cv2.imread(f"{OutFolderPathFace}/{i}")
        images.append(img)
        clases.append(i.split(".")[0])
        
    
    #face code
    FaceCode = Code_face(images)

    #Windows 3
    
    screen3 = Toplevel(screen)
    screen3.title("Bienvenido a Biometric")
    screen3.geometry("1280x720")
    
                #label video
    lblVideo =Label(screen3)
    lblVideo.place(x=0,y=0)
    
    #Capture Video
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(3,1280)
    cap.set(4,720)
    sign_biometric()
            
              
    

    
    
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

#read img step

img_info=cv2.imread("E:/PC-MIO/estudio/proyecto-python/reconocimiento_facial/setUp/info1.png")
img_check=cv2.imread("E:/PC-MIO/estudio/proyecto-python/reconocimiento_facial/setUp/check.png")
img_step0=cv2.imread("E:/PC-MIO/estudio/proyecto-python/reconocimiento_facial/setUp/step0.png")
img_step1=cv2.imread("E:/PC-MIO/estudio/proyecto-python/reconocimiento_facial/setUp/step1.png")
img_step2=cv2.imread("E:/PC-MIO/estudio/proyecto-python/reconocimiento_facial/setUp/step2.png")
img_linesCheck=cv2.imread("E:/PC-MIO/estudio/proyecto-python/reconocimiento_facial/setUp/linesCheck.png")

#enviroment

parpadeo = False
conteo = 0
muestra = 0
step = 0

#offset
offsety = 10
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
screen.geometry("1280x720")

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











