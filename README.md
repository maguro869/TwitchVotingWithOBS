# TwitchVotingWithOBS
Twitchコメントによる投票機能 for DJxDJ

# Usage
## 1. 環境作成
### pythonの準備
- このリポジトリをclone
```
git clone https://github.com/maguro869/TwitchVotingWithOBS
```
- 必要なものをインストール
```
pip install obs-websocket-py twitchio
```
### OBSの準備
- [obs-websocket](https://github.com/Palakis/obs-websocket)をOBSにインストール
- OBSからWebsocketのホスト、ポート、パスワードを設定
- RED_SCORE、BLUE_SCOREという名前のテキストソースを作成(それぞれの配置や見た目は各々に任せます)

## 2. config.pyの設定
config.pyに各種パラメータを書く必要があります。  
詳しくはconfig.pyをご覧下さい。

## 3. 実行
- リポジトリのディレクトリに移動して実行
```
py main.py

ONLINE | {bot.nick}
```
