#!/usr/bin/env python
import logging
import time
import os
curtime=time.strftime('%Y-%m-%d',time.localtime())
dir='/var/log/python-{}/'.format(curtime)
if not os.path.exists(dir):
	os.mkdir(dir)
logging.basicConfig(filename=r"{}/test.log".format(dir),
		level=logging.INFO,
		datefmt='%Y-%m-%d %H:%M:%S',
		format='%(asctime)s %(levelname)s  %(message)s'
		)
def printtime():
	logging.info('This function was called')
printtime()
