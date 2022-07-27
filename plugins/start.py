from modules.config import (
    START_PIC, 
    BOT_USERNAME,
    SUPPORT_GROUP,
    OWNER_USERNAME,
    UPDATES_CHANNEL,
)
from modules.helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message



@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_private(client: Client, message: Message):
 await message.reply_photo(
        photo=f"{START_PIC}",
        caption=f"""**━━━━━━━━━━━━━━━━━━
💥 اهلا بك اختصاص هذا البوت 
تشغيل الاغاني في المكالمات الصوتية » 
لمعرفة الاوامر عليك النقر على زر الاوامر
قناة ســـورس ألـرًسًــــــــآمِ [قناة السورس](t.me/E_L_R_A_S_A_M)... 
مطور السورس [ELRASAM](https://t.me/Mahmod777777)
━━━━━━━━━━━━━━━━━━**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎯 ¦ اضـفـني الى مـجمـوعـتك ¦ 🎯",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [
                    InlineKeyboardButton("🥇 ¦ المـــطور", url=f"https://t.me/{OWNER_USERNAME}"),
                    InlineKeyboardButton("🖥 ¦ الأوامــر", url=f"https://telegra.ph/%D8%A7%D9%87%D9%84%D8%A7-%D8%A8%D9%83-%D8%AC%D9%85%D9%8A%D8%B9-%D8%A7%D9%84%D8%A7%D9%88%D8%A7%D9%85%D8%B1-%D8%B9%D8%B1%D8%A8%D9%8A%D9%87-%D9%8A%D9%85%D9%83%D9%86%D9%83-%D8%AA%D8%B4%D8%BA%D9%8A%D9%84-%D9%81%D9%8A-%D8%A7%D9%84%D8%A7%D9%88%D8%A7%D9%85%D8%B1-%D8%A7%D9%84%D8%A7%D8%AC%D9%86%D8%A8%D9%8A%D9%87-%D8%A7%D9%8A%D8%B6%D8%A2-%D9%88%D8%B4%D9%83%D8%B1%D8%A7-%D9%84%D9%83%D9%85-07-01"),
                ],
                [
                    InlineKeyboardButton(
                        "🥇 ¦ الــكروب", url=f"{SUPPORT_GROUP}"
                    ),
                    InlineKeyboardButton(
 " ⚙️ ¦ السورس ", url=f"https://t.me/E_L_R_A_S_A_M"}"
                    ),
                ],
            ]
        ),
    )
    @Client.on_message(command(["مبرمج السورس" ,"ألـرًسًــــــــآمِ" ,"سورس" ,"السورس" ,"الرسام" ,"ELRASAM" ,"الرسام"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/37338e26a9c4d611c7770.jpg",
        caption=f""" [⍟ 𝚆𝙴𝙻𝙲𝙾𝙼𝙴 𝚃𝙾 ELRASAM](t.me/E_L_R_A_S_A_M)  """,
        reply_markup=InlineKeyboardMarkup(
         [
            [
                InlineKeyboardButton("ألـرًسًــــــــآمِ🇪🇬!", url=f"https://t.me/Mahmod777777"),
           ],
            [ 
                InlineKeyboardButton("ELRASAM", url=f"https://t.me/E_R_S_A_M1"),
            ],
            [
                InlineKeyboardButton(
                    "𝗦𝗨𝗢𝗥𝗖𝗘 ELRASAM🦍", url=f"https://t.me/E_L_R_A_S_A_M"
                ),
            ],
            [
                InlineKeyboardButton("🐍اضفني الى مجموعتك🐍", url=f"https://t.me/K61TBot?startgroup=true"),
            ]
         ]
     )
  )

@Client.on_message(command(["المطور", "/godzela", "مطور" ,"مطور البوت"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/b144db94dc0db0fd86526.jpg",
        caption=f""" الاول: هو مطور السورس🐍 \n الثاني: مطور البوت🐍 \n√""",
        reply_markup=InlineKeyboardMarkup(
         [
            [
                InlineKeyboardButton("ألـرًسًــــــــآمِ🇪🇬!", url=f"https://t.me/Mahmod777777"),
            ],
            [
                InlineKeyboardButton(
                        DEV_NAME, url=f"https://t.me/{OWNER_NAME}"
                ),
            ],
            [
                InlineKeyboardButton("🐍ضيـف البـوت لمجمـوعتـك🐍", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
            ]
         ]
     )
  )

@Client.on_message(filters.new_chat_members)
async def new_chat(c: Client, m: Message):
    chat_id = m.chat.id
    if await is_served_chat(chat_id):
        pass
    else:
        await add_served_chat(chat_id)
    ass_uname = (await user.get_me()).username
    bot_id = (await c.get_me()).id
    for member in m.new_chat_members:
        if member.id == bot_id:
            return await m.reply(
                "🐍 **شكرا لإضافتي إلى مجموعتك لتشغيل الموسيقي!**\n\n"
                "🐍 **قم بترقيتي مسؤول في المجموعة لكي أتمكن من العمل بشكل صحيح\nولا تنسى كتابة `/انضم او بيمبو تعاله` لدعوة الحساب المساعد\nقم بكتابة`/تحديث` لتحديث قائمة المشرفين",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("⚙️ ¦ السورس ", url=f"https://t.me/{UPDATES_CHANNEL}"),
                            InlineKeyboardButton("☣️ ¦ جـروب الدعم", url=f"https://t.me/{GROUP_SUPPORT}")
                        ],
                        [
                            InlineKeyboardButton(
                        ALIVE_NAME, url=f"https://t.me/{ass_uname}"),
                        ],
                        [
                            InlineKeyboardButton(
                        "🐍اضـفني لي مـجـمـوعـتـك🐍",
                        url=f'https://t.me/K61TBot?startgroup=true'),
                        ],
                    ]
                )
            )


chat_watcher_group = 5



