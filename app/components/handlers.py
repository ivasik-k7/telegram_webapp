from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    MenuButtonWebApp,
    Update,
)
from telegram.ext import ContextTypes, ConversationHandler

from app.utils import settings, setup_logger

# from .config import WEB_APP_URL, CHANNEL_URL
# from .utils import setup_logger

logger = setup_logger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handles the /start command."""
    start_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "Open Web App", web_app={"url": settings.WEB_APP_URL}
                )
            ],
            [
                InlineKeyboardButton(
                    "Subscribe to the channel", url=settings.CHANNEL_URL
                )
            ],
            [InlineKeyboardButton("How to monetize", url=settings.CHANNEL_URL)],
        ]
    )

    how_to_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "Open Web App", web_app={"url": settings.WEB_APP_URL}
                )
            ],
            [
                InlineKeyboardButton(
                    "Subscribe to the channel", url=settings.CHANNEL_URL
                )
            ],
        ]
    )

    await update.message.reply_text(
        """
        Hello! Welcome to TayCoin 🌟
        You are now the mastermind behind a Thai crypto exchange!
        Choose your path and dive into the world of TayCoin. Tap the screen to collect coins, boost your passive income, and craft your own income strategy.
        Your contributions will be celebrated once the TayCoin token is listed (stay tuned for the dates!).
        Don’t forget to invite your friends—bring them into the game to earn even more coins together!
        """,
        reply_markup=start_markup,
    )

    await update.message.reply_text(
        """
        How to Play TayCoin 🌟

Full Version of the Guide

💰 Tap to Earn  
Tap the screen to collect TayCoins.

⛏ Mine  
Upgrade your mining cards to unlock passive income opportunities.

⏰ Profit Per Hour  
Your exchange will generate income even when you're not playing. After 3 hours of inactivity, you’ll need to log back in to continue earning.

📈 LEVEL UP  
The more TayCoins you accumulate, the higher the level of your exchange, and the faster you’ll earn more coins.

👥 Friends  
Invite friends to join the game and earn bonuses. Help friends advance to higher leagues and receive even greater rewards.

🪙 Token Listing  
At the end of the season, the TayCoin token will be listed and distributed among players. Stay tuned for announcements about the listing dates in our channel!

For assistance, type /help to access this guide.
""",
        reply_markup=how_to_markup,
    )

    bot = context.bot
    chat_id = update.message.chat_id

    web_app_button = MenuButtonWebApp(
        text="Play",
        web_app={"url": settings.WEB_APP_URL},
    )

    await bot.set_chat_menu_button(chat_id, web_app_button)

    return ConversationHandler.END


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Handles the /help command."""
    markup = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Play", web_app={"url": settings.WEB_APP_URL})],
            [
                InlineKeyboardButton(
                    "Subscribe to the channel", url=settings.CHANNEL_URL
                )
            ],
            [InlineKeyboardButton("How to monetize", url=settings.CHANNEL_URL)],
        ]
    )
    await update.message.reply_text(
        """
        TayCoin Help Guide 🌟

Welcome to the TayCoin Help Guide! Here you’ll find all the information you need to get started and excel in the game. If you have any other questions, don’t hesitate to reach out!

Features

- Upgrading Cards: Enhance your mining cards to maximize passive income.  
- Earning Bonuses: Invite friends and help them progress to earn extra bonuses.  
- Token Distribution: Information about the token listing and distribution will be available in our announcement channel.

Common Issues

1. I’m not earning coins. What should I do?  
- Ensure you’re tapping the screen regularly and that your mining cards are upgraded.

2. How do I invite friends?  
- Use the “Invite Friends” feature in the game menu to send invitations.

3. I forgot to log in within 3 hours. What happens?  
- You’ll need to log back in to continue earning. Your exchange pauses when you’re inactive.

4. When will the token be listed?  
- The listing dates will be announced in our official announcement channel. Stay tuned!

Additional Commands

/start
Begin your journey with TayCoin.  

/help
Display this help guide.  

/invite
Get a link to invite friends.

/balance
View your current balance of TayCoins and track your progress.

/status
Check the status of your earnings and see how your exchange is performing.

/announcements
Get the latest news and updates about the game, including token listing dates and special events.

Contact Support

If you encounter any issues or have further questions, please reach out to our support team via the contact form in the game or email us at support@taycoin.com.
""",
        reply_markup=markup,
    )
    return ConversationHandler.END
