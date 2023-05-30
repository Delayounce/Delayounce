from main import *

import cProfile
import asyncio


def run_async_function():
    asyncio.run(read_item(Request))

cProfile.runctx('run_async_function()', globals(), locals())