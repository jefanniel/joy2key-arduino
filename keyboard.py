import serial
import keyboard as k

ser = serial.Serial('COM3', baudrate=9600, timeout=1)

def decode(x, y, z):
    if x == 'l':
        k.press("left"); k.release("right")
    elif x == 'r':
        k.press("right"); k.release("left")
    else:
        k.release("left"); k.release("right")

    if y == 'u':
        k.press("up"); k.release("down")
    elif y == 'd':
        k.press("down"); k.release("up")
    else:
        k.release("up"); k.release("down")

    if z == '1':
        k.press("space")
    else:
        k.release("space")


while True:
    try:
        line = ser.readline().decode('ascii').strip()
        if not line:
            continue

        parts = line.split(',')
        if len(parts) != 3:
            continue

        x, y, z = parts
        decode(x, y, z)

    except Exception as e:
        print("Error:", e)
