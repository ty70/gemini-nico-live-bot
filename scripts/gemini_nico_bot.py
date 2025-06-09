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