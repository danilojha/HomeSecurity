# HomeSecurity
Items used: 

- Intel Galileo Board 
- Ultrasonic Range Finder
- Webcam
- SD card
- My nerves trying to figure out the IP everytime it changed

Although the Galileo Board comes preloaded with a base version of Linux, this project required booting a developer kit Linux image that allowed the use of OpenCV.

Initially the project only worked with an ethernet cable, but wireless functionality was also added with the inclusion of a WiFi adapter in the final stage.

What happens when this is set up?

When an object gets too close to the rangefinder it triggers the webcam, which takes a photo and saves it locally on the board. The board then uploads the image to a pre-made email and sends it to a specified recipient.
