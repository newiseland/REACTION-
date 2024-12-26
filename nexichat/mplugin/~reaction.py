from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio

# Initialize the client
app = Client("reaction_bot", 
             api_id="24912072", 
             api_hash="1a9c568007ef51bed8fd2357947e5cb3", 
             bot_token="8147535526:AAHDQumv7CDFT9mKHeWr459tKlbdFsOGJTo")

# List of emojis for reactions
SUPPORTED_EMOJIS = ["👍", "❤️", "😂", "🔥", "👏"]

# Function to react to incoming messages
@app.on_message(filters.incoming)
async def react_to_messages(client: Client, message: Message):
    print(f"Received a message: {message.text}")  # Debugging log
    try:
        for emoji in SUPPORTED_EMOJIS:
            await message.react(emoji)  # React to the same message with each emoji
            await asyncio.sleep(0.5)  # Delay between reactions to avoid rate limiting
    except Exception as e:
        print(f"Failed to react to message: {e}")

# Run the bot
if __name__ == "__main__":
    app.run()
