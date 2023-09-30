# Satellite Tracking Script

This Python script allows you to retrieve real-time information about various amateur radio satellites. It provides two main functions:

1. `GetStatus(satname)`: This function retrieves and displays the status of a satellite, including recent reports, callsigns, and grid squares. It uses the AMSAT API to fetch this information.

2. `GetPasses(grid, satname)`: This function retrieves and displays the next passes of a satellite over a specific grid location. It provides information such as pass date, time, duration, azimuth of acquisition of signal (AOS), maximum elevation, azimuth of maximum elevation, and azimuth of loss of signal (LOS).

## Usage

To use this script, you need to have Python installed on your system. You can run the script by executing the following commands in your terminal:

1. Install the required libraries (if not already installed):

```bash
pip install requests
```

2. Run the script with the following command:

```bash
python satellite_tracking.py
```

Make sure to modify the `grid` and `sat_names` variables within the script to match your desired grid location and list of satellite names for tracking. By default, the script is configured to track the following satellites:

- AISAT-1
- CubeBel-1
- CUTE-1
- LilacSat-2
- FS-3

You can customize the list of satellites by updating the `sat_names` variable.

## Examples

Here are some examples of how to use the script:

```python
# Retrieve status information for a satellite (e.g., IO-86)
status_info = GetStatus("IO-86")
print(status_info)

# Retrieve upcoming passes for a satellite (e.g., IO-86) over a specific grid (e.g., OI33)
pass_info = GetPasses("OI33", "IO-86")
print(pass_info)

# Retrieve the first upcoming pass for a satellite (e.g., IO-86) over a specific grid (e.g., OI33)
first_pass_info = Get1stPass("OI33", "IO-86")
print(first_pass_info)

# Retrieve the first upcoming passes for a list of satellites (e.g., sat_names) over a specific grid (e.g., OI33)
GetAllSat1stPass("OI33", sat_names)
```

Please note that you need an internet connection to fetch real-time satellite information from the AMSAT API.

## Dependencies

This script relies on the following Python library:

- `requests`: This library is used to make HTTP requests to the AMSAT API for retrieving satellite information. Install it using the `pip` command as mentioned above.

## Disclaimer

This script is provided as-is and may be subject to changes in the AMSAT API or other external factors. Use it responsibly and consider any usage restrictions or terms of use imposed by the AMSAT API provider.

Feel free to customize and extend the script to suit your specific needs or integrate it into other projects as necessary.
