import tkinter as tk
from tkinter import*

def activate():
    import cv2
    import numpy as np
    video= cv2.VideoCapture("FireVideo2.mp4")
    fire = False
    while True:

	    ret, frame=video.read()
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
	    if int(size) > 10000:
		    if fire == False:
			    print("fire detected")
			    fire = True


   
	
	    if ret == False:
		    break
	
	    cv2.imshow("output", output)
	
	    if cv2.waitKey(1) & 0xFF == ord("q"):
		    break
	
    cv2.destroyAllWindows()
    video.release()
def exit():
      window.destroy
window=tk.Tk()
window.title("Fire detection System")
window.geometry("500x500")
window.configure(bg="#CCCCFF")



label= Label(window,text="Fire Detection System",font="Bahnschrift 14 bold",border=0).place(x=130,y=100)

button1 = Button(window,text="ACTIVATE",height=3,font="Bahnschrift 14 bold",width=10,border=0,command=activate,background="orange",activebackground="black", activeforeground="red", highlightcolor="yellow" ).place(x=100,y=180)

button2 = Button(window,text="QUIT",height=3,font="Bahnschrift 14 bold",width=10,command=exit,border=0,background="orange",activebackground="black", activeforeground="red", highlightcolor="yellow" ).place(x=250,y=180)

window.mainloop()
