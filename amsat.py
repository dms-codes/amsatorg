import requests
import sys

url_status = "https://www.amsat.org/status/api/v1/sat_info.php?name={}&hours={}"
url_track = "https://www.amsat.org/track/api/v1/passes.php?location={}&object={}"


def GetStatus(satname):
    res = requests.get(url=url_status.format(satname,"24"))
    data = res.json()
    res = "Status on Satellite {}\n{}\t\t{}\t\t{}\t{}\t\t{}\n".format(str.upper(satname),"Date", "Hour", "Callsign", "Report", "Grid")
    for d in data:
        date,hour = d['reported_time'].split("T")
        callsign = d['callsign']
        report = d['report']
        grid = d['grid_square']
        res = res + "{}\t{}\t{}\t\t{}\t\t{}\n".format(date, hour, callsign, report, grid)
    return res

def GetPasses(grid,satname):
    res = requests.get(url=url_track.format(grid,satname))
    data = res.json()
    res = "{}\t\t{}\t\t{}\t{}\t{}\t{}\t{}\n".format("Date", "Time", "Duration", "AOS Az.","Max Elev.","Max_Elev._Az", "LOS Az")
    for d in data:
        aos_date, aos_time = d['AOS_time'].split("T")
        pass_duration = d['pass_duration'][-6:]
        aos_azimuth = d['AOS_azimuth']
        max_elevation = d['max_elevation']
        max_elev_azimuth = d['max_elev_azimuth']
        los_azimuth= d['LOS_azimuth']
        res = res + "{}\t{}\t{}\t\t{}\t{}\t\t{}\t\t{}\n".format(aos_date,aos_time,pass_duration, aos_azimuth,max_elevation,max_elev_azimuth,los_azimuth)
    return res

def Get1stPass(grid,satname):
    res = requests.get(url=url_track.format(grid,satname))
    data = res.json()
    res = data
#    aos_date, aos_time = d['AOS_time'].split("T")
#    pass_duration = d['pass_duration'][-6:]
#    aos_azimuth = d['AOS_azimuth']
#    max_elevation = d['max_elevation']
#    max_elev_azimuth = d['max_elev_azimuth']
#    los_azimuth= d['LOS_azimuth']
#    res = aos_date, aos_time,pass_duration,aos_azimuth,max_elevation,max_elev_azimuth,los_azimuth
#    print(res)
    return res

def GetAllSat1stPass(grid,sat_names):
    FirstPasses = []
    First_Pass = Get1stPass(grid,sys.argv[1])
    print(First_Pass)


def GetAllSatsNames():
     SatUrl = "https://www.amsat.org/track/api/v1/passes.php?objects"
     res = requests.get(url=SatUrl)
     data = res.json()
     ListNames = list(data.keys())
     for names in ListNames:
         print(names)
     sys.exit(0)

if __name__ == "__main__":
    grid = "OI33"
    satname = "IO-86"
    if len(sys.argv) < 1:
        print("Please enter one argument")
        print("Example : python amsat.py ENSO")

    if sys.argv[1] == "-SatInfos":
        GetAllSatsNames()
    GetAllSat1stPass(grid,sys.argv[1])
