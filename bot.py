import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

# قراءة التوكن من متغيرات البيئة
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("BOT_TOKEN is not set in environment variables")

# دالة الردود
async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    text = update.message.text.lower()

    if "السلام" in text:
        await update.message.reply_text("وعليكم السلام ورحمة الله 🌹")
    elif "مرحبا" in text:
        await update.message.reply_text("مرحباً بك 👋")
    elif "كيفك" in text:
        await update.message.reply_text("الحمد لله تمام 😊")
    else:
        await update.message.reply_text("تم استلام رسالتك ✅")

# تشغيل التطبيق
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))
app.run_polling()
