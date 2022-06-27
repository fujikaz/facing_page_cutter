# facing_page cutter
## 目的など
- 見開きでスキャンしたPDFを，各ページ単位に切った1つのPDFに変換するためのスクリプト
- Brother MFC-J6583CDWを前提に作成
    - デフォルトで長辺が縦

## 仕様
- 見開きのPDFに対して，長辺を半分の大きさに切って連続するページに変換したファイルにして出力する．
    - ページの大きさは指定しない
    - 縦書きのものは左のページが若番，横書きのものは右ページが若番になるように並べる．
    - 縦書きかどうかはオプションで指定する
- 切った後の長辺が縦になるように回転する．
- 出力するファイル名は'元のファイル名+_cut.pdf'

## Usage
- `/path/to/facing_page_cut.py [-v] <pdf filename w/ .pdf>`

## Installation
- PyPDF2をインストール
    - `pip install PyPDF2`
- git clone https://github.com/fujikaz/facing_page_cutter
- パスの設定などは適当に
