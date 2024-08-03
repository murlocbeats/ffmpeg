import os

# مسیر فایل ویدیویی
video_path = 'video.mp4'

# بررسی وجود و دسترسی به فایل
if os.path.exists(video_path) and os.access(video_path, os.R_OK):
    print("فایل با موفقیت قابل خواندن است.")
else:
    print("فایل قابل خواندن نیست.")
