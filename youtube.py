# imports
import sys
from pytube import YouTube


# program
def main():
    s = 0
    m = 0
    h = 0

    yt = YouTube(input('inter your youtube link:  '))
    print("------------------ \n")

    # gets the video info
    title = yt.title
    length = yt.length  # int
    rating = yt.rating  # float
    author = yt.author
    description = yt.description
    views = yt.views  # int

    # prints video info
    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"Rating: {round(rating, 2)}")
    print(f"Views: {views:,}")

    # formats the length of the video h:m:s
    if length >= 3600:
        h = length // 3600
        m = (length % 3600) // 60
        s = (length % 3600) % 60
        print(f"length: {h}:{m}:{s}")
    elif 60 <= length < 3600:
        m = length // 60
        s = (length // 60) % 60
        print(f"length: {h}:{m}:{s}")
    else:
        s = length
        print(f"length: {h}:{m}:{s}")

    print(f"Description: {description} \n\n------------------")

    # download part
    dl = input("do you want to download this video? y/n   ").lower()

    if dl == "y":
        allStreams = yt.streams
        print(*allStreams, sep="\n")
    else:
        sys.exit()

    # gets the video itag and downloads it
    itag = input("\n\nplease enter the itag of the video:  ")
    stream = yt.streams.get_by_itag(itag)
    stream.download("youtube")
    print("Video Downloaded!")

    # reloads the program
    reload = input("do you want to run the program again? y/n  ").lower()
    main() if reload == "y" else sys.exit()


# runs the program
main()


# some other features of pytube:

# print(yt.streams.all())
# yt.streams.filter(progressive=True).all() # only progressive streams (acodec and vcodec are not seprated, max quality = 720p)
# yt.streams.filter(adaptive=True).all() # only DASH streams (acodec and vcodec are seprated, better quality)
# yt.streams.filter(only_audio=True).all()
# yt.streams.filter(file_extension='mp4').all()
# yt.streams.get_by_itag('22')
# yt.captions.all() # shows all available captions
# caption = yt.captions.get_by_language_code('en') # gets the English caption
# caption.generate_srt_captions() # generates .srt version of captions
