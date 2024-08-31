# nokogen
確率に基づき文章を生成します  
影響を受けた動画: https://www.youtube.com/watch?v=Xkq13ZthmA0  

## 環境
* 任意の名前で仮想環境を構築してください  
* `pip install -r requirements.txt` で環境を構築できます  
* `config.yaml.template` -> `config.yaml`に変更し、中身を書き換えてください  
* 常時実行を行う場合は`nohup`オプションを利用してください

## 使い方
* `src/main.py`: 生成した文をMisskeyに投稿するプログラム  
* `src/special.py`: 任意の回数文章を生成するプログラム  

## 注意点
* 利用の際は、Misskey側での投稿間隔に注意してください(デフォルトでは15分間隔になっていますが、設定を変更する場合はよく確認してください)  
* このプログラムを利用して発生した損害について、私(@nw31s)は責任を負いません
