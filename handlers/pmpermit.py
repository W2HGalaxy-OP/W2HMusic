from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"Hi there, This is a music assistant service .\n\n ❗️ Rules:\n   - No chatting allowed\n   - No spam allowed \n\n 👉 **If you get Any problem with playing Music then contact with Us @David99q and @w2h_ravan because they are owner of this bot.**\n\n)
  return                        
