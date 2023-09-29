from AnonXMusic.core.bot import Anony
from AnonXMusic.core.dir import dirr
from AnonXMusic.core.git import git
from AnonXMusic.core.userbot import Userbot
from AnonXMusic.misc import dbb, heroku

from .logging import LOGGER

PH_ON = ["https://telegra.ph/file/e5b252be0c8674312f8de.jpg", "https://telegra.ph/file/0aef66a3700da291ce500.jpg", "https://telegra.ph/file/39c569f8609a3dbf58b50.jpg", "https://telegra.ph/file/277d551ca262772ce54bb.jpg", "https://telegra.ph/file/907d0db309c3343b3c2eb.jpg", "https://telegra.ph/file/c2ad64ecf373f9b92a7df.jpg", "https://telegra.ph/file/6f8116af831fdcd878f8f.jpg", "https://telegra.ph/file/722c26f90c499751ce899.jpg", "https://telegra.ph/file/fcf53f590dddab080293d.jpg", "https://telegra.ph/file/e01f211dba12ea04eba30.jpg"]

from config import (
    API_HASH,
    API_ID,
    BOT_TOKEN,
    MONGO_DB_URI,
    LOGGER_ID,
    OWNER_ID,
    COMMAND_HANDLER,
    SUPPORT_CHANNEL,
    SUPPORT_CHAT,
    )

dirr()
git()
dbb()
heroku()

app = Anony()
userbot = Userbot()

GB =["https://telegra.ph/file/c06d6e3a3abacecf36427.mp4"]

OP = ["https://graph.org/file/ba8d4fb6d3410bbbe1dfc.jpg" , "https://graph.org/file/4c0be5dc3f741bbca04fa.jpg" , "https://graph.org/file/fc4ab06c07e1cc4ba96b0.jpg" , "https://graph.org/file/4466e0a16e28ac94212a2.jpg" , "https://graph.org/file/f2f1f01676b6a8ea5e8a2.jpg" , "https://graph.org/file/9a3e0e44a046af159dc6a.jpg" , "https://graph.org/file/6607c444b4aec00d6d591.jpg"]

from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
