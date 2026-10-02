# 高校野球 全国レーティングデータベース

全国高校野球の試合結果を蓄積し、検査・統合・レーティング計算を行うためのデータベースです。

## 目的

以下の試合データを全国規模で管理します。

- 過去10年程度の地区大会以上の試合
- 2025年春以降の各都道府県大会
- 春季大会
- 夏季大会
- 秋季大会
- 地区大会
- 明治神宮大会
- 選抜高校野球
- 全国高校野球選手権

最終的には全国の試合を統合し、各校のレーティングを計算します。

---

## データ構成

```text
hs-bb-ranking/
├─ data/
│  ├─ 01_hokkaido/
│  ├─ 02_tohoku/
│  ├─ 03_kanto_tokyo/
│  ├─ 04_tokai/
│  ├─ 05_hokushinetsu/
│  ├─ 06_kinki/
│  ├─ 07_chugoku/
│  ├─ 08_shikoku/
│  ├─ 09_kyushu/
│  └─ national/
│
├─ master/
│  ├─ schools.csv
│  ├─ tournaments.csv
│  └─ sources.csv
│
├─ scripts/
│  ├─ validate.py
│  ├─ merge.py
│  └─ rating.py
│
└─ output/
   ├─ all_matches.csv
   └─ rating.xlsx
