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

