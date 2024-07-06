class Config(object):
    LOGGER = True
    API_ID = 22122061
    API_HASH = 385b7993c2545e1abf8f18eaf4b51d9c
    TOKEN = 7081234335:AAENPFHX43yJbVK0x0p_KL3PQM3-YGMPqd4
    OWNER_ID= 7081234335
    
    SUPPORT_CHAT = @arshuu_69
    START_IMG = ""
    EVENT_LOGS = -1002195635749
    MONGO_DB_URI= mongodb+srv://Krishna:pss968048@cluster0.4rfuzro.mongodb.net/?retryWrites=true&w=majority
   
    DATABASE_URL = ""  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        ""
    )
    TIME_API_KEY = ""

    
    BL_CHATS = [] 
    DRAGONS = []
    DEV_USERS = []  
    DEMONS = [] 
    TIGERS = []  
    WOLVES = [] 

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
