from googleapiclient.discovery import build
import json
from general.general import *
import os


#api_key='AIzaSyCEkNfe79kxdt-nTKXy4fEWn8mJqKTjbo0'
#youtube = build('youtube', 'v3' , developerKey= api_key )

#res = youtube.search().list(q='UCqwUrj10mAEsqezcItqvwEw',part='snippet', type='channel').execute()
#channel=res['items'][0]['snippet']['title']
#print(channel)

list1=[{"kind": "youtube#playlistItem", "etag": "\"SJZWTG6xR0eGuCOh2bX6w3s4F94/acVbXUHjDYvkzB9AJ6qlX9Slb-U\"", "id": "VVVzVmh1SG9iUi1JLTR0Qk5GV2dCS2R3Lkx0VFBpVEprblRn", "snippet": {"publishedAt": "2020-03-01T10:45:49.000Z", "channelId": "UCsVhuHobR-I-4tBNFWgBKdw", "title": "Ink in water 2", "description": "", "thumbnails": {"default": {"url": "https://i.ytimg.com/vi/LtTPiTJknTg/default.jpg", "width": 120, "height": 90}, "medium": {"url": "https://i.ytimg.com/vi/LtTPiTJknTg/mqdefault.jpg", "width": 320, "height": 180}, "high": {"url": "https://i.ytimg.com/vi/LtTPiTJknTg/hqdefault.jpg", "width": 480, "height": 360}, "standard": {"url": "https://i.ytimg.com/vi/LtTPiTJknTg/sddefault.jpg", "width": 640, "height": 480}, "maxres": {"url": "https://i.ytimg.com/vi/LtTPiTJknTg/maxresdefault.jpg", "width": 1280, "height": 720}}, "channelTitle": "Shubham Dixit", "playlistId": "UUsVhuHobR-I-4tBNFWgBKdw", "position": 0, "resourceId": {"kind": "youtube#video", "videoId": "LtTPiTJknTg"}}}]
list2=[{"kind": "youtube#playlistItem", "etag": "\"SJZWTG6xR0eGuCOh2bX6w3s4F94/KLp_8dUlKikKrCIUtdWfcPzAGyo\"", "id": "VVVzVmh1SG9iUi1JLTR0Qk5GV2dCS2R3LkhyUEtkaWFDU2hr", "snippet": {"publishedAt": "2020-03-01T11:13:53.000Z", "channelId": "UCsVhuHobR-I-4tBNFWgBKdw", "title": "Sequence 20", "description": "", "thumbnails": {"default": {"url": "https://i.ytimg.com/vi/HrPKdiaCShk/default.jpg", "width": 120, "height": 90}, "medium": {"url": "https://i.ytimg.com/vi/HrPKdiaCShk/mqdefault.jpg", "width": 320, "height": 180}, "high": {"url": "https://i.ytimg.com/vi/HrPKdiaCShk/hqdefault.jpg", "width": 480, "height": 360}, "standard": {"url": "https://i.ytimg.com/vi/HrPKdiaCShk/sddefault.jpg", "width": 640, "height": 480}, "maxres": {"url": "https://i.ytimg.com/vi/HrPKdiaCShk/maxresdefault.jpg", "width": 1280, "height": 720}}, "channelTitle": "Shubham Dixit", "playlistId": "UUsVhuHobR-I-4tBNFWgBKdw", "position": 0, "resourceId": {"kind": "youtube#video", "videoId": "HrPKdiaCShk"}}}, {"kind": "youtube#playlistItem", "etag": "\"SJZWTG6xR0eGuCOh2bX6w3s4F94/iRNsZ_ZRrjtV0rkWt4JdzW6MgtY\"", "id": "VVVzVmh1SG9iUi1JLTR0Qk5GV2dCS2R3Lkx0VFBpVEprblRn", "snippet": {"publishedAt": "2020-03-01T10:45:49.000Z", "channelId": "UCsVhuHobR-I-4tBNFWgBKdw", "title": "Ink in water 2", "description": "", "thumbnails": {"default": {"url": "https://i.ytimg.com/vi/LtTPiTJknTg/default.jpg", "width": 120, "height": 90}, "medium": {"url": "https://i.ytimg.com/vi/LtTPiTJknTg/mqdefault.jpg", "width": 320, "height": 180}, "high": {"url": "https://i.ytimg.com/vi/LtTPiTJknTg/hqdefault.jpg", "width": 480, "height": 360}, "standard": {"url": "https://i.ytimg.com/vi/LtTPiTJknTg/sddefault.jpg", "width": 640, "height": 480}, "maxres": {"url": "https://i.ytimg.com/vi/LtTPiTJknTg/maxresdefault.jpg", "width": 1280, "height": 720}}, "channelTitle": "Shubham Dixit", "playlistId": "UUsVhuHobR-I-4tBNFWgBKdw", "position": 1, "resourceId": {"kind": "youtube#video", "videoId": "LtTPiTJknTg"}}}]
old=0
new=0
while True:
    if list2[new]['id']==list1[old]['id']:
        break;
    else:
        print(list2[new]['snippet']['title'] )
        new=new+1





