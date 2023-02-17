from flask import Flask,request,render_template
import requests
from datetime import datetime

app = Flask(__name__)
my_api ="### PUT YOUR API KEY ###"   #  i.e. Generated during sign in TO API portal

@app.route('/',methods = ['GET','POST'])
def weather():
    if request.method =='POST':
        city = request.form.get('city')
        comp_api_link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={my_api}"
        api_link = requests.get(comp_api_link)
        api_data = api_link.json()

        if api_data['cod'] =='404':
            return f"<h2> ! ! ! Invalid city {city}, please check the spelling .</h2>"
        else:
            wea_main = (api_data['weather'][0]['main'])
            temp1    = ((api_data['main']['temp']) - 273.15)
            temp     = round(temp1,2)
            humid    = (api_data['main']['humidity'])
            speed    = (api_data['wind']['speed'])
            timezone = (api_data['name'])
            tm       = datetime.now().strftime("%d/%m/%Y, %H:%M:%S %p")
        return render_template('index.html',wea_main=wea_main,temp=temp,humid=humid,speed=speed,timezone=timezone,tm=tm,city=city )
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
