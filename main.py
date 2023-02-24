import search as s
import sys


if __name__ == '__main__':
    print("\nWelcome to the Youtube Keyword Video Generator!!")
    while True:
        title = input(
            "\nWhat would you like to search?\n(Type 'q' to quit)\n\n")

        if title == 'q':
            sys.exit("")

        maxx = int(input("\nHow many videos? "))
        print('')

        if title != 'q':
            s.video_info(title, maxx, "video")
