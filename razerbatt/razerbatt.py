#!/bin/env python
from openrazer.client import DeviceManager

desired_device = "YOUR DEVICE NAME"

device_manager = DeviceManager()

for device in device_manager.devices:
	if desired_device in device.name:
	   desired_device = device
	else:
	   print('not found')
	   exit()

is_charging = ''
if desired_device.is_charging:
    is_charging = '󱐋'

print(f'{is_charging}{desired_device.battery_level}')
