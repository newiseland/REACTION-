import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message

# List of emojis supported by Telegram for reactions
SUPPORTED_EMOJIS = ["👍", "❤️", "😂", "🔥", "👏"]  # Add more if needed, ensure they are supported


@app.on_message(filters.incoming)
async def react_to_messages(client: Client, message: Message):
    try:
        for emoji in SUPPORTED_EMOJIS:
            await message.react(emoji)  # React to the same message with each emoji
            await asyncio.sleep(0.5)  # Optional: Add a small delay to avoid rate limiting
    except Exception as e:
        print(f"Failed to react to message: {e}")
        
