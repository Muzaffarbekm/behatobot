from environs import Env

# environs lib
env = Env()
env.read_env()

# read these 3 things from .env
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot token
ADMINS = env.list("ADMINS")  # list of admins
IP = env.str("ip")  # Hosting address
