# Clip-rn

## 概要
クリップボードを読み取って改行コードを消したうえでクリップボードに戻すアプリ
改行コードを削除するだけなら[clipGui.py][1], DeepLを使用した翻訳Verは[clipGui2.py][2]へ。
[1]:https://github.com/Gild-shogi/Clip-rn/blob/main/clipGui.py
[2]:https://github.com/Gild-shogi/Clip-rn/blob/main/clipGui2.py

mainブランチは英⇒日の翻訳のみ、中国語等や、日⇒英への対応プログラムはchoiseブランチ以下の`clipGui2.py`のプログラムで対応している(動作が重すぎるのでマージしてない)
## 注意
`datetime`, `pyperclip`, `selenium`とChromeWebDriverのインストールが必要です。

## 実行
改行コードを抜くだけ版
``` 
python clipGui.py
```
DeepLに突っ込んで翻訳してくる版(反映されるまでに時間がかかります)
```
python clipGui2.py
```

