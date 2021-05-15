#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from pathlib import Path

import click

from click_project.decorators import (
    argument,
    flag,
    option,
    command,
    use_settings,
    table_format,
    table_fields,
)
from click_project.lib import (
    TablePrinter,
    call,
)
from click_project.config import config
from click_project.log import get_logger
from click_project.types import DynamicChoice


LOGGER = get_logger(__name__)


import cowsay

@command()
@argument("what", help="What to say")
@option("--who", type=click.Choice(cowsay.char_names), help="Who says", default="cow")
def say(what, who):
    "Say something with style"
    getattr(cowsay, who)(what)
