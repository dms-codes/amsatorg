# amsatorg
Get status and passes of satellite from Amsat.org API 

https://amsat.org/status/api/
Send a query like : amsat.org/status/api/v1/sat_info.php?name=AO-91&hours=24 and you will get the last 24 hours of reports for AO-91 in JSON format. 
The hours parameter is optional, if you omit it you will get the last 96 hours of reports. 
The name of the satellite must match the string shown on amsat.org/status , i.e AO-91 works, but AO-92 does not ... use AO-92_L/v or AO-92_U/v instead.
This API is not stable yet ... we are still working on the time, and it seems a query for the list of available satellites is in order. 
For the moment, all reports show half past the hour that they were in.

https://www.amsat.org/track/api/
Use www.amsat.org/track/api/v1/passes.php?objects to get a list of object name/object number pairs. 
Select a name from the list returned from above and use a Maidenhead grid square to specify the location. 
This will give you summary info on the next 10 passes for that location. www.amsat.org/track/api/v1/passes.php?location=JN42&object=ISS
This API is not stable yet. 
Suggestions to webmaster@amsat.org
