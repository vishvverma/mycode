#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

LOOKUPAPI = "https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=95131&date=2019-07-16&distance=25&API_KEY=2179EFCE-DA8F-455C-AE1D-8C89AC3FE0A9"

# imports always go at the top of your code
import requests

def main():
    """Run time code"""
    # create r, which is our request object
    r = requests.get(LOOKUPAPI)

    ## set up screen
    print("Weather Forecast")
    print("----------------")

    # display the JSON we were returned as Pythonic datastructures
# loop across the list returned to us
    for x in r.json():
        print(x.get("DateForecast"))
        print("----------")
        print(x.get("Discussion"))

main()
