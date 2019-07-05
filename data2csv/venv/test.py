import os
import re
import json
path=os.path.abspath(os.path.join(os.getcwd(),"..\.."))
filename=path+'\\zhangjiakou_userpic.txt'
f=open(filename,encoding='gbk'')
data={'DATE':[],'CITY':[],'LNG':[],'LAT':[],'GRA':[],'INCOME':[]}
count = 0
limit = 10
key_GRA=[]
key_INCOME=[]
for line in f:
    count += 1
    line = line[0:-1]
    line=re.split(r",(?![^{]*\})",line)
    data['DATE'].append(line[0])
    data['CITY'].append(line[1])
    data['LNG'].append(line[2])
    data['LAT'].append(line[3])
    item = eval(line[4])
    for key in item.keys():
        if key not in key_GRA:
            key_GRA.append(key)
    data['GRA'].append(item)
    item = eval(line[5])
    for key in item.keys():
        if key not in key_INCOME:
            key_INCOME.append(key)
    data['INCOME'].append(item)
    if count > limit:
        print('pause')
        break

# process data
outfilename = path+'test.csv'
with open(outfilename,'w+') as f:
    f.write('DATE,CITY,LNG,LAT')
    for item in key_GRA:
        f.write(','+str(item))
    for item in key_INCOME:
        f.write(','+str(item))
    f.write('\n')
    for i in range(len(data['DATE'])):
        f.write(data['DATE'][i]+',')
        f.write(data['CITY'][i]+',')
        f.write(data['LNG'][i]+',')
        f.write(data['LAT'][i]+',')
        for item in key_GRA:
            try:
                val = data['GRA'][i][item]
                f.write(str(val)+',')
            except:
                f.write('0,')
        for item in key_INCOME:
            try:
                val = data['INCOME'][i][item]
            except:
                val = 0
            if item == key_INCOME[-1]:
                f.write(str(val))
            else:
                f.write(str(val)+',')
        f.write('\n')


print('finish')