
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, ChatJoinRequestHandler, ContextTypes

# ========= CONFIG =========
BOT_TOKEN = "8673419397:AAFSL5rPRMR3mJRkeTphJLcqsLXe1S4Yafk"
REGISTER_LINK = "https://okwingame22.com/#/register?invitationCode=7825714955019"
ADMIN_USERNAME = "princtrade"

VIDEO_PATH = "PRINCEVIDEO.mp4"
VOICE_PATH = "VOICE.ogg"
# ==========================

logging.basicConfig(level=logging.INFO)


async def approve_and_send(update: Update, context: ContextTypes.DEFAULT_TYPE):
    join_request = update.chat_join_request
    user = join_request.from_user
    name = user.first_name or "User"

    try:
        # ✅ Approve
        await join_request.approve()

        # 🌟 Welcome
        await context.bot.send_message(
            chat_id=user.id,
            text=(
                f"✨ 𝗛𝗹𝗼 {name} 👋\n\n"
                "✅ aapki request approve ho chuki hai\n\n"
                "📌 Niche details di gayi hai 👇"
            )
        )

        # 🎬 Video
        await context.bot.send_video(
    chat_id=user.id,
    video=open(VIDEO_PATH, "rb"),
    caption=(
        "🎯 𝗬𝗲𝗵 𝗿𝗵𝗮 𝗻𝘂𝗺𝗯𝗲𝗿 𝘄𝗮𝗹𝗮 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 📢\n\n"
        "👉 𝗜𝘀𝗽𝗲 𝗷𝗼𝗶𝗻 𝗵𝗼𝗻𝗮 𝗵𝗮𝗶 𝗷𝗮𝗹𝗱𝗶 𝘀𝗲 ⚡\n\n"
        "🎮 𝗢𝗞 𝗪𝗶𝗻 𝗺𝗲 𝗻𝗲𝘄 𝗜𝗗 𝗯𝗻𝗮𝗼\n"
        "💸 𝗗𝗲𝗽𝗼𝘀𝗶𝘁 𝗸𝗮𝗿𝗼\n"
        "📸 𝗦𝗰𝗿𝗲𝗲𝗻𝘀𝗵𝗼𝘁 𝗯𝗵𝗲𝗷𝗼"
    )
)
        # 🔗 Register Link
        await context.bot.send_message(
            chat_id=user.id,
            text=(
        "🔗 𝗥𝗘𝗚𝗜𝗦𝗧𝗘𝗥 𝗟𝗜𝗡𝗞\n\n"
        f"{REGISTER_LINK}"
    )
        )

       


        # 🎤 Voice
        await context.bot.send_voice(
            chat_id=user.id,
            voice=open(VOICE_PATH, "rb"),
            caption="👆 Poora audio sun lo sahi se 🎧"
        )

        # 💬 Admin button
        keyboard = [
            [InlineKeyboardButton("💬 Contact Admin", url=f"https://t.me/{ADMIN_USERNAME}")]
        ]

        await context.bot.send_message(
            chat_id=user.id,
            text="🛠️ Help chahiye? Admin se baat karo 👇",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    except Exception as e:
        print("Error:", e)


def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(ChatJoinRequestHandler(approve_and_send))

    print("🚀 Bot Running...")
    app.run_polling()


if __name__ == "__main__":
    main()