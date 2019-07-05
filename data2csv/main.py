import os
import re
from tqdm import tqdm
class data2csv(object):
    def __init__(self,Proj):
        self.Proj = Proj
        self.filename = Proj+'.txt'
        self.data = {}
        self.key_GRA = []
        self.key_INCOME = []
    def get_data(self):
        data={'DATE':[],
              'CITY':[],
              'LNG':[],
              'LAT':[],
              'GRA':[],
              'INCOME':[]
              }
        key_GRA = []
        key_INCOME = []
        try:
            f=open(self.filename,encoding='UTF-8')
            for line in f:
                line = line[0:-1]
                line = re.split(r",(?![^{]*\})", line)
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
            f.close()
        except Exception as e:
            print('Error: %s ',e.args)

        self.data = data
        self.key_GRA = key_GRA
        self.key_INCOME = key_INCOME
        return
    def write_file(self):
        outfilename = self.Proj+'.csv'
        key_GRA = self.key_GRA
        key_INCOME = self.key_INCOME
        data = self.data
        with open(outfilename, 'w+') as f:
            f.write('DATE,CITY,LNG,LAT')
            for item in key_GRA:
                f.write(',' + str(item))
            for item in key_INCOME:
                f.write(',' + str(item))
            f.write('\n')
            for i in tqdm(range(len(data['DATE'])),desc='Writing file:', ncols=100):
                f.write(data['DATE'][i] + ',')
                f.write(data['CITY'][i] + ',')
                f.write(data['LNG'][i] + ',')
                f.write(data['LAT'][i] + ',')
                for item in key_GRA:
                    try:
                        val = data['GRA'][i][item]
                        f.write(str(val) + ',')
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
                        f.write(str(val) + ',')
                f.write('\n')
        f.close()
        return
    def process(self):
        self.get_data()
        self.write_file()
        print('Project %s is Finished.', self.Proj)

if __name__ == '__main__':
    path=os.path.abspath(os.path.dirname(os.getcwd()))
    NAMES = ['baoding_userpic',
             'zhangjiakou_userpic',
             'xintai_userpic',
             'tianjin_userpic',
             'tangshan_userpic',
             'shijiazhuang_userpic',
             'qinhuangdao_userpic',
             'langfang_userpic',
             'hengshui_userpic',
             'handan_userpic',
             'chengde_userpic',
             'cangzhou_userpic',
             'beijing_userpic'
             ]
    for name in NAMES:
        print('Processing:',name)
        run = data2csv(path+'\\'+name)
        run.process()
    print('finish')