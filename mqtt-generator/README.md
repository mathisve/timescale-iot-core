# iot-core-mqtt

## Virtual Environment
To make this easier, set up a virtual environment
```
virtualenv env
source env/bin/activate
pip3 install -r requirements.txt
```

## Set up environment variables
```
source setup.sh
```

<!-- https://stackoverflow.com/a/50680936/11413442 -->

## Certificates
You need to generate (or request) a certificate and private key! If you generate these using your own CA, you need to register it with IoT Core!


## Run the code
Lastly, run the code:
```
python3 main.py
```