#!/usr/bin/env python

import rospy
import serial
import sys

from std_msgs.msg import String
from std_srvs.srv import Trigger, TriggerResponse

class EmcoCompact5CNC(serial.Serial):
    def __init__(self, port='/dev/ttyUSB0', baudrate=300):
        super().__init__(port, baudrate)
        
        rospy.init_node('emco_compact5_cnc')

        self.subscriber = rospy.Subscriber('send_g_code', String, self.send_g_code)
        self.service = rospy.Service('get_g_code', Trigger, self.get_g_code)
        rospy.spin()

    def send_g_code(self, g_code):
        self.write(g_code.data.encode('ascii'))
        rospy.loginfo('G-code sent')        

    def get_g_code(self, req):
        res = TriggerResponse()
        
        if self.in_waiting > 0:
            while self.in_waiting:
                res.message += self.read().decode('ascii')
                rospy.sleep(0.035) # 300 DB to T

            rospy.loginfo('G-code received') 
            res.success = True
        else:
            res.success = False
            rospy.logwarn('No G-code received')
            
        return res
        

if __name__ == '__main__':

    if len(sys.argv) > 1:
        port = rospy.get_param(sys.argv[2])
        EmcoCompact5CNC(port)
    else:
        EmcoCompact5CNC()