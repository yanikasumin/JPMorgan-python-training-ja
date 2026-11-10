<img width="50%" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/J_P_Morgan_Logo_2008_1.svg/1280px-J_P_Morgan_Logo_2008_1.svg.png">

# Python Training 日本語版（Python 研修）
**この Python 研修は、JPMorgan のビジネスアナリストとトレーダー、および一部のクライアントを対象としています。**

> **日本語版について**: このリポジトリは、[jpmorganchase/python-training](https://github.com/jpmorganchase/python-training) の日本語版です。単なる翻訳ではなく、翻訳を基礎に、次の増補と修正を行っています。ライセンスは原典と同じ Apache 2.0 です。
>
> - **翻訳と文体**: 全章を翻訳し、直訳調でない自然な日本語に全面リスタイルしています
> - **補足解説**: 原文で説明が不足している箇所に、日本語版独自の解説を追加しています（第7・8・9章）
> - **追加実装**: 第8章に、SEC EDGAR（APIキー不要）で計算する節と計算の内訳の可視化、第9章には、原文にコードしかなかった箇所への説明と追加のコードを加え、章として組み立てています
> - **修正**: 第4章の原文が使う CoinDesk の API は提供が終了していたため、原文のコードは実行できない記録として残し、代替の API で動く経路を追加しています
> - **用語解説**: サイト版では各ページの下部に用語解説（金融とプログラムの両分野）を付け、本文中の用語をクリックすると解説に飛べます
>
> 独自の補足・追加・修正には、すべて「日本語版独自」と明記し、原文の内容と区別しています。第6章は、原典自体が未実装のプレースホルダ（空のコードセルのみ）のため、日本語版でも未実装です。
>
> 日本語版の翻訳・公開： 霞ヶ関京  
> 連絡先： GitHub [@yanikasumin](https://github.com/yanikasumin)  
> X（旧 Twitter）[@lieberalism](https://x.com/lieberalism)（アカウント凍結中）  
> YouTube [@KASUMI_MOF](https://www.youtube.com/@KASUMI_MOF)

**Web サイト版（用語解説付きで、そのまま読めます）**: https://yanikasumin.github.io/JPMorgan-python-training-ja/

![GitHub](https://img.shields.io/github/license/jpmorganchase/python-training?style=flat-square)
[![Contact](https://img.shields.io/badge/Contact-Email-lightgrey?style=flat-square)](mailto:open_source@jpmorgan.com)


## 概要
このコースは、Python での数値計算とデータ可視化の入門です。コンピュータサイエンスやプログラミングの網羅的なコースではありません。ねらいは、複雑に見える題材でも、プログラミングの専門教育を受けていない人が取り組めることを、実例を通して示すことです。

研修は対面形式で、J.P. Morgan のテクノロジストとトレーダーが講師を務めます。機関投資家のお客様で関心のある方は、J.P. Morgan の担当チームへお問い合わせください。

[![](https://img.shields.io/badge/Launch-Cloud%20Instance-brightgreen?style=for-the-badge)](https://mybinder.org/v2/gh/yanikasumin/JPMorgan-python-training-ja/main?urlpath=lab)

## 章一覧

0. [科学計算のためのベストプラクティス](https://yanikasumin.github.io/JPMorgan-python-training-ja/notebooks/0_best_practices.html) — 開発環境と読みやすいコードの作法（Git、テスト、スタイル）
1. [Jupyter 入門](https://yanikasumin.github.io/JPMorgan-python-training-ja/notebooks/1_basic.html) — Python の基礎とノートブックの使い方
2. [例1：ストラドルの価格計算](https://yanikasumin.github.io/JPMorgan-python-training-ja/notebooks/2_straddle.html) — オプションの価格を近似式とモンテカルロ法で計算する
3. [例2：ファイルを扱う](https://yanikasumin.github.io/JPMorgan-python-training-ja/notebooks/3_flights.html) — OpenFlights の路線データを pandas で読み込み、集計する
4. [Web API からのデータ取得](https://yanikasumin.github.io/JPMorgan-python-training-ja/notebooks/4_webapi.html) — API の呼び出しと JSON の整形（日本語版で API 提供終了に対応済み）
5. [Web サイトからデータを取得する](https://yanikasumin.github.io/JPMorgan-python-training-ja/notebooks/5_website.html) — read_html と BeautifulSoup によるスクレイピング
6. [金融データの利用](https://yanikasumin.github.io/JPMorgan-python-training-ja/notebooks/6_financial_data.html) — 原典でも未実装のプレースホルダ
7. [グラフ描画の応用：matplotlib の先へ](https://yanikasumin.github.io/JPMorgan-python-training-ja/notebooks/7_advanced_plotting.html) — ボラティリティ・サーフェスなど、描画ライブラリの応用
8. [金融データを使う例 #1：アルトマンZスコア（ダブルプライム）の計算](https://yanikasumin.github.io/JPMorgan-python-training-ja/notebooks/8_altman_z_double_prime.html) — 信用リスクのモデル実装（日本語版で SEC EDGAR 版を追加）
9. [3次元プロット](https://yanikasumin.github.io/JPMorgan-python-training-ja/notebooks/9_3d_plotting.html) — 米国債イールドカーブの3次元可視化（日本語版で章として組み立て）

## About (English)

This is a Japanese edition of JPMorgan's [python-training](https://github.com/jpmorganchase/python-training) — translated and expanded. It teaches Python for numerical computing and data visualization with Jupyter notebooks: best practices and Git, Python basics, options pricing (straddle, Monte Carlo), pandas with OpenFlights data, web APIs and JSON, web scraping with BeautifulSoup, advanced plotting and volatility surfaces, the Altman Z'' credit-risk model (with an added keyless SEC EDGAR implementation), and 3D plotting of the US Treasury yield curve. The [website edition](https://yanikasumin.github.io/JPMorgan-python-training-ja/) adds a per-chapter glossary covering both finance and programming terms. Licensed under Apache 2.0, same as the original.

## プラットフォームへの帰属表示
このリポジトリは [Binder](https://mybinder.readthedocs.io/en/latest/about.html) プロジェクトを利用しています。Binder は [Google Cloud Platform](https://cloud.google.com/)、[OVH](https://www.ovh.com/world/)、[GESIS Notebooks](https://notebooks.gesis.org)、[Turing Institute](https://www.turing.ac.uk) の支援を受けています。


## データへの帰属表示

- 金融データは [Alpha Vantage](https://www.alphavantage.co) の提供です。このコースは当初 [IEX Cloud](https://iexcloud.io) を使っていましたが、IEX Cloud は2024年8月31日にサービスを終了しました。対象のノートブックは Alpha Vantage の API に移行済みです。自分の API キーの設定方法は [.env.example](.env.example) を見てください。
- 空港と路線のデータは [OpenFlights.org](https://openflights.org/data.html#license) の提供です

このリポジトリで IEX Cloud、Alpha Vantage、その他のサードパーティのプラットフォーム、製品、データ、API プロバイダに触れているのは、説明と教育のためだけです。J.P. Morgan Chase & Co. やその関連会社が、その製品や企業を推奨していると受け取らないでください。


## ライセンス
このソフトウェアは Apache 2.0 ライセンスで提供しています。詳しくは [LICENSE](LICENSE) ファイルを見てください。
