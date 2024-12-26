from pyrogram import Client, filters
from pyrogram.types import Message
from nexichat import nexichat

# Use only emojis supported by Telegram
SUPPORTED_EMOJIS = ["👍", "❤️", "😂", "🔥", "😢", "😡", "🤩", "👏", "😎", "🙌",
                    "🎉", "💪", "🤔", "😅", "😊", "👀", "🎶", "🌟", "💯"]

@nexichat.on_message(filters.incoming)
async def react_to_messages(client: Client, message: Message):
    try:
        for emoji in SUPPORTED_EMOJIS:
            await message.react(emoji)
    except Exception as e:
        print(f"Failed to react to message: {e}")
