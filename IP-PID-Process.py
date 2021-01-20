import psutil
from time import sleep
import logging

logging.basicConfig(filename='process.log', encoding='utf-8', format='%(asctime)s %(message)s', level=logging.DEBUG)

def check_con(target_ip):
	net_con = psutil.net_connections()
	for i in net_con:
		try:
			ip = i[4][0]
			stat = i[5]
		except:
			ip = ''
			stat = ''
		if (ip == target_ip_1 or ip == target_ip_2) and stat=='ESTABLISHED':
			pid = i[6]
			logging.info("Found PID"+str(pid))
			if psutil.pid_exists(pid):
				for p in psutil.process_iter(['pid', 'name', 'username']):
					if p.pid == pid:
						logging.warning(p.info)
			else:
				print("Pid doesn't exist")
			logging.info(str(i)+str(pid))

if __name__=='__main__':
	logging.info("Starting")
	target_ip_1 = '*.*.*.*'
	target_ip_2 = '*.*.*.*'
	logging.info("Target: %s , %s"  %(target_ip_1 , target_ip_2))
	print("Detecting the network connections to %s " % target_ip)
	while True:
		check_con(target_ip)
		sleep(0.5)
		logging.info('Not detected')
