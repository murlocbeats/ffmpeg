import os

# نام فایل
file_path = "example.txt"

# متنی که می‌خواهیم بنویسیم
content = "این یک متن ساده است."

# بررسی اینکه آیا فایل وجود دارد یا خیر
if not os.path.exists(file_path):
    # ایجاد و نوشتن در فایل
    with open(file_path, "w") as file:
        file.write(content)
    print(f"فایل '{file_path}' ایجاد شد و متن در آن نوشته شد.")
else:
    print(f"فایل '{file_path}' از قبل وجود دارد.")
