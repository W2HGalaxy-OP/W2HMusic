import asyncio
from pyrogram import Client as c

API_ID = input("\nEnter Your API_ID:\n > ")
API_HASH = input("\nEnter Your API_HASH:\n > ")

print("\n\n Enter Phone number when asked.\n\n")

i = c(":memory:", api_id=API_ID, api_hash=API_HASH)


async def main():
  await i.start()
  i.storage.SESSION_STRING_FORMAT = ">B?256sQ?"
  i.storage.SESSION_STRING_SIZE = 356
  ss = await i.export_session_string()
  print("\nHERE IS YOUR STRING SESSION, COPY IT, DON'T SHARE For Support Join @w2hsupport !!\n")
  print(f"\n{ss}\n")


asyncio.run(main())
