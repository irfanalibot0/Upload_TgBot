from pyrogram import filters
from pyrogram.types import CallbackQuery, Message
from pyromod.helpers import ikb

from uploadtgbot.bot_class import UploadTgBot
from uploadtgbot.utils.constants import Constants
from uploadtgbot.utils.joinCheck import joinCheck
from uploadtgbot.vars import Vars


@UploadTgBot.on_message(filters.command("start", Vars.PREFIX_HANDLER) & filters.private)
@joinCheck()
async def start_bot(_, m: Message):
    return await m.reply_text(
        Constants.USAGE_WATERMARK_ADDER.format(m.from_user.first_name, Vars.CAPTION),
        reply_markup=ikb(Constants.START_KB),
        disable_web_page_preview=True,
        quote=True,
    )


@UploadTgBot.on_message(filters.command("help", Vars.PREFIX_HANDLER) & filters.private)
@joinCheck()
async def help_bot(_, m: Message):
    return await m.reply_text(
        Constants.page1_help,
        reply_markup=ikb(Constants.page1_help_kb),
        disable_web_page_preview=True,
    )


@UploadTgBot.on_callback_query(filters.regex("^help_callback."))
async def help_callback_func(_, q: CallbackQuery):
    query_data = q.data.split(".")[1]
    if query_data in ("start", "page1"):
        await q.message.edit_text(
            Constants.page1_help,
            reply_markup=ikb(Constants.page1_help_kb),
            disable_web_page_preview=True,
        )
    elif query_data == "page2":
        await q.message.edit_text(
            Constants.page2_help,
            reply_markup=ikb(Constants.page2_help_kb),
            disable_web_page_preview=True,
        )
    elif query_data == "page3":
        await q.message.edit_text(
            Constants.page3_help,
            reply_markup=ikb(Constants.page3_help_kb),
            disable_web_page_preview=True,
        )
    await q.answer()
