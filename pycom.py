#!/usr/bin/env python
import random, time, math, os, serial, sys

def read_str():
	t = 0
        try:
            result = ser.readline()
	    if result.strip() != "": 
	    	print(result)
	    while 0 != cmp(result , "OK\r\n"):
#	    	print t
	    	t=t+1
                if 20 == t:
                    sys.stderr.write("read timeouti1 \r\n");
                    sys.exit(1);
                    ser.close()
                    break;
		result = ser.readline()
		if result.strip() != "": 
		    print(result)
        except serial.serialutil.SerialException as ee:
            sys.stderr.write("read fail \r\n");
            sys.exit(1);
            ser.close()
        except AttributeError as aee:
            sys.stderr.write("read timeout2 \r\n");
            sys.exit(1);
            ser.close()


def write_str(str):
	print(str)
	x = ser.write(str)


def main(port,data,rate):
    try:
        global ser;
        ser = serial.Serial(port,rate,timeout = 2)
    except serial.SerialException as e:
        sys.stderr.write(port+" not found or Access "+ port +" Permission denied\r\n");
        sys.exit(1);

    write_str(data+"\r\n")
    read_str()

    ser.close()


if __name__ == "__main__":
    global send_port;
    global send_data;
    global send_rate;
    if 3 != len(sys.argv):
        print("param error!\r\nex:./pycom.py /dev/ttyUSB0 at\r\n");
        sys.exit(1);
    send_data = sys.argv[1];
    send_port = sys.argv[2];
    send_rate = 115200;
    main(send_port,send_data,send_rate);
