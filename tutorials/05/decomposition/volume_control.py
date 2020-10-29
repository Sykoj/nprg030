import math

# operations
VOLUME_UP = "VOLUME_UP"
VOLUME_DOWN = "VOLUME_DOWN"
MUTE = "MUTE"

# access
password = input("Enter password: ")

# interfaces with hw volume unit -- requires complex computation
volume = 0

def hw0_device_vol_0_s1(v0):
    pass # imagine code

def hw0_device_vol_0_s2(v0):
    pass # imagine code

# check password
if correct_password == password:
    # ask the client what they want to do
    action = input("Enter desired action: ")
    if action == VOLUME_UP:
        if volume > 100:
            print("Incorrect value!")
            exit()
        else:
            volume += 1
        hw_value = 0x3012 * volume // 42
        hw_value /= math.sin(math.pi / 4) 
        hw0_device_vol_0_s1(hw_value * 0x12)
        hw0_device_vol_0_s2(hw_value * 0x01)
    elif action == VOLUME_DOWN:
        if volume < 0:
            print("Incorrect value!")
            exit()
        else:
            volume -= 1
        hw_value = 0x3012 * volume // 42
        hw_value /= math.sin(math.pi / 4) 
        hw0_device_vol_0_s1(hw_value * 0x12)
        hw0_device_vol_0_s2(hw_value * 0x01)
    elif action == MUTE:
        volume = 0
        hw_value = 0x3012 * volume // 42
        hw_value /= math.sin(math.pi / 4) 
        hw0_device_vol_0_s1(hw_value * 0x12)
        hw0_device_vol_0_s2(hw_value * 0x01)
    else:
        ...
else:
    print("Incorrect password!")
