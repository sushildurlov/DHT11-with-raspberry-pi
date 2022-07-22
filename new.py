#! /usr/bin/python
import adafruit_dht
import time
import board
import logging
import sys
import psutil
import os

for proc in psutil.process_iter():
    if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
        proc.kill()
# ---------------------------------
dhtSensor = adafruit_dht.DHT11(board.D4)
while True:
    log_format="[%(asctime)s.%(msecs)03d] [%(levelname)s] [%(lineno)d] %(msg)s"
    logging.basicConfig(filename='/var/log/debug1.log', filemode='a', format=log_format, datefmt="%Y-%m-%d %H:%M:%S", level=logging.INFO)
    try:
        humidity = dhtSensor.humidity
        temp_c = dhtSensor.temperature
#	    print("done")
    except RuntimeError:
        print("RuntimeError, trying again...")
        continue
    logging.info("Temperature: {}*C   Humidity: {}% ".format(temp_c, humidity))
    time.sleep(2.0)

