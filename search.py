from googleapiclient.discovery import build
import pandas as pd
from key import key
import organized as o
import sys


# Set up the YouTube Data API client with API key authentication
youtube = build('youtube', 'v3', developerKey=key)


def video_info(keyword, max_videos, result_type):
    # Search for for videos
    search_response = youtube.search().list(
        q=keyword,
        type=result_type,
        part='id,snippet',
        maxResults=max_videos
    ).execute()

    # Extract the list of videos from the search response
    videos = search_response['items']

    # Iterate through the list of videos and return the title, link, and view count of each video
    # then append it to a list
    list_of_names = []
    list_of_views = []
    list_of_links = []

    for i in range(max_videos):
        video_id = videos[i]['id']['videoId']

        youtube_link = "https://www.youtube.com/watch?v=" + video_id

        video_response = youtube.videos().list(
            part='statistics',
            id=video_id
        ).execute()

        view_count = int(video_response['items'][0]['statistics']['viewCount'])

        title = videos[i]['snippet']['title']

        list_of_names.append(title)
        list_of_views.append(view_count)
        list_of_links.append(youtube_link)

    # Sort the video views in descending order
    sorted_views = o.ordered(list_of_views)
    sorted_names = []
    sorted_links = []

    for views in sorted_views:
        index = list_of_views.index(views)
        sorted_names.append(list_of_names[index])
        sorted_links.append(list_of_links[index])

    # Reverse the list to get the top videos first
    sorted_names.reverse()
    sorted_views.reverse()
    sorted_links.reverse()

    print("\nHere are the top videos:\n")

    total = len(sorted_views)

    i = 0

    while i < total:
        print(
            f'{sorted_names[i]} ({sorted_links[i]}) ({sorted_views[i]} views)')
        i += 1

    message = input("\nDo you want a list of the links? (y/n) ")
    p_message = message.lower()

    if p_message == "y":
        print("")
        for links in sorted_links:
            print(links)

    else:
        next_message = input("\nDo you want to see it in a table? (y/n) ")
        p_next = next_message.lower()

        if p_next == "y":

            df = pd.DataFrame({
                "Links": sorted_links,
                'Views': sorted_views,
                'Names': sorted_names,
            }
            )

            # display all rows and columns
            pd.set_option('display.max_rows', None)
            pd.set_option('display.max_columns', None)

            print("")
            print(df)
