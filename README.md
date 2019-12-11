# Generating-data-provenance-graph-from-IoT-traffic
### File name and their contents
Network_Output_Domain.txt - Network output dictionary 
http_payload_txt -  http request output file
Consolidated Output for all devices date wise.zip -  All the output files after parsing pcap date wise

main.py -  Network dictionary code
graph.py -  graph generation code
dest.py - Reverse IP lookup code
payload.py -  Code to extract http request with source,destination and body
master_dict.pickle.pickle - Master dictionary with all source destination mappings mapped to mac address of IOT devices
