# coding: utf-8
# 日本語版について: このファイルは jpmorganchase/python-training の英語原文を
# 日本語に翻訳したものです（Apache License 2.0）。コードの動作は変更していません。

import numpy as np


def mandelbrot(X, Y, max_iterations=1000, verbose=True):
    """マンデルブロ集合を計算する。

    マンデルブロ数列が発散するまでの反復回数を格納した行列を返します。
    行列の各セルは、入力の X ベクトルと Y ベクトルの要素の組 (x, y) に
    対応します。各点について、最大で max_iterations 回まで反復します。
    :param X: x 座標の集合
    :param Y: y 座標の集合
    :param max_iterations: 数列を止めるまでの最大反復回数
    :param show_out: 計算中の行番号をコンソールに表示するかどうかを
        示すフラグ
    :return: 入力で指定した全点についての、発散までの反復回数を
        格納した行列
    """

    # 出力配列を初期化
    out_arr = np.zeros((len(Y), len(X)))

    # y 座標についてループ
    for i, y in enumerate(Y):
        for j, x in enumerate(X):
            n = 0
            c = x + 1j*y
            z = c
            while (n < max_iterations) and (abs(z) <= 2):
                z = z*z + c
                n += 1
            out_arr[i, j] = n

    return out_arr
