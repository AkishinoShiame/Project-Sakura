import json
from pprint import pprint

import wget

import os

path = os.getcwd()

def LowLevelDownload(DownLink='',SavPath=''):
    PrograssDownload = wget.download(DownLink, SavPath)
    print('Finished download: ', PrograssDownload)


def ReadJson():
    with open('RawAnimeTorrentList.json') as jsonfile:
        content = json.load(jsonfile)
    return content

if __name__ == "__main__":
    index = 1
    print(path)
    #os.mkdir('RawTorrent')
    for JsonObj in ReadJson():
        # print(JsonObj["NAME"], " | ", JsonObj["TorrentURL"], " | ", JsonObj["Magnet"])
        print('['+str(index)+']'+JsonObj["TorrentURL"])
        index += 1
        if index > 193:
            LowLevelDownload("https://nyaa.si"+JsonObj["TorrentURL"],path+"\\RawTorrent\\"+JsonObj["TorrentURL"].split('/')[2])
        