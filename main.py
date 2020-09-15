from OBS import OBS
from bot import Bot
from config import *

if __name__ == "__main__":
    obs = OBS(HOST,PORT,PASSWORD)
    bot = Bot(TMI_TOKEN,CLIENT_ID,BOT_NICK,BOT_PREFIX,CHANNEL,obs)
    bot.run()