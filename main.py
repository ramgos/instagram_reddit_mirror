from instagrapi import Client
from PIL import Image
from pathlib import Path
from time import sleep
import requests
import praw
import json
import random
import os
import io

record = "post_ids.txt"
secret = "info.json"

# turn any picture into a square


def make_square(im, min_size=256, fill_color=(0, 0, 0, 0)):
    x, y = im.size
    size = max(min_size, x, y)
    new_im = Image.new('RGB', (size, size), fill_color)
    new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
    return new_im


def square_and_save(name, image_link):
    image = requests.get(image_link)
    image_bytes = io.BytesIO(image.content)
    image_pil = Image.open(image_bytes)
    image_pil = make_square(image_pil)
    image_pil.save(name)

# reading secret information regarding instagram and reddit client


with open(secret) as json_file:
    info = json.load(json_file)
reddit_info = info["RedditInfo"]
instagram_info = info["InstagramInfo"]

reddit = praw.Reddit(
    client_id=reddit_info["client_id"],
    client_secret=reddit_info["client_secret"],
    user_agent=reddit_info["user_agent"],
    username=reddit_info["username"],
    password=reddit_info["password"]
)

subreddit = reddit.subreddit(reddit_info["subreddit"])
instagram_client = Client()
instagram_client.login(instagram_info["username"], instagram_info["password"])


def post():
    feed = subreddit.hot(limit=10)
    for submission in feed:
        if submission.is_video:
            continue
        if submission.pinned:
            continue
        if submission.over_18:
            continue
        submission_info = vars(submission)
        try:
            post_id = str(submission_info['id'])
            lines = []

            with open(record, 'r+') as history:
                for line in history:
                    lines.append(line.rstrip('\n'))
                if post_id not in lines:
                    history.write(post_id)
                    history.write('\n')

            if post_id in lines:
                continue

            title = str(submission_info['title'])
            author = str(submission_info['author'])
            image_link = str(submission_info['url'])
            permalink = str(submission_info['permalink'])
            name = post_id + '.jpg'

            square_and_save(name=name, image_link=image_link)

            try:
                tags = open("tags/" + random.choice(os.listdir("tags"))).read()
            except:
                tags = ""
            caption = '"{title}"\n posted by: {author} (on reddit)\n https://reddit.com{permalink} \n*\n*\n*\n {tags}'\
                .format(title=title, author=author, permalink=permalink, tags=tags)
            instagram_client.photo_upload(path=Path(name), caption=caption)

            os.remove(Path(name))

            break
        except KeyError as e:
            print(e.args[0] + " key missing")


while True:
    post()
    sleep(3600)
