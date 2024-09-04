import os
import sys
import hashlib
import argparse
from collections import defaultdict

def calculate_file_hash(filepath):
    """Calculate the MD5 hash of a file."""
    hasher = hashlib.md5()
    try:
        with open(filepath, 'rb') as file:
            buf = file.read(65536)  # Read in 64kb chunks
            while len(buf) > 0:
                hasher.update(buf)
                buf = file.read(65536)
        return hasher.hexdigest()
    except Exception as e:
        print(f"Error calculating hash for {filepath}: {e}")
        return None

def find_duplicate_files(folder_path, recursive=False):
    """Find duplicate files in the specified folder."""
    hash_dict = defaultdict(list)
    
    if recursive:
        for root, _, files in os.walk(folder_path):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_hash = calculate_file_hash(filepath)
                if file_hash:
                    hash_dict[file_hash].append(filepath)
    else:
        for filename in os.listdir(folder_path):
            filepath = os.path.join(folder_path, filename)
            if os.path.isfile(filepath):
                file_hash = calculate_file_hash(filepath)
                if file_hash:
                    hash_dict[file_hash].append(filepath)
    
    return {hash_value: files for hash_value, files in hash_dict.items() if len(files) > 1}

def delete_files(file_list):
    """Delete the specified files."""
    for file in file_list:
        try:
            os.remove(file)
            print(f"Deleted: {file}")
        except OSError as e:
            print(f"Error deleting {file}: {e}")

def main():
    print("Welcome to DeDupe Detective: The File Doppelgänger Sleuth!")
    print("--------------------------------------------------------")

    parser = argparse.ArgumentParser(description="Detect and manage duplicate files in a specified folder.")
    parser.add_argument("folder", nargs='?', default=".", help="Folder path to scan for duplicates (default: current directory)")
    parser.add_argument("-r", "--recursive", action="store_true", help="Scan subdirectories recursively")
    args = parser.parse_args()

    folder_path = os.path.abspath(args.folder)
    print(f"\nInvestigating files in: {folder_path}")
    print(f"Recursive mode: {'On' if args.recursive else 'Off'}")
    
    duplicates = find_duplicate_files(folder_path, args.recursive)

    if not duplicates:
        print("\nCase closed! No duplicate files found.")
        return

    print("\nSuspicious doppelgängers detected:")
    for hash_value, files in duplicates.items():
        print(f"\nDoppelgänger group with fingerprint {hash_value}:")
        for file in files:
            print(f"  🔍 {file}")

    while True:
        choice = input("\nShall we eliminate the duplicates, detective? (yes/no): ").lower()
        if choice in ['yes', 'no']:
            break
        print("Please enter 'yes' or 'no'.")

    if choice == 'yes':
        for files in duplicates.values():
            # Keep the first file, delete the rest
            delete_files(files[1:])
        print("\nMission accomplished! Duplicate files have been eliminated.")
    else:
        print("\nVery well, detective. The files remain untouched.")

    print("\nThank you for using DeDupe Detective. Case closed!")

if __name__ == "__main__":
    main()