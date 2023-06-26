import serial
import time


ser = serial.Serial('/dev/ttyUSB0',  baudrate=300)


#input()
g_code = ''

g_code_send = """%
    N` G`   X `    Z `  F`  H 
    00M03                     
    01M30                     
   M|"""
input()
# ser.write(g_code_send.encode('ascii'))  

while ser.in_waiting:
    g_code += ser.read().decode('ascii')

print(g_code)
# ser.write(bytes([1]))    
    
# #   s.writelines("hello")
# print(ser.in_waiting)

# time.sleep(2)
# ser.write(bytes([0]))

# time.sleep(2)
