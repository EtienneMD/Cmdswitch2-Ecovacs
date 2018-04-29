# Cmdswitch2-Ecovacs
A Python script to integrate your Ecovacs vacuum to Homekit.

## Requirements
This script assumes you have the following installed:
* [Homebridge](https://github.com/nfarina/homebridge)
* [Cmdswitch2](https://github.com/luisiam/homebridge-cmdswitch2)
* [Sucks](https://github.com/wpietri/sucks)

## Installation
1. Enter your Ecovacs credentials into the python  script
2. Run the script as state_cmd in your config.json file.  

### Example configuration
 ```
"platforms": [{
    "platform": "cmdSwitch2",
    "name": "CMD Switch",
    "switches": [{
        "name": "Vacuum",
        "on_cmd": "sucks clean 120",
        "off_cmd": "sucks charge",
        "state_cmd": "python3 /var/homebridge/vacstate.py",
        "polling": true,
        "interval": 120,
        "timeout": 20
    }]
```

## License
MIT
