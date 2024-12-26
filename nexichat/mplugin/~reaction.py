from pyrogram import Client, filters
from pyrogram.types import Message
from nexichat import nexichat


# List of emojis for reactions
# SUPPORTED_EMOJIS = ["👍", "❤️", "😂", "🔥", "👏"]

# Function to react to incoming messages
@nexichat.on_message(filters.incoming)
async def react_to_messages(client: Client, message: Message):
    try:
            await message.react("💥","💗")  # React to the same message with each emoji
            await asyncio.sleep(0.5)  # Delay between reactions to avoid rate limiting
    except Exception as e:
        print(f"Failed to react to message: {e}")
