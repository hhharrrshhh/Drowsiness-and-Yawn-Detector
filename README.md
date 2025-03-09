# Drowsiness and Yawn detection with voice alerts.

## Dependencies

1. Python 3.11.9
2. opencv 4.11.0.86
3. dlib-bin 19.24.6
4. imutils 0.5.4
5. scipy  1.15.2
6. numpy 2.2.3
7. argparse 
8. playsound 1.2.2

## Run 

```
Python3 drowsiness_yawn.py -- webcam 0		//For external webcam, use the webcam number accordingly
```

## Setups

Change the threshold values accordingly.
```
EYE_AR_THRESH = 0.3
EYE_AR_CONSEC_FRAMES = 30
YAWN_THRESH = 10	//change this according to the distance from the camera


This code is tested for Windows.If using Linux or Raspberry Pi,we can use ESpeak module instead of Playsound.

ESpeak doesn't seem to wrok on Windows for some reason,so I used Playsound module instead..
```

## Authors

**Harsh Gharat** 
