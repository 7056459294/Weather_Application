# temperature and hum. checking app

import tkinter as tk
import requests,json
import pyttsx3


def btnSubmit():
   city=entry.get()  
   data=requests.get("http://api.weatherapi.com/v1/current.json?key=5a643b20dbc8468483c52636200408&q="+str(city))
   data=json.loads(data.content)
   d=data["location"]["localtime"]
   t=data["current"]["temp_c"]
   h=data["current"]["humidity"]
   lbl6=tk.Label(root,text=d,font=30,bg="yellow",fg="red",padx=5,pady=5)
   lbl6.grid(row=4,column=1)
   lbl7=tk.Label(root,text=t,font=30,bg="yellow",fg="red",padx=5,pady=5)
   lbl7.grid(row=5,column=1)
   lbl8=tk.Label(root,text=h,font=30,bg="yellow",fg="red",padx=5,pady=5)
   lbl8.grid(row=6,column=1)
   if t>=30:
       ob2=pyttsx3.init()
       ob2.say(f"{city} temperature is high {t} degree celcius and humidity is {h} ")
       ob2.runAndWait()
   elif 15>t<30:
       ob2=pyttsx3.init()
       ob2.say(f"{city} temperature is normal {t} degree celcius and humidity is {h} ")
       ob2.runAndWait()
   else:
       ob2=pyttsx3.init()
       ob2.say(f"{city} temperature is low {t} degree celcius and humidity is {h} ")
       ob2.runAndWait()
   
    
root=tk.Tk()
root.title("MOHIT T&H App")
root.geometry("")
root.config(bg="sky blue") 
 
        
lbl1=tk.Label(root,text="CITY:-",font=30,bg="yellow",fg="red",padx=5,pady=5)
lbl1.grid(row=0,column=0)

        
entry=tk.StringVar()
entry=tk.Entry(root,textvariable=id)
entry.grid(row=0,column=1)

btn_submit=tk.Button(root,text="SUBMIT",font=20,command=btnSubmit)
btn_submit.grid(row=3,column=1)

lbl3=tk.Label(root,text="Time..-",font=30,bg="yellow",fg="red",padx=5,pady=5)
lbl3.grid(row=4,column=0)
lbl4=tk.Label(root,text="Temp..-",font=30,bg="yellow",fg="red",padx=5,pady=5)
lbl4.grid(row=5,column=0)
lbl5=tk.Label(root,text="Hum..-",font=30,bg="yellow",fg="red",padx=5,pady=5)
lbl5.grid(row=6,column=0)

ob2=pyttsx3.init()
ob2.say("welcome mohit temperature and humidity application")
ob2.runAndWait()  


tk.mainloop()