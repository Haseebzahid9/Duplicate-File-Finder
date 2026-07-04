# Duplicate File Finder

Duplicate File Finder is a Python-based command-line utility designed to scan directories recursively, identify duplicate files by comparing their contents, and generate a clear report that helps users reclaim unnecessary storage space. The program uses cryptographic hashing to ensure that files are considered duplicates only when they are truly identical, regardless of filename differences.

## Objectives

The primary objectives of this project are to:

- Detect duplicate files in a selected folder or directory tree
- Compare files based on content rather than filename
- Support recursive scanning of nested folders
- Generate a readable report of duplicate groups and affected files
- Provide a simple and practical example of file handling, hashing, and CLI application design in Python
- Demonstrate clean project organization suitable for GitHub and educational purposes

## Project Description

In many systems, duplicate files accumulate over time in locations such as Downloads, Documents, Images, Backups, and shared folders. These duplicates often remain unnoticed because the files may have different names, timestamps, or folder locations. This project addresses that issue by scanning a target directory, reading each file, and computing a SHA-256 hash for its contents.

Files that share the same hash are treated as duplicates. The program then reports the duplicate groups and the amount of space that could potentially be recovered.

## Key Features

- Recursive directory traversal using Python’s file system tools
- Content-based comparison using SHA-256 hashing
- Ignoring empty files during the scan
- Detection of duplicate files even when file names differ
- Console-based duplicate report output
- Saving duplicate findings to a text report file
- Simple command-line interface for ease of use
- No external dependencies required

## Requirements

The following requirements are needed to run this project successfully:

- Python 3.8 or higher
- A compatible operating system such as Windows, Linux, or macOS
- Basic terminal or command prompt access
- Sufficient read permissions to scan the selected folder

## Installation

1. Clone the repository from GitHub:
   ```bash
   git clone https://github.com/Haseebzahid9/Duplicate-File-Finder.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Duplicate-File-Finder
   ```
3. Ensure Python is installed and available in your PATH.

## How to Run

### Run the program on a folder

```bash
python duplicate_finder.py --path C:/path/to/folder
```

### Save the report to a custom output file

```bash
python duplicate_finder.py --path C:/path/to/folder --output reports/my_report.txt
```

### Run the sample demo included in the repository

```bash
python duplicate_finder.py --path sample_files
```

## Usage Example

Suppose a folder contains the following files:

- photo.jpg
- photo_copy.jpg
- notes.pdf
- copy_notes.pdf

Although the filenames differ, the program will detect that the files share identical content and report them as duplicates.

## Technologies Used

This project is built using the following Python modules and standard libraries:

- Python 3
- os for directory traversal
- pathlib for path handling
- hashlib for SHA-256 hashing
- argparse for command-line arguments
- typing for type hints

## Project Structure

```text
Duplicate-File-Finder/
├── duplicate_finder.py
├── hash_utils.py
├── scanner.py
├── report.py
├── config.py
├── sample_files/
├── reports/
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

## Workflow

The program follows this general workflow:

1. Accept a target folder path from the user
2. Scan the directory recursively for files
3. Skip empty files
4. Compute a SHA-256 hash for each non-empty file
5. Group files by hash value
6. Identify groups that contain more than one file as duplicates
7. Display the results in the terminal
8. Save the report to a text file in the reports directory

## Example Output

```text
====================================
Duplicate File Finder
====================================
Scanned path: ...
Files scanned: 5
Duplicate groups: 2
Duplicate files: 4
Space wasted: 60 B
```

## Notes

- The program compares file contents, not names.
- This makes it reliable for detecting mirrored or renamed duplicate files.
- It is suitable for personal use, file organization, and educational demonstrations.

## Author

Made by Haseeb Zahid

GitHub: https://github.com/Haseebzahid9

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contribution

Contributions, improvements, and suggestions are welcome. If you would like to contribute, please open an issue or submit a pull request.
