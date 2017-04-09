# coding=utf-8
"""
Utility functions
"""
import asyncio
import logging as log
import os
import sys

from typing import List


async def async_subprocess(loop: asyncio.events.AbstractEventLoop, cmd: List[str], silent: bool=True) -> int:
    """
    Wrapper around :pyfunc:`asyncio.create_subprocess_exec` for easier use (silent/non-silent running)
    
    :param loop:    Event loop
    :param cmd:     Command to run, split into a list
    :param silent:  Whether stding and stdout should communicate with user, or if it should run in silence
    :return:        Return code of the process
    """
    log.debug(f'Calling subprocess asynchronously: `{" ".join(cmd)}`')
    stdin = sys.stdin if not silent else open(os.devnull, 'wb')
    stdout = sys.stdout if not silent else open(os.devnull, 'wb')
    stderr = sys.stderr if not silent else open(os.devnull, 'wb')
    proc = await asyncio.create_subprocess_exec(*cmd,
        stdin=stdin, stdout=stdout, stderr=stderr
    )
    return_code: int = proc.returncode
    log.debug(f'{return_code} was returned by subprocess `{"".join(cmd)}`')
    return return_code
