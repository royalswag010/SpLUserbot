import textwrap
import os
from PIL import Image, ImageFont, ImageDraw
from pyrogram import Client, filters
from config import STUFF
from Spoiled.Utils import eor, verify
from . import add_command

hl = STUFF.COMMAND_HANDLER

@Client.on_message(filters.command(["memify", "mmf"], hl))
async def handler(_, m):
    x = await verify(_, m)
    if not x:
        return
    if not m.reply_to_message:
        return await eor(m, "Reply to an image or a sticker !")
    if not m.reply_to_message.sticker and not m.reply_to_message.photo:
        return await eor(m, "Reply to an image or a sticker !")
    msg = await eor(m, f"`Memifying this image! (」ﾟﾛﾟ)｣ `")
    file = await m.reply_to_message.download()
    if len(m.command) == 1:
        return await msg.edit("You might want to try `/mmf text`")
    text = m.text.split(None, 1)[1]
    meme = await drawText(file, text)
    await m.reply_sticker(meme)
    await msg.delete()
    os.remove(meme)

async def drawText(image_path, text):
    img = Image.open(image_path)
    os.remove(image_path)
    shadowcolor = "black"
    i_width, i_height = img.size
    if os.name == "nt":
        fnt = "ariel.ttf"
    else:
        fnt = "./Fonts/default.ttf"
    m_font = ImageFont.truetype(fnt, int((70 / 640) * i_width))
    if ";" in text:
        upper_text, lower_text = text.split(";")
    else:
        upper_text = text
        lower_text = ""
    draw = ImageDraw.Draw(img)
    current_h, pad = 10, 5
    if upper_text:
        for u_text in textwrap.wrap(upper_text, width=15):
            u_width, u_height = draw.textsize(u_text, font=m_font)
            draw.text(
                xy=(((i_width - u_width) / 2) - 2, int((current_h / 640) * i_width)),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(((i_width - u_width) / 2) + 2, int((current_h / 640) * i_width)),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=((i_width - u_width) / 2, int(((current_h / 640) * i_width)) - 2),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(((i_width - u_width) / 2), int(((current_h / 640) * i_width)) + 2),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )

            draw.text(
                xy=((i_width - u_width) / 2, int((current_h / 640) * i_width)),
                text=u_text,
                font=m_font,
                fill=(255, 255, 255),
            )
            current_h += u_height + pad
    if lower_text:
        for l_text in textwrap.wrap(lower_text, width=15):
            u_width, u_height = draw.textsize(l_text, font=m_font)
            draw.text(
                xy=(
                    ((i_width - u_width) / 2) - 2,
                    i_height - u_height - int((20 / 640) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(
                    ((i_width - u_width) / 2) + 2,
                    i_height - u_height - int((20 / 640) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    (i_height - u_height - int((20 / 640) * i_width)) - 2,
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    (i_height - u_height - int((20 / 640) * i_width)) + 2,
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )

            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    i_height - u_height - int((20 / 640) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(255, 255, 255),
            )
            current_h += u_height + pad
    image_name = "memify.webp"
    webp_file = os.path.join(image_name)
    img.save(webp_file, "webp")
    return webp_file

command = "Memify"
help = f"`» {hl}mmf | {hl}memify - try out`"

add_command(command, help)
