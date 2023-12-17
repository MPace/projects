import os
import pathlib
import logging
from logging.config import dictConfig
from dotenv import load_dotenv
import discord



load_dotenv()

BOT_SECRET = os.getenv("BOT_TOKEN")

GUILD_ID = discord.Object(id=int(os.getenv("GUILD")))

USER_ID = discord.Object(id=int(os.getenv('USER')) )

BASE_DIR = pathlib.Path(__file__).parent

LOGGING_CONFIG = {
    "version": 1,
    "disabled_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)-10s - %(asctime)s - %(module)-15s : %(message)s"
        },
        "standard": {"format": "%(levelname)-10s - %(name)-15s : %(message)s"},
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "standard",
        },
        "console2": {
            "level": "WARNING",
            "class": "logging.StreamHandler",
            "formatter": "standard",
        },
#        "file": {
#            "level": "INFO",
#            "class": "logging.FileHandler",
#            "filename": "logs/infos.log",
#            "mode": "w",
#            "formatter": "verbose",
#        },
    },
    "loggers": {
        "bot": {"handlers": ["console"], "level": "INFO", "propagate": False},
        "discord": {
            "handlers": ["console2"],
            "level": "INFO",
            "propagate": False,
        },
    },
}

dictConfig(LOGGING_CONFIG)

