#!/usr/bin/env python
# coding: utf-8
import os
import argparse
import logging
import logging.handlers

LOG_LEVEL = logging.INFO

# root loggerに対して設定することで、これ以後使うloggerすべてに共通の設定が適用される。
logger = logging.getLogger("")
formatter = logging.Formatter(
    fmt="%(asctime)s:[%(name)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
logger.setLevel(LOG_LEVEL)

# stdout出力
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel(LOG_LEVEL)
logger.addHandler(stream_handler)

# ログ出力
file_handler = logging.handlers.RotatingFileHandler(
    os.path.join(os.path.abspath(os.path.dirname(__file__)), "log", "app.log"),
    maxBytes=1000000, backupCount=50)
file_handler.setFormatter(formatter)
file_handler.setLevel(LOG_LEVEL)
logger.addHandler(file_handler)
