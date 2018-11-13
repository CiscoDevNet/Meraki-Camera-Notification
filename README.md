# Meraki Camera Notification Example

[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/CiscoDevNet/Meraki-Camera-Notification)

Leverage Meraki new camera API and MQTT capability to create a notification service. When the camera detects a person consistently appears in a particular zone the service will send a Webex team message to a Webex team room with a video link which will directly go to the video footage when that even occurred. This is useful for alerting unexpected person movement in off-hours.

![](/docs/digram.png)


## API and technology

### API

[Camera API](https://documenter.getpostman.com/view/897512/2To9xm#20d8eb95-2b3c-41cb-98de-61222b4d32d1): Returns video link for the specified camera. If a timestamp supplied, it links to that time.

### MQTT and setting:

1. Go to **Cameras > [Camera Name] > Settings > Sense** page.
2. Click **Add or edit MQTT Brokers > New MQTT Broker** and add you broker information. For testing/trial you can find public broker at [here](https://github.com/mqtt/mqtt.github.io/wiki/public_brokers).
3. You can install [MQTT.fx](https://mqttfx.jensd.de/) to subscribe to MQTT broker. This is a very useful tool



## Build locally
### Config
#### Configurations in `app.py`

General API and MQTT configurations

|Name|Description|
|---|---|
|MQTT_SERVER|MQTT Broker ip or domain|
|MQTT_PORT|MQTT Broker port|
|MQTT_TOPIC|Meraki Camera mqtt top, default is "/merakimv/#"|
|MERAKI_API_KEY|Meraki Api key|
|NETWORK_ID|Camera's network ID, will use this get video link with camera api|
|COLLECT_CAMERAS_SERIAL_NUMBERS|Array of cameras serial numbers, all is *.|
|COLLECT_ZONE_IDS|Array of zone id, all is *|

Motion detected configurations, you can keep this as it.

|Name|Description|
|---|---|
|MOTION_ALERT_PEOPLE_COUNT_THRESHOLD| The threshold of people count from the camera to start the detection mode|
|MOTION_ALERT_ITERATE_COUNT| The iterate count when in the detection mode|
|MOTION_ALERT_TRIGGER_PEOPLE_COUNT| After threshold of people count after iteration to trigger the alert or not|
|MOTION_ALERT_PAUSE_TIME|The pause time after alert is triggered|

#### Configurations in `Webexteam.py`

|Name|Description|
|---|---|
|WEBEXTEAMKEY|The Webex team API key|
|ROOM_ID| The Webex team room ID|

### Build
1. Run `python3 install -r requirement.txt`
2. Run `python3 app.py`


## Docker

Build : `docker build -t meraki-camera-notification .`

Run : `docker run -it meraki-camera-notification .`
