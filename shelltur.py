import platform
import socket

print("=" * 40)
print(" SUCCESS: Connected to Raspberry Pi!")
print("=" * 40)
print(f"Hostname : {socket.gethostname()}")
print(f"System   : {platform.system()} {platform.release()}")
print(f"Hardware : {platform.machine()}")

# Read Raspberry Pi CPU temperature directly from the system file
try:
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
        temp_c = int(f.read().strip()) / 1000.0
    print(f"CPU Temp : {temp_c}°C")
except FileNotFoundError:
    print("CPU Temp : Thermal zone not found (Running on PC?)")
print("=" * 40)
