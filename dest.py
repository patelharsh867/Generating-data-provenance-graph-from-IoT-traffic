import socket
import csv
import pickle
import pandas as pd


# reader = csv.reader(open('data/22large.csv'), delimiter=',')
# next(reader)

f = open('data/out22.csv', 'w')
csv_writer = csv.writer(f, delimiter=',')

result = dict()
no = 0

data = pd.read_csv('data/22large.csv')
# print(data.head)

unique_dest_ip = data['IP.dst'].unique()
print(len(unique_dest_ip))

for ip in unique_dest_ip:
    print(no, ip)
    no+=1
    if ip == None:
        continue
    else:
        try:
            res = socket.gethostbyaddr(ip)[0]
            result[ip] = res
            csv_writer.writerow([ip, res])
            print('\t\t', res)
        except:
            pass

print(result)

with open('ip_mappings.pickle', 'wb') as handle:
    pickle.dump(result, handle, protocol=pickle.HIGHEST_PROTOCOL)
