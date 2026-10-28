import json
import os
from datetime import datetime

# あなたのアフィリエイトトラッキングタグ（後からいつでも書き換え可能）
AMAZON_TRACKING_ID = os.environ.get("AMAZON_TAG", "your-tag-22")

# 厳選アイテムマスタープール
MASTER_ITEMS = [
    {
        "id": "item1",
        "title": "Anker 511 Charger (Nano 3, 30W)",
        "category": "gadget",
        "description": "スマホもMacBook Airも急速充電できる超小型USB-C充電器。荷物を極限まで減らしたい必須ギア。",
        "price": "約¥3,000",
        "badge": "★4.6 人気",
        "base_url": "https://www.amazon.co.jp/dp/B0B5TDQZ99"
    },
    {
        "id": "item2",
        "title": "CIO NovaPort DUO 65W 超小型充電器",
        "category": "gadget",
        "description": "2ポート同時出力で自動電力振り分け対応。スマホとPCの同時持ち歩きに最適。",
        "price": "約¥4,900",
        "badge": "殿堂入り",
        "base_url": "https://www.amazon.co.jp/dp/B0B7BGW588"
    },
    {
        "id": "item3",
        "title": "ロジクール MX MASTER 3S 高性能ワイヤレスマウス",
        "category": "desk",
        "description": "静音クリックと超高速スクロールホイール。作業効率を劇的に引き上げる定番フラッグシップ。",
        "price": "約¥15,000",
        "badge": "生産性No.1",
        "base_url": "https://www.amazon.co.jp/dp/B0B1DM9BDP"
    },
    {
        "id": "item4",
        "title": "『イシューからはじめよ』 安宅和人 著",
        "category": "book",
        "description": "AI時代だからこそ差がつく「本当に解くべき本質的な問い」を見極める思考法の名著。",
        "price": "約¥1,980",
        "badge": "必読ベストセラー",
        "base_url": "https://www.amazon.co.jp/dp/447801453X"
    },
    {
        "id": "item5",
        "title": "BenQ ScreenBar モニター掛け式ライト",
        "category": "desk",
        "description": "画面の反射がなく省スペース。長時間の画面作業でも目の負担を大幅に軽減するデスクライト。",
        "price": "約¥14,000",
        "badge": "愛用者多数",
        "base_url": "https://www.amazon.co.jp/dp/B0785D93KD"
    }
]

def build_affiliate_url(base_url, tag):
    delimiter = "&" if "?" in base_url else "?"
    return f"{base_url}{delimiter}tag={tag}"

def run():
    os.makedirs("data", exist_ok=True)
    
    # アフィリエイトURLの動的付与と日次ローテーション
    curated_list = []
    for item in MASTER_ITEMS:
        curated_list.append({
            "title": item["title"],
            "category": item["category"],
            "description": item["description"],
            "price": item["price"],
            "badge": item["badge"],
            "url": build_affiliate_url(item["base_url"], AMAZON_TRACKING_ID)
        })

    # data/products.json に書き出し
    output_path = os.path.join("data", "products.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(curated_list, f, ensure_ascii=False, indent=2)
    
    print(f"[{datetime.now().isoformat()}] products.json updated successfully with {len(curated_list)} items.")

if __name__ == "__main__":
    run()
