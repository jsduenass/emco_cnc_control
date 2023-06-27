roscore
rosrun cnc_control cnc_control.py 
rostopic pub -1 /send_g_code std_msgs/String 'data: "%\r\n    N` G`   X `    Z `  F`  H \r\n\    00M03                     \r\n\    01M30                     \r\n\   M|"'