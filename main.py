import csv
from collections import defaultdict, Counter
from urllib.request import urlopen
import pickle
import ssl
from pprint import pprint

context = ssl._create_unverified_context()
f = open('data/22large.csv', 'r')
csv_reader = csv.reader(f, delimiter=',')

next(csv_reader)
data = list(csv_reader)

list_of_devices = urlopen('https://iotanalytics.unsw.edu.au/resources/List_Of_Devices.txt', context=context)
devices = dict()
i=0
for device in list_of_devices:
    listed_device = (list(filter(None, device.decode('utf-8').split('\t'))))
    i += 1
    if i > 1 and len(listed_device) > 2:
        devices[listed_device[1].strip()] = \
            {
                'name': listed_device[0].strip(),
                'type': listed_device[2].replace('\n', '')
            }

devices['e8:ab:fa:19:de:4f'] = {'name': 'Insteon Camera'}
devices['14:cc:20:51:33:ea'] = {'name': 'TPLink Router Bridge LAN (Gateway)'}

print(devices.keys())
master_dict = defaultdict()

for line in data:
    if line[3] in master_dict.keys():
        master_dict[line[3]]['dest_list'].append(line[6])
    else:
        master_dict[line[3]] = {
            'name': devices[line[3]]['name'],
            'dest_list': [line[6]],
            'dest_names': list()
        }

# pprint(master_dict)

with open('ip_mappings.pickle', 'rb') as handle:
    ip_mappings = pickle.load(handle)

for key, val in master_dict.items():
    private_ip_cnt = 0
    # counter = Counter(val['dest_list'])
    for ip in val['dest_list']:
        if ip not in ip_mappings.keys():
            private_ip_cnt += 1
        else:
            master_dict[key]['dest_names'].append(ip_mappings[ip])

    master_dict[key]['private_ip_cnt'] = private_ip_cnt
    # master_dict[key]['most_common'] = counter.most_common()
    master_dict[key]['total_cnt'] = len(val['dest_list'])

for key, val in master_dict.items():
    counter = Counter(val['dest_names'])
    master_dict[key]['most_common'] = counter.most_common()
    print(val['name'])
    print('\tTotal: ', val['total_cnt'], '\n\tPrivate: ', val['private_ip_cnt'])
    print('\tMost common: ')
    for ip, freq in val['most_common']:
        # if ip in ip_mappings.keys():
        #     print('\t\t', ip_mappings[ip], '\t\t', ip, '\t', freq)
        # else:
        print('\t\t', ip, '\t', freq)


with open('master_dict.pickle', 'wb') as handle:
    pickle.dump(master_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

