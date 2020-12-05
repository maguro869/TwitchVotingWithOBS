# obs-websocket-pyのパラメータ
HOST = 'localhost'      # ローカル環境ならlocalhostでOK
PORT = 4444             # OBSWebsocketに設定したサーバーポート
PASSWORD = 'password'   # OBSWebsocketに設定したパスワード

# TwitchIOのパラメータ
# 各パラメータの取得方法は https://qiita.com/maguro869/items/57b866779b665058cfe8 を参考にしてください
TMI_TOKEN = 'oauth:xxxxxxxxxxxxxxxxxxxx'
CLIENT_ID = 'xxxxxxxxxxxxxxxxxxxxxxxxxx'
BOT_NICK = 'twitch_bot_id'
BOT_PREFIX = '!'
CHANNEL = ['twitch_id']

# TwitchVotingWithOBSのパラメータ
MASTER_ID = 'master_twitch_id' # botの管理者権限を持つTwitchのアカウントのID(恐らくあなた) 