import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("21581573"))
API_HASH = getenv("554c8781bfff196b38d7ba8e105004d4")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("5879618868:AAEwTncyevKC4-05Ejp1l-Inku8AXgy-3NY")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("mongodb+srv://bsdk:motherchod@cluster0.elanwji.mongodb.net/?retryWrites=true&w=majority", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 10000000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("-1001984925736",))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID",11231132051)

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME",Jatinumusic)
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY",a7a569e1-d592-40af-9766-30e60d4e66df)

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Jatinuzmusic/Anon-Music/master/",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Viral_Reels1m")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/II_LINK_KI_DUNIYA_II")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", true))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 11231132051)
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 11231132051)
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @Jatinuzmusic_bot on Telegram
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/73efddc6cc2de542938e6.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/73efddc6cc2de542938e6.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/73efddc6cc2de542938e6.jpg"
STATS_IMG_URL = "https://telegra.ph/file/73efddc6cc2de542938e6.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/73efddc6cc2de542938e6.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/73efddc6cc2de542938e6.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/73efddc6cc2de542938e6.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/73efddc6cc2de542938e6.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/73efddc6cc2de542938e6.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/73efddc6cc2de542938e6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/73efddc6cc2de542938e6.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/73efddc6cc2de542938e6.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://https://t.me/sub4subgroupethical"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://t.me/jatinzx"
        )
