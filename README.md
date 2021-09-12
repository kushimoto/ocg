# ocg
アルファベットの画像を少しだけ読みにくくします。<br/>
reCAPTCHAもどきを作っている子どものために作りました。

### 使い方
1. リポジトリをダウンロード
```
git clone https://github.com/kushimoto/ocg.git
```
2. ダウンロードしたリポジトリのディレクトリへ移動
```
cd ocg
```
3. 元となる[アルファベットの画像](https://sozai.cman.jp/icon/string/alphabet2/)をダウンロード
4. ファイル名は A.png a.png など大文字小文字で分けて保存する
5. 最後にプログラムを実行
```
python3 ocg.py
```
6. lowercase uppercase というディレクトリが作成されて、中に読みにくいアルファベットが入っています。

### 依存関係の解決
たぶん下のコマンドを実行しておけば大丈夫。あとは自分でがんばってね
```
sudo apt update
sudo apt install python3-pip
sudo pip3 install opencv-python3
```
