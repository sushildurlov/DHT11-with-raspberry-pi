# DHT11-with-raspberry-pi
To be able to easily communicate with some sensors, CircuitPython has been developed. So, before installing the specific DHT-library, we have to do some preparation work. <br />

Open a terminal window and write following commands: <br />
sudo apt update <br />
sudo apt full-upgrade <br />
sudo apt install python3-pip <br />
sudo pip3 install --upgrade setuptools <br />
sudo reboot <br />
Then install and run a script developed by Adafruit : <br />
sudo pip3 install --upgrade adafruit-python-shell <br />
wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py <br />
sudo python3 raspi-blinka.py <br />
Install the CircuitPython-DHT Library <br />
Open a terminal window and write following commands: <br />

pip3 install adafruit-circuitpython-dht <br />
sudo apt-get install libgpiod2 <br />

To enable dht11.py script run automatic copy temperature.service file inside /etc/systemd/system of raspberry pi  <br />
Enjoy!!!
