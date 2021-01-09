# Instagram Reddit Mirror Bot
This bot does exactly what it sounds like it does: It takes posts from subreddits and posts it to instagram. The rest of this document will go over everything you need to run this bot yourself.
### Description:
I made this bot in order to make reposting from reddit easy :) 
the bot has some default parameters:
* Post Every Round Hour
* Filter NSFW Submissions
* Post Submissions from hot

Those all can be changed later by editing ```main.py```, just thought I'd clarify.
It isn't recommended to use your personal reddit and instagram accounts because of rate limits and bot-detecting algorithms. I'd suggest making both a new instagram and reddit account for this project. 
### What Will You Need:
* A Reddit account
* An Instagram account
* Git installed on your computer (a no brainer)
* Docker installed on your machine (and on your VPS if you intend to run it there)
* A Computer that can be left turned on with programs running on it if you want this bot to run all the time

NOTE: This project isn't compatiable with Heroku because Heroku doesn't give you disk space, but rather saves everything to its memory which means that reposts are to be expected after some runtime. I'm not that advanced so if you manage to run it on heroku please bring it up in Issues and tell me how

NOTE2: This Tutorial is more targeted towards begginer developers rather than intermidiate ones. If you have some experience with Docker and programming I would suggest only reading this note and the next section. After that, download this repository, rename ```info_TEMPLATE.json``` to ```info.json``` 
edit the json and enter your credentials there, you can also enter multiple subreddits seperating them with commas (The only confusing credential is user_agent, read about it [here](https://praw.readthedocs.io/en/latest/getting_started/quick_start.html) under "User Agent"). After setting up ```info.json``` open Command Line/Terminal in your current directory and you can immediately start building the docker image since the Dockerfile is already written. Have fun with your bot :)

### Setting Up Your Reddit Application:
After logging into your reddit account from your browser, click on your profile in the top right corner and go to visit old reddit. Then, go to prefrences (It's located right to your username) and in the menu bar enter the Apps tab. 

Click on Create App, give it a name and in the about and redirect links you can just write "https://reddit.com". Click "Create App"

Now you'll be able to see the client_id and client_secret under the name of your app, save those somewhere for in a minute, and you're done setting up your reddit application.

### Downloading This Repository
Download this repository by typing the following command into the Command Line/ Terminal
```git clone https://github.com/ramgos/instagram_reddit_mirror.git```
After your download, open the folder and rename ```info_TEMPLATE.json``` to ```info.json``` and edit the json with a text editor like Notepad++. Enter your credentials into the fields, regarding user_agent - read about it [here](https://praw.readthedocs.io/en/latest/getting_started/quick_start.html) under "User Agent". If you can't bother just write a silly set of characters there and that's good enough.

You can grab from multiple subreddits by seperating them with commas. Also, now is the time to tweak the bot's settings if you want to post from the new feed or change the frequency the bot posts.

### Install Docker (If you haven't already)
I won't explain how to install docker, the [Offical Documentation](https://docs.docker.com/docker-for-windows/install/) is quite good already and very helpful. I'd also highly recommend creating a Docker Hub Account and a private repository over there.
### Creating Your Docker Image and Running it
Open the Command Line/Terminal in the repository folder, and type the following command:
```docker image build -t <docker hub username>/<private repository name>:redditoinstagram .```

If you want to run the bot on your local machine type the following command afterwards:
```docker run -d <docker hub username>/<private repository name>:redditoinstagram```

(You might have to use the "sudo" prefix in unix-based systems like Linux and Mac-OS)

If you have a VPS or another machine in your home you'd like to use, push the image you've created to Docker Hub and pull it from your VPS/other machine and run the same command. If you have no clue what have I jsut said I'd recommend reading the [Get Started Page](https://docs.docker.com/get-started/) over the offical docker docs.


