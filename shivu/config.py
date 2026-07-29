class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "7657218453"
    sudo_users = ["7657218453", "8679737897"]
    GROUP_ID = "-1003087506512"
    TOKEN = "8917618422:AAGy__Venc8MgzdspAp0M6fcfWkZzAnxnYk"
    mongo_url = "mongodb+srv://primarycroll_db_user:n9EHCzsmAf68MsY2@cluster0.ft576pm.mongodb.net/?appName=Cluster0"
    PHOTO_URL = ["https://files.catbox.moe/sgo9in.png", "https://files.catbox.moe/kgcrnb.jpeg"]
    SUPPORT_CHAT = "ANIME_GROUP_HAI"
    UPDATE_CHAT = "SAND_VILLAGE"
    BOT_USERNAME = "AlyaWaifuBot"
    CHARA_CHANNEL_ID = "-1004425617417"
    api_id = "10658015"
    api_hash = "a0087bca748f86698c53d291c9e5b3af"
    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
