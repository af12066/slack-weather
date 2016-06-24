#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
import json

def getjsondata():
    response = urllib.request.urlopen("http://weather.livedoor.com/forecast/webservice/json/v1?city=130010").read().decode("utf-8")
    response = json.loads(response)
    
    response = response['forecasts'][0]
    response.update({'city':response['location']['city']})

    return response['forecasts'][0]
