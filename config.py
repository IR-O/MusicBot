from os import getenv

API_ID = int(getenv("API_ID", "24208695"))
API_HASH = getenv("API_HASH", "fa96a7eb2dffe7f4cc8ba1399b68d24d")
BOT_TOKEN = getenv("BOT_TOKEN", "8319239223:AAFlIgIjlEo3rZD3shqvHk3F_0kkf-DZ1OU")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6045293810").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://LUSTIFYXMUSIC:Abhi77394@lustifymusic.evxnqby.mongodb.net/?retryWrites=true&w=majority&appName=LUSTIFYMUSIC")
SESSION_STRING = getenv("SESSION_STRING", "BQFVD0wAfL6rlpVParik224hq_VRptmdycjrhV788nRMGdS_YYt6O25TkJwpbjmgKyfrDAnXnDCrVIJwPjhbuLelWp8UK8voOklIm0CFwlzSnRTxRzWQcJRZTRhuRelr14r5OIw9CqNqCPddJ-N6LkjD9JnOk6TNBv5ubY7X0xmNRJzs_NN4lPsjqpzXV-1LPCciO54fuC2P6TImr81HHs6Y6eX7J8NseA1qaTRbzogOVbnXyWIknboV0XxY5VsxdLl6vdpQ0SiiJYwBFAeLMHd4UI-GtojE6zp71CSyuYCpRbsal66ON6c_qFjKYznpIcjQw1Jhe9gspQYNK3DGTPvZge1NjAAAAAFKEGWjAA")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "https://t.me/iro_bot_support")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/iro_x_support")
