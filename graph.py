# To display master_dict, run the following:
import pickle
with open('master_dict.pickle', 'rb') as handle:
    master_dict = pickle.load(handle)

import networkx as nx
import matplotlib.pyplot as plt
import csv
from collections import defaultdict
graph = defaultdict(set)

i = 0
for key, val in master_dict.items():
    if ( i==8):
        graph[val['name']] =  set(val['dest_names'])
        break
    print(val['name'])
    print('\tTotal: ', val['total_cnt'])
    print('\tPrivate: ', val['private_ip_cnt'])
    #print('\tList of dest names:', val['dest_names'])
    print('\tMost common: ')
    for ip, freq in val['most_common']:
        # if ip in ip_mappings.keys():
        #     print('\t\t', ip_mappings[ip], '\t\t', ip, '\t', freq)
        # else:
        print('\t\t', ip, '\t', freq)
    i+=1
print("final",graph)
g = nx.DiGraph(graph)
pos = nx.spring_layout(g)
nx.draw(g, dim=2, k=None, pos=None, fixed=None, iterations=50, weight='weight', scale=1,with_labels = True,font_size=7,linewidths=0.1,width=0.1,node_size=80,font_color='darkblue',node_color='grey',font_weight='bold')
plt.axis('off')
plt.draw()
plt.show()