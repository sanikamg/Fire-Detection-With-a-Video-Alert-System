import email
import tkinter as tk
from tkinter import*

def activate():
    import cv2
    import numpy as np
    from playsound2 import playsound
    import smtplib
    from email.message import EmailMessage
    from email.mime.base import MIMEBase
    from email import encoders

    fire_reported = 0
    alarm_status = False
    


    def play_audio():
        playsound("C:/Users/ADMIN\Desktop/Fire detection in python/Alarm.mp3",True)

    def send_email():
        
        


        video_file = MIMEBase('application', "octet-stream")


        video_file.set_payload(open('filename.avi', "rb").read())
        encoders.encode_base64(video_file)
        msg = EmailMessage()
        msg['Subject'] = 'warning'
        msg['From'] = 'fire system'
        msg['To'] = 'firesystem123456@gmail.com'
        msg.set_content("fire detected")

        
        msg.add_attachment(video_file, filename="filename.avi")

        server=smtplib.SMTP_SSL('smtp.gmail.com',465)
        server.login("firestationalert@gmail.com","fire@1234")
        server.send_message(msg)
        server.quit()
    



        

		
		


    url = "http://192.168.82.181:8080/video"
    video= cv2.VideoCapture(url)
    frame_width = int(video.get(3))
    frame_height = int(video.get(4))

    size = (frame_width, frame_height)
    
        
    result = cv2.VideoWriter('filename.avi', 
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         10, size)

    while True:

        ret, frame=video.read()
        result.write(frame)
        
      
        frame =  cv2.resize(frame,(1600,600),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
        blur = cv2.GaussianBlur(frame, (15,15),0)
        hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
	
        lower = [18,50,50]
        upper = [35,255,255]

        lower = np.array(lower,dtype='uint8')
        upper = np.array(upper,dtype='uint8')

        mask = cv2.inRange(hsv,lower,upper)

        output = cv2.bitwise_and(frame,hsv,mask=mask)

        size = cv2.countNonZero(mask)
        if int(size) > 25000:
            fire_reported = fire_reported + 1
                                        
            if fire_reported >= 1:
                if alarm_status == False:
                    
                    play_audio()
                    send_email()
                    alarm_status = True

   
	
        if ret == False:
            break
	
        cv2.imshow("output", output)
	
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
	
    cv2.destroyAllWindows()
    video.release()
def exit():
      window.destroy()
window=tk.Tk()
window.title("Fire detection System")
window.geometry("500x500")
window.configure(bg="#CCCCFF")



label= Label(window,text="Fire Detection System",font="Bahnschrift 14 bold",border=0).place(x=130,y=100)

button1 = Button(window,text="ACTIVATE",height=3,font="Bahnschrift 14 bold",width=10,border=0,command=activate,background="orange",activebackground="black", activeforeground="red", highlightcolor="yellow" ).place(x=100,y=180)

button2 = Button(window,text="QUIT",height=3,font="Bahnschrift 14 bold",width=10,command=exit,border=0,background="orange",activebackground="black", activeforeground="red", highlightcolor="yellow" ).place(x=250,y=180)

window.mainloop()
