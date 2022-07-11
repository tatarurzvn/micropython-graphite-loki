# micropython-graphite-loki-http
Sends graphite & loki stats to cloud via HTTP.
Wifi connection needs to be set-up before. 
Time needs to be set-up before.

## Installation
- Replace `config.py` with correct credentials
- Compile the `mrequests` submodule (used due to lack of basic auth in the standard library)
- Install ampy
```
pip install adafruit-ampy
```
- Push mrequests *mpy to mcu /lib using
```
ampy -p [serial_port] -b [baud_rate] put *.mpy /lib/*.mpy
```
- Push `config.py` and `metrics.py` to mcu
```
ampy -p [serial_port] -b [baud_rate] put config.py config.py
ampy -p [serial_port] -b [baud_rate] put metrics.py metrics.py
ampy -p [serial_port] -b [baud_rate] ls
```
