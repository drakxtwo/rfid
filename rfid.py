import serial
serial = serial.Serial("/dev/ttyUSB0", baudrate=9600)

code = ''

while True:
    data = serial.read().decode("utf-8")

    if data == '\r':
        print("RFID CODE:", code)
        strlgth = len(code)
        EmployeeHEX = code[(strlgth - 5):strlgth]
        # print strlgth, EmployeeHEX
        decodeONE = EmployeeHEX[0:1]
        decodeTWO = EmployeeHEX[1:3]

        decodeONE = ord(decodeONE) - ord("A") + 1
        print("1st character: %s " % decodeONE)
        print("2nd character: %s " % decodeTWO)
        EmployeeID = ("%d%s") % (decodeONE, decodeTWO)
        EmployeeID = int(EmployeeID, 16)
        print("Employee ID: %s " % EmployeeID)
        code = EmployeeID = EmployeeHEX = decodeONE = decodeTWO = ''
    else:
        code = code + data
