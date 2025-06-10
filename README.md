# 📺 Gemini NicoNico Live Comment Response Bot (Simulated)

This repository introduces a sample bot that uses Google's Gemini API to automatically respond to comments from NicoNico Live (NicoNama).

> ⚠️ Currently, this is a **simulated comment input** version for testing. Real-time integration with NicoNama is not yet implemented.

---

## ✅ Overview

* Users manually input comments
* Responses are generated using the Gemini API (Google Generative AI)
* The bot behaves like a real NicoNama streamer

---

## 🧰 Requirements

* Python 3.9 or higher
* Gemini API key issued from Google AI Studio
* `google-generativeai` library

---

## 📦 Installation

```bash
pip install google-generativeai
```

---

## 🔑 Getting the API Key

1. Log in to your Google account
2. Visit [Google AI Studio](https://makersuite.google.com/)
3. Select "Get API Key" to obtain your key
4. Add the key to a `.env` file or directly in your script

---

## 🚀 How to Run

```bash
python gemini_nico_bot.py
```

---

## 📝 Sample Code (`gemini_nico_bot.py`)

```python
import google.generativeai as genai
import os

# Set your API key (use environment variables for security)
genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel('gemini-pro')

print("🎥 Simulated NicoNama Comment Bot Started!")
while True:
    comment = input("👤 Viewer: ")
    if comment.lower() in ["q", "quit"]:
        print("👋 Exiting")
        break
    response = model.generate_content(f"As a NicoNama streamer, reply cheerfully to the following comment: {comment}")
    print(f"🤖 Bot: {response.text}\n")
```

---

## 🧪 Expansion Ideas

* Integrate with actual NicoNama WebSocket comments
* Auto-reply posting via Selenium or other automation tools
* Character-based responses (e.g., sassy, healing, Kansai dialect)
* Switch between Gemini and GPT-based bots

---

## 📚 References

* [Google AI Studio](https://makersuite.google.com/)
* [google-generativeai GitHub](https://github.com/google/generative-ai-python)

---

## ❓ Q\&A

**Q. Is the Gemini API free?**
A. As of June 2025, a free tier exists but usage limits may apply depending on your activity.

**Q. Can this bot work with real NicoNama comments?**
A. Yes, but you need to implement WebSocket handling and NicoNama integration separately.
