from pathlib import Path
import csv

SCHOOLS_FILE = Path("master/schools.csv")


def load_school_aliases():
    """
    schools.csv を読み込み、
    別名 -> 正規学校名 の辞書を作る
    """
    aliases = {}

    with SCHOOLS_FILE.open(
        "r",
        encoding="utf-8-sig",
        newline=""
    ) as f:
        reader = csv.DictReader(f)

        for row in reader:
            canonical = row["canonical_name"].strip()

            if not canonical:
                continue

            # 正規名そのもの
            aliases[canonical] = canonical

            # alias列
            for key, value in row.items():
                if not key.startswith("alias"):
                    continue

                alias = (value or "").strip()

                if alias:
                    aliases[alias] = canonical

    return aliases


def normalize_school_name(name, aliases):
    """
    学校名を正規化する
    """
    name = (name or "").strip()

    if not name:
        return ""

    return aliases.get(name, name)


def main():
    aliases = load_school_aliases()

    print("=" * 60)
    print("学校名正規化テスト")
    print("=" * 60)

    test_names = [
        "星稜",
        "星稜高",
        "星稜高校",
        "金沢高校",
        "富山商業",
        "敦賀気比高",
        "日本文理高校",
        "上田西高",
        "未登録高校",
    ]

    for name in test_names:
        normalized = normalize_school_name(
            name,
            aliases
        )

        print(f"{name} -> {normalized}")


if __name__ == "__main__":
    main()
