# File Automation Script

This project is a Python-based utility designed to automate the organization of files in the **Downloads** folder. The script categorizes files into different subfolders based on their file types, such as **Images**, **Documents**, **Videos**, **Audio Files**, and more.

## Features

- Automatically organizes files into appropriate folders:
  - Images (JPEG, PNG, GIF, etc.)
  - Documents (PDF, Word, Excel, etc.)
  - Videos (MP4, AVI, etc.)
  - Code files (Python, HTML, etc.)
  - Compressed files (ZIP, RAR, etc.)
  - Applications (EXE, DMG, etc.)
  - Audio (MP3, WAV, etc.)
- Runs automatically on a scheduled basis (e.g., weekly) using the `schedule` library.
- Ensures no overwriting of files by renaming them if duplicates exist.

## Prerequisites

- Python 3.x
- Libraries used:
  - `os`
  - `shutil`
  - `schedule`

Install the required packages:
```bash
pip install schedule
```

## How to Use

1. Clone the repository to your local machine.
2. Modify the `source_folder` path in the script to point to your **Downloads** folder.
3. Run the script, and it will automatically organize your files on the set schedule (e.g., every Monday).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

