# some useful python standard libraries
import csv, json, sys
from random import randint
import ipaddress

def readIPData(json_file):
    """(10 pt) Return the a list of dictionary of raw data
    
    json_file : the directory of db.json
    
    e.g. [{
            "ip":"238.167.63.192",
            "city": "Denison"
          },
          {
            "ip": "242.134.236.156",
            "city": "Hackensack"
          },
          ...
            ]
    """
    with open(json_file, "r") as f :
        data = json.load(f)
    return data
    pass

def readQuery(query_file):
    """(10 pt) Return a list of query IPs    
    
    query_file : the directory of query.csv
    
    e.g. ["238.167.63.192", "242.134.236.156", ...]
    
    """
    ip = []
    with open(query_file, "r") as f :
        data = csv.DictReader(f)
        for row in data:
            ip.append(row['ip'])
    return ip
    pass

def writeAns(array, ans_file):
    """(10 pt) Write query answer to csv file
    
    array : response answer of each query 
    ans_file : output file directory
    
    output csv should be in this format:
    
    ip,city
    238.167.63.192,Denison
    242.134.236.156,Hackensack
    8.8.8.8,-1
    ...
    
    """
    with open(ans_file, 'w') as output:
        name = ['ip', 'city']
        writer = csv.DictWriter(output, fieldnames=name)
        writer.writeheader()
        for row in array:
            writer.writerow({'ip':row[0], 'city':row[1]})
    output.close()
    pass

def sortIP(IPList):
    """(25 pt) Sort the list with each IPs and return the sorted list of dictionary
    
    IPList : the list of dictionary generated with readIPData()
    
    """
    IPList.sort(key = lambda k:(ipaddress.ip_address(k.get('ip', 0))))
    return IPList
    pass

def binarySearch(array, IP, start, end):
    """(25 pt) perform binary search on a sorted list of dictionaries
    
    return the city of specified IP 
    return -1 if query IP not found
    
    """
    # 範例: ipaddress.ip_address('192.0.2.2')
    front = start
    back = end
    
    while back >= front:
        mid = int((front+back)/2)
        
        if ipaddress.ip_address(array[mid]['ip']) < ipaddress.ip_address(IP):
            front = mid+1
            
        elif ipaddress.ip_address(array[mid]['ip']) > ipaddress.ip_address(IP):
            back = mid-1
            
        else:
            return array[mid]['city']
    return -1
    
    pass

def test_hw2(raw, query, ans):
    """
    combine above works
    (20 pt) if your script complete in 3 seconds 

    """
    db = readIPData(raw)
    query = readQuery(query)
    sortedIP = sortIP(db)
    response = []
    for q in query:
        r = binarySearch(sortedIP, q, 0, len(sortedIP))
        response.append([q, r])
    writeAns(response, ans)

if __name__ == "__main__":
    test_hw2(sys.argv[1], sys.argv[2], sys.argv[3])
