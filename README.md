# Meraki Camera Notification Example

Leverage Meraki new camera API and MQTT capability to create a notification service. When the camera detects a person consistently appears in a particular zone the service will send a Webex team message to a Webex team room with a video link which will directly go to the video footage when that even occurred.

![](/docs/digram.png)


## API and technology

### API

[Camera API](https://n262.meraki.com/CiscoStore-switc/n/XSQlFbOc/manage/support/api_docs#returns-video-link-for-the-specified-camera): Returns video link for the specified camera. If a timestamp supplied, it links to that time.

### MQTT and setting:

1. Go to **Cameras > [Camera Name] > Settings > Sense** page.
2. Click **Add or edit MQTT Brokers > New MQTT Broker** and add you broker information. You can find public broker at [here](https://github.com/mqtt/mqtt.github.io/wiki/public_brokers).
3. You can install [MQTT.fx](https://mqttfx.jensd.de/) to subscribe to MQTT broker. This is a very useful tool



## Build locally
1. Update `MQTT information`,`Meraki API`,`Network ID`, `Camera information` in `app.py` and `WEBEXTEAMKEY` and `Room_id` in `Webexteam.py`
2. Run `python3 install -r requirement.txt`
3. Run `python3 app.py`


## Docker

Build : `docker build -t meraki-camera-notification .`

Run : `docker run -it meraki-camera-notification .`
