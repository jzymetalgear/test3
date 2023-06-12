import asyncio
from datetime import datetime
from telegram import Bot

# Define your bot token
TOKEN = '6177428008:AAEewf2ZGq657fvMqJ6oqH4tYoYvpaP68p8'

# Define the reminder message
reminder_message = "Dang Dang Dang~"

# Create an instance of the Bot class
bot = Bot(token=TOKEN)

# Define the asynchronous function to send the reminder message
async def send_reminder():
    current_hour = datetime.now().hour
    if current_hour > 0:
        reminder_text = reminder_message * current_hour
        await bot.send_message(chat_id='1285682450 ', text=reminder_text)

# Run the bot continuously
async def main():
    while True:
        # Get the current time
        current_time = datetime.now().strftime('%H:%M')

        # Check if it's a whole hour
        if current_time.endswith(':00'):
            await send_reminder()

        # Sleep for 1 minute
        await asyncio.sleep(60)

# Run the main function
asyncio.run(main())
