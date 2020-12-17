# TwitchVotingWithOBS
Twitchコメントによる投票機能 for DJxDJ  
  
[オンラインDJバトル　DJxDJ アーカイブ(Twitch)](https://www.twitch.tv/videos/826506802)

# Usage🐰
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

## 4. Twitchコマンド入力
(master)と書いてある物は`MASTER_ID`に該当するアカウントのみで実行されます。
※commanf_prefixは`!`とする

|コマンド|説明|
| ---- | ---- |
| !ready | (master)各ラウンド一番最初に実行するコマンド、スコアの初期化を行う |
| !timeup | (master)各ラウンド終了時に実行するコマンド、スコアの確定と保存を行う |
| !total | (master)現時点の合計得点を出力する |
| !red or !blue | 各チームに投票するコマンド、readyコマンド後のみ反映される |

