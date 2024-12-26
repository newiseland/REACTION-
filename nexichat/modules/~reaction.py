

from pyrogram import Client, filters
from pyrogram.types import Message
from nexichat import nexichat

@nexichat.on_message(filters.incoming)
async def react_to_messages(client: Client, message: Message):
    emojis = ["👍", "❤️", "😂", "🔥", "😎", "💯", "👏", "😊", "🎉", "🙌", 
              "🤔", "😅", "😢", "😡", "🤩", "🎶", "✅", "🌟", "👀", "💪"]
    try:
        for emoji in emojis:
            await message.react(emoji)
    except Exception as e:
        print(f"Failed to react to message: {e}")
