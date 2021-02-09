# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 00:15:55 2021

@author: intel
"""

import requests

response = requests.get('https://httpbin.org/ip')

print('Your IP is {0}'.format(response.json()['origin']))