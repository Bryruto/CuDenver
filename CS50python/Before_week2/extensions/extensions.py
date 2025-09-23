file = input("file name: ").strip().lower()

if "gif" in file or "png" in file or "jpg" in file or "jpeg" in file:
    if "jpg" in file:
        file = file.replace("jpg","jpeg")
    print (f"image/{file.split(".")[-1]}")
elif "pdf" in file or "zip" in file:
    print(f"application/{file.split(".")[-1]}")
elif "txt" in file:
    print(f"text/plain")
else:
    print("application/octet-stream")
