import requests

url_status = "https://www.amsat.org/status/api/v1/sat_info.php?name={}&hours={}"
url_track = "https://www.amsat.org/track/api/v1/passes.php?location={}&object={}"
url_satelitte_index = "https://www.amsat.org/amateur-satellite-index"

sat_names = [
    "AISAT-1",
    "CubeBel-1",
    "CUTE-1",
    "LilacSat-2",
    "FS-3",
]

def get_json_from_requests(url,*params):
    return requests.get(url=url.format(*params)).json()

def get_status(sat_name):
    data = get_json_from_requests(url_status,sat_name,"24")
    res = "Status on Satellite {}\n{}\t\t{}\t\t{}\t{}\t\t{}\n".format(str.upper(sat_name),"Date", "Hour", "Callsign", "Report", "Grid")
    for d in data:
        date,hour = d['reported_time'].split("T")
        callsign = d['callsign']
        report = d['report']
        grid = d['grid_square']
        res = res + "{}\t{}\t{}\t\t{}\t\t{}\n".format(date, hour, callsign, report, grid)
    return res

def get_passes(grid,sat_name):
    data = get_json_from_requests(url_track,grid,sat_name)
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

def get_1st_pass(grid,sat_name):
    data = get_json_from_requests(url_track,grid,sat_name)
    res = "{}\t\t{}\t\t{}\t{}\t{}\t{}\t{}\n".format("Date", "Time", "Duration", "AOS Az.","Max Elev.","Max_Elev._Az", "LOS Az")
    for d in data:
        aos_date, aos_time = d['AOS_time'].split("T")
        pass_duration = d['pass_duration'][-6:]
        aos_azimuth = d['AOS_azimuth']
        max_elevation = d['max_elevation']
        max_elev_azimuth = d['max_elev_azimuth']
        los_azimuth= d['LOS_azimuth']
        res = res + "{}\t{}\t{}\t\t{}\t{}\t\t{}\t\t{}\n".format(aos_date,aos_time,pass_duration, aos_azimuth,max_elevation,max_elev_azimuth,los_azimuth)
        print(res)
        break
    return res

def get_1st_pass_all_sats(grid,sat_names):
    FirstPasses = []
    for sat_name in sat_names:
        First_Pass = get_1st_pass(grid,sat_name)

if __name__ == "__main__":
    grid = "JO28UX"
    sat_name = "AO-91"
    sat_names = [sat_name]
    #print(get_status(sat_name))
    #print(get_passes(grid,sat_name))
    get_1st_pass_all_sats(grid,sat_names)
