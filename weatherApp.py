from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz
import requests

root = Tk()
root.title('Weather App')
root.geometry("900x500+300+200")
root.resizable(False,False)

def getWeather():
    try:
        city = textField.get()
        geolocator = Nominatim(user_agent='geoapiExercises')
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
        
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        # weather
        api = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=b6dca21bf49eeec5a6edb56ace9212b4'
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        valueTemp.config(text=(temp,'°'))
        valueCondition.config(text=(condition,'|','FEELS','LIKE',temp,'°'))
        valueWind.config(text=wind)
        valueHum.config(text=humidity)
        valuePre.config(text=pressure)
        valueDes.config(text=description)
    except Exception as e:
        messagebox.showerror('Weather App','Wrong City!')

# search box
search_image = PhotoImage(file='image/search.png')
imageSearch = Label(image=search_image)
imageSearch.place(x = 20,y = 20)

textField = tk.Entry(root, justify='center',width=17,font=('poppins',25,'bold'),bg='#404040',border=0,fg='white')
textField.place(x = 40, y = 40)
textField.focus()

search_icon = PhotoImage(file='image/search_icon.png')
imageIcon = Button(image=search_icon,borderwidth=0,bg='#404040',cursor='hand2',command=getWeather) # what is cursor??
imageIcon.place(x = 400,y = 34)

# logo
logo_image = PhotoImage(file='image/logo.png')
imageLogo = Label(image=logo_image)
imageLogo.place(x = 150, y = 100)

# bottom box
box_image = PhotoImage(file='image/box.png')
bottomBox = Label(image=box_image)
bottomBox.pack(padx = 5, pady= 5, side=BOTTOM)

# time
name = Label(root, font=('arial',15,'bold'))
name.place(x = 30, y = 100)
clock = Label(root,font=("Helvetica",20))
clock.place(x = 30, y = 130)

# label
label1 = Label(root, text='WIND',font=('Helvetica',15,'bold'),fg='white',bg='#1AB5EF')
label1.place(x = 120,y = 400)
label2 = Label(root, text='HUMIDITY',font=('Helvetica',15,'bold'),fg='white',bg='#1AB5EF')
label2.place(x = 250,y = 400)
label3 = Label(root, text='DESCRIPTION',font=('Helvetica',15,'bold'),fg='white',bg='#1AB5EF')
label3.place(x = 430,y = 400)
label4 = Label(root, text='PRESSURE',font=('Helvetica',15,'bold'),fg='white',bg='#1AB5EF')
label4.place(x = 650,y = 400)

valueTemp = Label(font=('arial',70,'bold'),fg='#EE666D')
valueTemp.place(x = 400, y = 150)
valueCondition = Label(font=('arial',15,'bold'))
valueCondition.place(x = 400, y = 250)

valueWind = Label(text='...',font=('arial',20,'bold'),bg='#1AB5EF')
valueWind.place(x = 120, y = 430)
valueHum = Label(text='...',font=('arial',20,'bold'),bg='#1AB5EF')
valueHum.place(x = 280, y = 430)
valueDes = Label(text='...',font=('arial',20,'bold'),bg='#1AB5EF')
valueDes.place(x = 430, y = 430)
valuePre = Label(text='...',font=('arial',20,'bold'),bg='#1AB5EF')
valuePre.place(x = 670, y = 430)




root.mainloop()