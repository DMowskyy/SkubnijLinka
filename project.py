import sys
import re
import yt_dlp

def main():
    link,file_type = validate_format()
    get_download_options(link,file_type)


def validate_format():
    if len(sys.argv) == 3:
        format = sys.argv[2].lower()
        if validate_url(sys.argv[1]) and format in ("mp3", "mp4"):
            return sys.argv[1],format
        else:
            sys.exit("Invalid Inputs")
    elif len(sys.argv) == 1:
        link = input("Link: ")
        format = input("Format: ").lower()
        if validate_url(link) and format in ("mp3", "mp4"):
            return link , format
        else:
            sys.exit("Invalid format")
    else:
        sys.exit("Invalid format")

def validate_url(link):
    if match := re.search(r"^(https?://www\.)?youtube.com/watch\?v=[\w=_&-]*$",link.replace('"','')):
        return True
    else:
        sys.exit("Invalid Link")


def get_download_options(link, file_type):
    if file_type == "mp3":
        ydl_opts = {
            'format': 'bestaudio/best',
            'cookiefile': 'cookies.txt',
            'js_runtimes': {'node': {}},
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }
    elif file_type == "mp4":
        ydl_opts = {
            'format': 'bv*+ba/b',
            'merge_output_format': 'mp4',
            'cookiefile': 'cookies.txt',
            'js_runtimes': {'node': {}},
        }
    else:
        raise ValueError("Invalid format")

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

if __name__ == "__main__":
    main()
