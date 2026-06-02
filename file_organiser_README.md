# 🗂️ Python File Organiser

Automatically organises all files in a folder into subfolders based on file type.

## 📌 What it does
- Scans any folder you give it
- Sorts files into: `Images`, `Documents`, `Videos`, `Audio`, `Code`, `Archives`, `Others`
- Handles duplicate filenames automatically
- Works on Windows, Mac, and Linux

## 🛠️ Requirements
- Python 3.x
- No external libraries needed (uses built-in `os` and `shutil`)

## ▶️ How to run

```bash
python organiser.py
```

Then enter the full path of the folder you want to organise.

**Example:**
```
Enter the full path of the folder to organise:
> C:\Users\YourName\Downloads
```

## 📂 Output example
```
✅ Moved: photo.jpg → Images/
✅ Moved: resume.pdf → Documents/
✅ Moved: song.mp3 → Audio/
✅ Moved: script.py → Code/

📁 Done! 4 files organised, 0 skipped.
```

## 👨‍💻 Author
**Faizal Khan** — Python Developer & Automation Specialist  
[Fiverr](https://www.fiverr.com/faizalpathan369) | [GitHub](https://github.com/faizal911)
