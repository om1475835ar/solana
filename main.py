import time
import requests
from telegram import Bot

# إعدادات
API_KEY = "a79df3d8-874e-46f8-b190-2212385daff1"
TELEGRAM_BOT_TOKEN = "7509802817:AAE9xoxHG6HN8l34zBCvD_cTCNI6YHbh_58"
CHAT_ID = "YOUR_TELEGRAM_ID"

bot = Bot(token=TELEGRAM_BOT_TOKEN)

def analyze_and_notify():
    try:
        # مثال لتحليل عملة
        url = f"https://mainnet.helius-rpc.com/?api-key={API_KEY}"
        response = requests.post(url, json={"jsonrpc":"2.0", "id":1, "method":"getAssetsByOwner", "params":["dummy"]})
        data = response.json()

        # إرسال إشعار وهمي للتجريب
        bot.send_message(chat_id=CHAT_ID, text="🚀 بوت شغال: تم تحليل عملة تجريبية وإرسال الإشعار.")

    except Exception as e:
        bot.send_message(chat_id=CHAT_ID, text=f"❌ حدث خطأ: {e}")

# يعمل كل دقيقة
while True:
    analyze_and_notify()
    time.sleep(60)
