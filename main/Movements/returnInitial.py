# set all servos to initial position
import time
from board import SCL, SDA
import busio
import drivers
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

i2c = busio.I2C(SCL, SDA)
pca1 = PCA9685(i2c)
pca1.frequency = 60
# display = drivers.Lcd()

MIN_ANGLE        =           0
MAX_ANGLE        =           180

LF_KNEE_PIN      =           10
LF_SHOULDER_PIN  =           9
LF_HIP_PIN       =           8

LB_KNEE_PIN      =           2
LB_SHOULDER_PIN  =           1
LB_HIP_PIN       =           0

RF_KNEE_PIN      =           14
RF_SHOULDER_PIN  =           13
RF_HIP_PIN       =           12

RB_KNEE_PIN      =           6
RB_SHOULDER_PIN  =           5
RB_HIP_PIN       =           4

RF_KNEE_INIT     =           70
RF_SHOULDER_INIT =           80
RF_HIP_INIT      =           60

RB_KNEE_INIT     =           75 #
RB_SHOULDER_INIT =           60 #
RB_HIP_INIT      =           85 #

LF_KNEE_INIT     =           90 #
LF_SHOULDER_INIT =           100 #
LF_HIP_INIT      =           65 #

LB_KNEE_INIT     =           94 #
LB_SHOULDER_INIT =           65 #
LB_HIP_INIT      =           55 #

RF_KNEE          =           servo.Servo(pca1.channels[RF_KNEE_PIN])
RF_SHOULDER      =           servo.Servo(pca1.channels[RF_SHOULDER_PIN])
RF_HIP           =           servo.Servo(pca1.channels[RF_HIP_PIN])
RB_KNEE          =           servo.Servo(pca1.channels[RB_KNEE_PIN])
RB_SHOULDER      =           servo.Servo(pca1.channels[RB_SHOULDER_PIN])
RB_HIP           =           servo.Servo(pca1.channels[RB_HIP_PIN])
LF_KNEE          =           servo.Servo(pca1.channels[LF_KNEE_PIN])
LF_SHOULDER      =           servo.Servo(pca1.channels[LF_SHOULDER_PIN])
LF_HIP           =           servo.Servo(pca1.channels[LF_HIP_PIN])
LB_KNEE          =           servo.Servo(pca1.channels[LB_KNEE_PIN])
LB_SHOULDER      =           servo.Servo(pca1.channels[LB_SHOULDER_PIN])
LB_HIP           =           servo.Servo(pca1.channels[LB_HIP_PIN])

CTRL_INIT        =           [12] 
CTRL_ANGLE       =           [12]

def init_spot():
    RF_KNEE.angle     = RF_KNEE_INIT
    RF_SHOULDER.angle = RF_SHOULDER_INIT
    RF_HIP.angle      = RF_HIP_INIT
    RB_KNEE.angle     = RB_KNEE_INIT
    RB_SHOULDER.angle = RB_SHOULDER_INIT
    RB_HIP.angle      = RB_HIP_INIT
    LF_KNEE.angle     = LF_KNEE_INIT
    LF_SHOULDER.angle = LF_SHOULDER_INIT
    LF_HIP.angle      = LF_HIP_INIT
    LB_KNEE.angle     = LB_KNEE_INIT
    LB_SHOULDER.angle = LB_SHOULDER_INIT
    LB_HIP.angle      = LB_HIP_INIT
    time.sleep(0.1)
    


def main():
    init_spot()
    pca1.deinit()


if __name__ == '__main__':
    print("hi")
    main()

