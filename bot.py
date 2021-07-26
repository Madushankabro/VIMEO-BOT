"""
Vimeo downloader bot
Copyright (C) 2021 @ImJanindu

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

# Kang with credits vomro

import os
import logging
from pyrogram import filters, Client, idle
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from vimeo_downloader import Vimeo
from sample_config import Config

# location
LOCATION = "./"

# logging
bot = Client(
   "Vimeo",
   api_id=Config.API_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.BOT_TOKEN,
)


@bot.on_message(filters.regex(pattern="https://vimeo.com/") & filters.private)
async def vimeo(_, message):
    input = message.text
    try:
        v = Vimeo(input)
        streams = v.streams
        vid = stream[-1].download(download_directory=LOCATION,
                        filename="vimeo")
    except Exception as e:
        print(str(e))
        return
    await bot.send_video(message.chat.id, video=vid)
    os.remove(vid)

bot.start()
idle()
