import os
import sys
import json
import shutil 
import Handlers as HD
from googleapiclient.discovery import build

KEY = str(HD.readConfig('Youtube','api'))
youtube = build('youtube', 'v3' , developerKey= KEY )

def start():
    print('Video was called')
    while True:
        print('1. For seeing something new in your favorite channel')
        print('2. For adding a channel to your favorite list ')
        print('3. To delete some channel')
        print('4. To view your subscribed channel')
        # print('5. To show current stored videos')
        print('5. Exit')
        
        choice = int(input('What you have in your mind??\n'))
        
        if choice==1:
            show_new_videos()
        elif choice==2:
            name = input('Enter the exact channel name\n')
            add_channel(name)
        elif choice==3:
            name=input('Enter the exact channel name\n')
            delete_channel(name)
        elif choice==4:
            show_channels()
        elif choice == 5:
            break
        else:
            print('Your Bad!! You entered something wrong')
            continue
        
#----Add new channel name to file----#

def add_channel(channel_name):
    res = youtube.search().list(q=channel_name, part='id', type='channel').execute()
    channel_id = res['items'][0]['id']['channelId']
    if not os.path.isfile('Data/channel_list.txt') :
        HD.writeFile('Data/channel_list.txt',channel_id)
    else:
        channel_list = fileToSet('Data/channel_list.txt')
        channel_list.add(channel_id)
        HD.setToFile(channel_list,'Data/channel_list.txt')

#----Delete a channel from list file----#

def delete_channel(channel_name):
    if not os.path.isfile('Data/channel_list.txt'):
        print("Channel list is empty")
        return

    res = youtube.search().list(q=channel_name, part='id', type='channel').execute()
    channel_id = res['items'][0]['id']['channelId']
    channel_list = HD.fileToSet('Data/channel_list.txt')
    
    if channel_id in channel_list:
        channel_list.remove(channel_id)
        print('Your channel '+ channel_name + ' with channel Id '+ channel_id+ ' is deleted')
        HD.setToFile(channel_list,'Data/channel_list.txt')
        shutil.rmtree('Data/'+channel_name)
    else:
        print('Your channel was not found!!')

#----Show your favorite cannel----#

def show_channels():

    if not os.path.isfile('Data/channel_list.txt'):
        print('Channel list file does not exist')
        return
    
    channel_list=fileToSet('Data/channel_list.txt')
    
    if len(channel_list)==0:
        print('There are no stored channel Id in the file channel_list.txt')
        return
    
    for channel in channel_list:
        res = youtube.search().list(q=channel, part='snippet', type='channel').execute()
        print('Channel Name: '+res['items'][0]['snippet']['title'] + ' \t\t\tChannel Id: '+res['items'][0]['snippet']['channelId'])

#----Extract all the videos of a particular channel by using the channel id----#

def get_channel_videos(channel_id):
    res = youtube.channels().list(id=channel_id,part='contentDetails').execute()
    playlist_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    videos = []
    next_page_token = None
    
    while 1:
        res = youtube.playlistItems().list(playlistId=playlist_id,part='snippet',maxResults=50, pageToken=next_page_token).execute()
        videos += res['items']
        next_page_token = res.get('nextPageToken')
        
        if next_page_token is None:
            break
    
    return videos

#----Extract each channel from file and print its latest 50 videos----#

def show_new_videos():
    if not os.path.isfile('Data/channel_list.txt'):
        print('channel_list.txt doesnot exist ')
        return
    
    channel_list = HD.fileToSet('Data/channel_list.txt')
    
    if len(channel_list) == 0:
        print('Your Channel list is empty!! First add some channel')
        return
    
    for channel in channel_list:
        res = youtube.search().list(q=channel, part='snippet', type='channel').execute()
        dir_path = 'Data/'+res['items'][0]['snippet']['title']
        create_project_dir(dir_path)
        updated_videos = get_channel_videos(channel)
        updated_videos = sorted(updated_videos,key= lambda x:x['snippet']['publishedAt'],reverse=True)
        updated_videos = updated_videos[0:50]
        file_path = dir_path + '/data.json'
        
        if not os.path.isfile(file_path):
            with open(file_path,'w') as f:
                json.dump(updated_videos,f)
                f.close()
        
        with open(file_path) as f:
            old_videos = json.load(f)
            f.close()

        if(updated_videos == old_videos):
            print('There are no new videos for channel name = '+res['items'][0]['snippet']['title'])
            print('Showing last five uploaded videos')
            videos = old_videos[0:5]
            
            for video in videos:
                print('Name:' + video['snippet']['title'] + '\t\tvideo Link: https://www.youtube.com/watch?v=' + video['snippet']['resourceId']['videoId'])
        else:
            with open(file_path,'w') as f:
                json.dump(updated_videos,f)
                f.close()
            print('The new videos for channel :'+res['items'][0]['snippet']['title'] + ' are:')
            new=0
            
            while True:
                if updated_videos[new]['id']==old_videos[0]['id']:
                    break
                else:
                    print('Name:' + updated_videos[new]['snippet']['title'] + '\t\tvideo Link: https://www.youtube.com/watch?v=' + updated_videos[new]['snippet']['resourceId']['videoId'] + '\t\tChannel Name: ' + updated_videos[new]['snippet']['channelTitle'])
                    new=new+1
