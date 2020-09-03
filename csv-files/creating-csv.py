import csv
hosts = [["workstation.local", "126.364.23.12"], ["webserver.cloud", "196.255.23.11"]]
with open('hosts.csv', 'w') as hosts_csv:
	writer = csv.writer(hosts_csv)
	writer.writerows(hosts)
