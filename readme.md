Here's the cleaned-up markdown version of the document:

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

## Usage

Run the script from the command line:

```bash
python dedupe_detective.py [folder_path] [-r]
```

### Options

- **`[folder_path]`**: Optional. The directory to scan. If not provided, the current directory will be scanned.
- **`-r` or `--recursive`**: Optional. If included, the script will scan the specified directory and all its subdirectories.

### Examples

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

### Simulation

```
Welcome to DeDupe Detective: The File Doppelgänger Sleuth!
--------------------------------------------------------

Investigating files in: /mnt/e/Downloads
Recursive mode: Off

Suspicious doppelgängers detected:

Doppelgänger group with fingerprint 5ce5fee0fa882375d30e384ade3d2a38:
  🔍 /mnt/e/Downloads/all-in-one-video-gallery.2.6.1/all-in-one-video-gallery/includes/loader.php
  🔍 /mnt/e/Downloads/all-in-one-video-gallery.3.3.0/all-in-one-video-gallery/includes/loader.php

Doppelgänger group with fingerprint 077f21f31fab2e6648d1e4ecc3d44617:
  🔍 /mnt/e/Downloads/all-in-one-video-gallery.2.6.1/all-in-one-video-gallery/includes/roles.php
  🔍 /mnt/e/Downloads/all-in-one-video-gallery.3.3.0/all-in-one-video-gallery/includes/roles.php

Doppelgänger group with fingerprint d0acb0dcb7bd84853ac6a9ec27ea1b18:
  🔍 /mnt/e/Downloads/all-in-one-video-gallery.2.6.1/all-in-one-video-gallery/includes/walker-terms-checklist.php
  🔍 /mnt/e/Downloads/all-in-one-video-gallery.3.3.0/all-in-one-video-gallery/includes/walker-terms-checklist.php

...

Shall we eliminate the duplicates, detective? (yes/no):
...
Mission accomplished! Duplicate files have been eliminated.
Total space freed: 2.5 MB

Thank you for using DeDupe Detective. Case closed!
```
