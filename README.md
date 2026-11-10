<img width="50%" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/J_P_Morgan_Logo_2008_1.svg/1280px-J_P_Morgan_Logo_2008_1.svg.png">

# Python Training 日本語版（Python 研修）
**この Python 研修は、JPMorgan のビジネスアナリストとトレーダー、および一部のクライアントを対象としています。**

> **日本語版について**: このリポジトリは、[jpmorganchase/python-training](https://github.com/jpmorganchase/python-training) を日本語に翻訳したフォークです。本文・ノートブック・コメントを日本語化しています。ライセンスは原典と同じ Apache 2.0 です。
>
> なお、第4章・第8章・第9章には、原文に不足していた部分を日本語版が独自に実装・修正した箇所があります（API の提供終了への対応、キーなしで使えるデータ源への差し替え、説明のないコードへの章の組み立て）。各章の中で明記しています。
>
> 日本語版の翻訳・公開： 霞ヶ関京  
> 連絡先： GitHub [@yanikasumin](https://github.com/yanikasumin)  
> X（旧 Twitter）[@lieberalism](https://x.com/lieberalism)（アカウント凍結中）  
> YouTube [@KASUMI_MOF](https://www.youtube.com/@KASUMI_MOF)

![GitHub](https://img.shields.io/github/license/jpmorganchase/python-training?style=flat-square)
[![Contact](https://img.shields.io/badge/Contact-Email-lightgrey?style=flat-square)](mailto:open_source@jpmorgan.com)


## 概要
このコースは、Python での数値計算とデータ可視化の入門です。コンピュータサイエンスやプログラミングの網羅的なコースではありません。ねらいは、複雑に見える題材でも、プログラミングの専門教育を受けていない人が取り組めることを、実例を通して示すことです。

研修は対面形式で、J.P. Morgan のテクノロジストとトレーダーが講師を務めます。機関投資家のお客様で関心のある方は、J.P. Morgan の担当チームへお問い合わせください。

[![](https://img.shields.io/badge/Launch-Cloud%20Instance-brightgreen?style=for-the-badge)](https://mybinder.org/v2/gh/yanikasumin/JPMorgan-python-training-ja/main?urlpath=lab)

## プラットフォームへの帰属表示
このリポジトリは [Binder](https://mybinder.readthedocs.io/en/latest/about.html) プロジェクトを利用しています。Binder は [Google Cloud Platform](https://cloud.google.com/)、[OVH](https://www.ovh.com/world/)、[GESIS Notebooks](https://notebooks.gesis.org)、[Turing Institute](https://www.turing.ac.uk) の支援を受けています。


## データへの帰属表示

- 金融データは [Alpha Vantage](https://www.alphavantage.co) の提供です。このコースは当初 [IEX Cloud](https://iexcloud.io) を使っていましたが、IEX Cloud は2024年8月31日にサービスを終了しました。対象のノートブックは Alpha Vantage の API に移行済みです。自分の API キーの設定方法は [.env.example](.env.example) を見てください。
- 空港と路線のデータは [OpenFlights.org](https://openflights.org/data.html#license) の提供です

このリポジトリで IEX Cloud、Alpha Vantage、その他のサードパーティのプラットフォーム、製品、データ、API プロバイダに触れているのは、説明と教育のためだけです。J.P. Morgan Chase & Co. やその関連会社が、その製品や企業を推奨していると受け取らないでください。


## ライセンス
このソフトウェアは Apache 2.0 ライセンスで提供しています。詳しくは [LICENSE](LICENSE) ファイルを見てください。
