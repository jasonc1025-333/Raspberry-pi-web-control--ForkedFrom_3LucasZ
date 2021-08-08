import smbus2 as smbus
import int_to_byte

bus = smbus.SMBus(6)
DEVICE_ADDRESS = 0x53

msg = smbus.i2c_msg.read(DEVICE_ADDRESS, 64)
print(bus.i2c_rdwr(msg))