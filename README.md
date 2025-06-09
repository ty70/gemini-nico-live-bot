# 📺 Gemini ニコ生コメント返答ボット（疑似）

このリポジトリでは、Google の Gemini API を活用して、ニコニコ生放送（ニコ生）のコメントに自動で返答するボットのサンプルを紹介します。

> ⚠️ 現段階では **疑似的なコメント入力**に対して返答するテストバージョンです。リアルニコ生連携は未実装です。

---

## ✅ 概要

* ユーザーが手動でコメントを入力
* Gemini API（Google Generative AI）を通じて応答を生成
* あたかもニコ生の配信者のように振る舞います

---

## 🧰 必要なもの

* Python 3.9 以上
* Google AI Studio で発行した Gemini API キー
* `google-generativeai` ライブラリ

---

## 📦 インストール

```bash
pip install google-generativeai
```

---

## 🔑 APIキーの取得

1. Google にログイン
2. [Google AI Studio](https://makersuite.google.com/) にアクセス
3. "Get API Key" を選択し、API キーを取得
4. 取得したキーを `.env` ファイルまたはスクリプト内に記載

---

## 🚀 実行方法

```bash
python gemini_nico_bot.py
```

---

## 📝 サンプルコード（`gemini_nico_bot.py`）

```python
import google.generativeai as genai
import os

# APIキーを設定（安全のため環境変数が推奨）
genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel('gemini-pro')

print("🎥 ニコ生疑似コメントボット 起動！")
while True:
    comment = input("👤 視聴者: ")
    if comment.lower() in ["q", "quit"]:
        print("👋 終了します")
        break
    response = model.generate_content(f"ニコ生配信者として、以下のコメントに楽しく返答してください：{comment}")
    print(f"🤖 ボット: {response.text}\n")
```

---

## 🧪 拡張アイデア

* 実際のニコ生 WebSocket コメントと連携
* Selenium等によるコメント返信の自動投稿
* キャラ別応答（例：毒舌系、癒し系、関西弁 など）
* GPT互換対応ボットとの切替機能

---

## 📚 参考

* [Google AI Studio](https://makersuite.google.com/)
* [google-generativeai GitHub](https://github.com/google/generative-ai-python)

---

## ❓ Q\&A

**Q. Gemini API は無料ですか？**
A. 2025年6月現在、一部無料枠がありますが利用量に応じて制限される可能性があります。

**Q. ニコ生の実コメント対応はできますか？**
A. 可能ですが別途 WebSocket 連携などの実装が必要です。
