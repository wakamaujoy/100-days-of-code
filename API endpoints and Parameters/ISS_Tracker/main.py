import requests
import datetime
import smtplib

my_email = "userjoycee@gmail.com"
my_password ="wetkpklfvpwmagcd"


LAT = -0.498000
LONG = 36.328430
# getting sunrise and sunset in my location
parameters ={
    "lat": LAT,
    "lng": LONG,
    "formatted": 0
}
sunrise_sunset_response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
sunrise_sunset_response.raise_for_status()
sunrise_sunset_response_data = sunrise_sunset_response.json()


rise = int(sunrise_sunset_response_data["results"]["sunrise"].split("T")[1].split(":")[0])
set = int(sunrise_sunset_response_data["results"]["sunset"].split("T")[1].split(":")[0])


print(set)


# getting the current time
time_now = datetime.datetime.now()
hr = time_now.hour
min = time_now.minute
print(hr)

# getting ISSposition at the moment
iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_response.raise_for_status()
iss_response_data =  iss_response.json()
iss_lat = float(iss_response_data["iss_position"]["latitude"])
iss_lng = float(iss_response_data["iss_position"]["longitude"])
iss_pos = ((iss_lat, iss_lng))
print(iss_pos)


# check when the iss is above me
def is_position_true():
    if LAT -5 <=iss_lat <= LAT+5  and LONG -5 <=iss_lng <=LONG+5:
        return True

def is_nighttime():
    if hr>=set and hr <= rise:
        return True

def send_mail():
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(my_email, my_password)
    connection.sendmail(from_addr=my_email, to_addrs="wakamaujoy@gmail.com", msg="SUBJECT:ISS above you, CHECK OUT")

if is_nighttime() and is_position_true():
    send_mail()