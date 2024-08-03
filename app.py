from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def check_file():
    video_path = 'video.mp4'
    if os.path.exists(video_path) and os.access(video_path, os.R_OK):
        return "فایل با موفقیت قابل خواندن است."
    else:
        return "فایل قابل خواندن نیست."

if __name__ == '__main__':
    app.run()
