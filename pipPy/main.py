from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token("5703355736:AAEEK1seScMfcqODF_p6W3D1iJepTvJdCYc").build()

app.add_handler(CommandHandler("hi", hiCommand))
app.add_handler(CommandHandler("time", timeCommand))
app.add_handler(CommandHandler("help", helpCommand))
app.add_handler(CommandHandler("sum", sumCommand))

app.run_polling()