import requests
from datetime import datetime, timedelta
import config

class UserModel:
    def __init__(self):
        self.accessId = config.APIKEY
        self.stopID = "8600858"
        self.basePoint ='https://www.rejseplanen.dk/api/'
        self.endPoint = "departureBoard"
    def request(self):
        now = datetime.now()
        current_date = now.strftime("%Y-%m-%d") # Formatér til"YYYY-MM-DD"
        current_time = now.strftime("%H:%M") # Formatér til "HH:MM"
        params = {
            "accessId" : self.accessId,
            "id": self.stopID,
            "date" : current_date,
            "time" : current_time,
            "format": "json",
            "useBus": "0"
            }
        url = self.basePoint+self.endPoint
        return requests.get(url,params=params)

req = UserModel()
response = req.request()
departureList = response.json()['Departure']

for departure in departureList:
    name = departure.get("name")
    stop = departure.get("stop")
    time = departure.get("time")
    date = departure.get("date")
    rtTime = departure.get("rtTime")
    rtDate = departure.get("rtDate")
    if rtTime == None:
        rtTime = time
        rtDate = date
    depTime = datetime.strptime(rtTime, "%H:%M:%S").time()
    depDate = datetime.strptime(rtDate,"%Y-%m-%d").date()
    rtDep = datetime.combine(depDate, depTime)
    now = datetime.now().replace(microsecond=0)
    timeDelta = rtDep-now
    timeDelta = max(timeDelta, timedelta())
    direction = departure.get("direction")
    timeDelta = rtDep-now
    timeDelta = max(timeDelta, timedelta())
    direction = departure.get("direction")
    if stop == "CPH Lufthavn" or stop == "Københavns Lufthavn (Ellehammersvej)":
        print(f"Afgang: {name}")
        print(f"Stoppested: {stop}")
        print(f"Planmmæssig afgang: {time}")
        print(f"Faktisk afgang: {rtTime}")
        print(f"Om: {timeDelta}")
        print(f"Retning: {direction}")
        print("-" * 20)

