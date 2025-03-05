from pytube import YouTube

def Download(link):
 
 YouTube(link).streams.first().download()
 yt = YouTube(link)
 yt.streams
 ... .filter(progressive=True, file_extension='mp4')
 ... .order_by('resolution')
 ... .desc()
 ... .first()
 ... .download()

Download("https://www.youtube.com/watch?v=u-FC1XQIgkg")