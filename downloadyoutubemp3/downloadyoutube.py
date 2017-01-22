from __future__ import unicode_literals
import youtube_dl
import boto3
import os


url = "https://www.youtube.com/watch?v=LvwQDenTgw8"
bucket='lambda-youtube-mp3'
region = "us-west-2"
client= boto3.client('s3')

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

def upload(d):
	filename = "{0}-{1}.mp3".format(str(d['title']), str(d['id']))
	filepath = "/tmp/{0}".format(filename)
	client.upload_file(filepath, bucket, filename)
	client.put_object_acl(ACL='private', Bucket=bucket, Key=filename)
	return "https://s3-{0}.amazonaws.com/{1}/{2}".format(region, bucket, filename)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')
        

def run(event, context):
	url = event[url] ### Need to be changed for Api Gateway POST request
	ydl_opts = {
    'outtmpl': '/tmp/%(title)s-%(id)s.%(ext)s',
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
    'ffmpeg_location': 'ffmpeg/',
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        #ydl.download([url])
        ydl.add_default_info_extractors()
        info = ydl.extract_info(url, True)
    response = upload(info)
    return { "url" : response }
