import sys
import os
import argparse
import subprocess

def is_virtualenv():
    return hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--info', action='store_true', help='Display virtual environment status and installed packages')
    args = parser.parse_args()

    if args.info:
        if is_virtualenv():
            print("Virtual environment is activated")
            subprocess.call([sys.executable, '-m', 'pip', 'list'])
        else:
            print("Virtual environment is deactivated. To activate, run: source env/Scripts/activate")

if __name__ == "__main__":
    main()
