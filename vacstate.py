from sucks import *
from time import sleep
from sys import exit
import logging

logging.disable(logging.CRITICAL)

def On(vacbot):
    vacbot.disconnect()
    exit(0)

def Off(vacbot):
    vacbot.disconnect()
    exit(1)

def ConnectVac():
    # Enter your credentials here.
    config = {
                'device_id': EcoVacsAPI.md5(str(time.time())),
                'email': '<email>',
                'password': EcoVacsAPI.md5('<password>'),
                'country': '<country>',
                'continent': '<continent>'
             }

    api = EcoVacsAPI(config['device_id'],config['email'],config['password'],
                                config['country'],config['continent'])
    vac_id = api.devices()[0]
    vacbot = VacBot(api.uid,api.REALM,api.resource, api.user_access_token, vac_id, config['continent'])
    vacbot.connect_and_wait_until_ready()
    return vacbot

vacbot = ConnectVac()
vacbot.run(GetChargeState())
sleep(1)
if vacbot.charge_status == "returning": #Returning
    On(vacbot)
if vacbot.charge_status == "charging": #Charging
    Off(vacbot)
vacbot.run(GetCleanState())
sleep(1)
if vacbot.clean_status == "stop": #Stuck
    Off(vacbot)
else: #Cleaning
    On(vacbot)
