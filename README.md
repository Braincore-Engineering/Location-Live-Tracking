# Location-Live-Tracking
The source code of Location Live Tracking using GPS Module


## Run Locally

Clone the project

```bash
  git clone https://github.com/Braincore-Engineering/Location-Live-Tracking.git -b dzaky/impl
```

Go to the project directory and initialize Virtual Environment

```bash
  cd Location-Live-Tracking
  py -3 -m venv .venv
```

activate the virtual environment and install all the requirement

```bash
  .\.venv\Scripts\activate
  pip install -r .\requirements.txt
```

setup your environment from the .env.example

```bash
  cp .env.example .env
```

Start the server

```bash
  flask --app app run --debug
```

## ESP32 Code

Get yourself an ESP32 module or devkit and a UART GPS Module (Ublox 6M would work) and also preferably I2C 1306 OLED Screen

Open the ESP32_GPS.ino file and change this configuration

```c
const char* ssid = "wife-i";
const char* password = "73555608";
const char* serverName = "https://location-live-tracking-muf7kziviq-as.a.run.app/receive_data";
const char* trackerId = "2";
```

Adjust to your local WiFi SSID and password, latest endpoint and your designated trackerId

Compile and upload to the ESP32 and wait until the GPS module calibrated itself!

