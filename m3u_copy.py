import shutil
import sys
import os
import argparse


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "-infile", required=True, help="Path to playlist file")
    parser.add_argument("-o", "-outfile", required=True, help="Directory for copies of files")
    return parser.parse_args().i, parser.parse_args().o


def copy_audiofiles(playlist_path, copy_path):
    fh = None
    try:
        fh = open(playlist_path, encoding='cp1251')
        music_dir = playlist_path[:playlist_path.rfind('/')+1] or playlist_path[:playlist_path.rfind('\\')+1]
        for line in fh:
            if not line.startswith('#'):
                line = line.replace('\n', '')
                mp3_path = music_dir + line
                shutil.copy(mp3_path, copy_path)
    except EnvironmentError as err:
        print("{0}: export error: {1}".format(os.path.basename(sys.argv[0]), err))
    finally:
        if fh is not None:
            fh.close()


def main():
    playlist_path, copy_path = parser()
    copy_audiofiles(playlist_path, copy_path)


if __name__ == "__main__":
    main()