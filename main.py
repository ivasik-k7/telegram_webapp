from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler

from app.components.handlers import help, start
from app.utils import settings, setup_logger

logger = setup_logger(__name__)


def main() -> None:
    application = Application.builder().token(settings.TELEGRAM_BOT_TOKEN).build()

    start_handler = CommandHandler("start", start)

    help_handler = CommandHandler("help", help)

    application.add_handler(start_handler)
    application.add_handler(help_handler)

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    load_dotenv()

    main()
