'''
yt-dataset-gen.py

Name: Ersun Erdem
Date: 4/15/2022
Desc: Scrape info from youtube to generate pool of data, to then train AI model.
'''


import os
from dotenv import load_dotenv
import googleapiclient.discovery
from bs4 import BeautifulSoup

#Constants

#File name for the training data
training_fn = "training_data.txt"
#File name for test data
test_fn = "test_data.txt"
#File name for all youtube data
yt_fn = "youtube_data.txt"
#Number for test, rest will go into training
#A constant I will use to replace newline, and then re-edit so I don't mess up the csv
const_newline_mod = '*^_NEWLINE^_*'

#Number of all collected data that will go into test... rest into training!
test_num = 40

load_dotenv()
#Make sure you create a .env file with GOOGLE_API_KEY!
API_KEY = os.getenv('GOOGLE_API_KEY')
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "flash-audio-246217-69942b334b63.json"


#Search will only return a max of 50... use nextPageToken to find more in batches of 50
def search_and_scrape(term, **kwargs):
    yt = googleapiclient.discovery.build('youtube', 'v3', developerKey=API_KEY)
    video_list = yt.search().list(q=f"{term}", order='viewCount', part='snippet', **kwargs).execute()
    all_videos = video_list['items']
    print(f"Found {len(video_list['items'])} videos.")
    f = open(yt_fn, 'a', encoding='utf-8')
    
    while(video_list.nextPageToken):
        print(f"Found {len(video_list['items'])} more videos.")
        video_list = yt.search().list(q=f"{term}", order='viewCount', part='snippet', pageToken=video_list.nextPageToken, **kwargs).execute()
        for i in video_list:
            all_videos.append(i)
    
    for video in all_videos:
            print(video['snippet']['description'])
            title = video['snippet']['title']
            desc = video['snippet']['description']
            mod_desc = desc.replace('\n', const_newline_mod)
            f.write(title)
            f.write("\n")
            f.write(mod_desc)
            f.write("\n")
    f.close()



def search():
    #List of strings to search for
    to_search = ['sidemen','ksi','miniminter','tbjzl','zerkaa','vikkstar123','w2s','behzinga','willne','chrismd']
    for term in to_search:
        print(f"Searching term {term} in YouTube.")
        search_and_scrape(term, maxResults=250)


def split_data():
    f = open(yt_fn, 'r', encoding='utf-8')
    test_out_file = open(test_fn, 'w', encoding='utf-8')
    training_out_file = open(training_fn, 'w', encoding='utf-8')
    #This index would normally start at 0, but notepad starts at line 1. Want to stay consistent
    cur_line = 1
    video_num = 0
    for line in f:
        #Work with titles only... this must be a title
        if(cur_line % 2 == 1):
            if(video_num < test_num):
                test_out_file.write(line)
            else:
                training_out_file.write(line)
            video_num += 1
        cur_line += 1
    f.close()
    test_out_file.close()
    training_out_file.close()




def start():
    #search()
    split_data()



#Start the program
start()