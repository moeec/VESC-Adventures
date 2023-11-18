from pyvesc import VESC

# Serial port may vary based on your setup
serial_port = '/dev/ttyUSB0'  # or 'COM3' on Windows

with VESC(serial_port=serial_port) as my_vesc:
    # Set the speed (RPM)
    my_vesc.set_rpm(3000)
