'''
from flask import Flask, send_file, abort
import subprocess
import os

app = Flask(__name__)

@app.route('/edit-video', methods=['GET'])
def edit_video():
    input_path = 'video.mp4'
    output_path = 'edited_video.mp4'
    start_time = '00:00:00'
    duration = '00:00:10'
    width = 360
    height = 360

    if os.path.exists(input_path) and os.access(input_path, os.R_OK):
        ffmpeg_path = os.getenv('FFMPEG_PATH', 'ffmpeg')
        # اجرای فرمان ffmpeg برای ویرایش ویدئو
        command = [
            ffmpeg_path,
            '-y',
            '-i', input_path,
            '-ss', start_time,
            '-t', duration,
            '-vf', f'crop={width}:{height}',
            '-c:a', 'copy',
            output_path
        ]
        subprocess.run(command)

        # بررسی اینکه فایل ویرایش‌شده ساخته شده یا نه
        if os.path.exists(output_path):
            return send_file(output_path, as_attachment=True)
        else:
            return "ویرایش فایل ناموفق بود.", 500
    else:
        return "فایل یافت نشد یا قابل خواندن نیست.", 404

if __name__ == '__main__':
    app.run()
'''

from flask import Flask, request, send_file
import subprocess
import os

app = Flask(__name__)

FFMPEG_PATH = 'bin/ffmpeg'
VIDEO_FILE = 'video.mp4'
OUTPUT_FILE = 'output.mp4'

@app.route('/process', methods=['GET'])
def process_video():
    # Define the command to cut the first 10 seconds and resize the video
    command = [
        FFMPEG_PATH,
        '-i', VIDEO_FILE,
        '-ss', '00:00:00',
        '-t', '00:00:10',
        '-vf', 'scale=360:360',
        OUTPUT_FILE
    ]
    
    # Run the command
    subprocess.run(command, check=True)
    
    # Return the processed video file
    return send_file(OUTPUT_FILE, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
