from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = 8548643375:AAENLumkAdkiyixZz4Te8eR17rFuZrg1IUw

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Plano Mensal", callback_data="mensal")],
        [InlineKeyboardButton("Plano Trimestral", callback_data="trimestral")],
        [InlineKeyboardButton("Plano Semestral", callback_data="semestral")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Acesso imediato ao Canal VIP\n\n"
        "Escolha um plano para continuar:",
        reply_markup=reply_markup
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
