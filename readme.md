# DeDupe Detective: The File Doppelgänger Sleuth

**Is your Downloads folder always full? Tired of manual cleanup? Meet DeDupe Detective, the ultimate solution for duplicate file detection!** This Python script helps you identify and manage duplicate files across your system, freeing up valuable storage space. It works seamlessly on macOS, Windows, Linux, and more, making it an essential tool for keeping your digital life organized.

## Key Benefits

- **Effortless Cleanup**: Automatically detect and remove duplicate files, saving you time and effort.
- **Space Optimization**: Free up storage space by eliminating unnecessary file copies.
- **Cross-Platform Compatibility**: Works on macOS, Windows, Linux, and other operating systems.
- **User-Friendly**: Simple command-line interface with clear instructions and feedback.
- **Safe and Secure**: Only deletes duplicates after user confirmation, ensuring your important files are safe.

## Features

- **Efficient Scanning**: Scan files in the current directory or recursively through all subdirectories.
- **Accurate Detection**: Use MD5 hashing to identify duplicate files, ensuring accuracy even if file names differ.
- **User Interaction**: Present detected duplicates and provide an option to delete unwanted copies.
- **Flexible Operation**: Choose between scanning just the current directory or including all subdirectories.

## Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/rasrobo/dedupe-detective.git
cd dedupe-detective
```

# Usage

Run the script from the command line:

```bash
python dedupe_detective.py [folder_path] [-r]
```

## Options

- **`[folder_path]`**: Optional. The directory to scan. If not provided, the current directory will be scanned.
- **`-r` or `--recursive`**: Optional. If included, the script will scan the specified directory and all its subdirectories.

## Examples

1. **Scan the current directory**:
   ```bash
   python dedupe_detective.py
   ```

2. **Scan a specific directory**:
   ```bash
   python dedupe_detective.py /path/to/directory
   ```

3. **Scan a directory recursively**:
   ```bash
   python dedupe_detective.py /path/to/directory -r
   ```
```
