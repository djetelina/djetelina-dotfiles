# coding=utf-8
"""
Utility functions
"""
import asyncio
import logging
import os
import sys
from typing import Union

log = logging.getLogger(__name__)


async def async_subprocess(cmd: str, silent: bool=True, grep: Union[bool, str]=False) -> Union[bool, int]:
    """
    Wrapper around :pyfunc:`asyncio.create_subprocess_exec` for easier use (silent/non-silent running)
    
    :param cmd:     Command to run, split into a list
    :param silent:  Whether stdin and stdout should communicate with user, or if it should run in silence
    :param grep:    Completely changes the behavior and instead returns whether this string is in the first's output
    :return:        Return code of the process
    """
    log.debug(f'Calling subprocess asynchronously: `{cmd}`')
    stdin = sys.stdin if not silent else open(os.devnull, 'wb')
    stdout = sys.stdout if not silent else open(os.devnull, 'wb')
    stderr = sys.stderr if not silent else open(os.devnull, 'wb')
    if grep:
        stdout = asyncio.subprocess.PIPE

    proc = await asyncio.create_subprocess_exec(
        *cmd.split(), stdin=stdin, stdout=stdout, stderr=stderr
    )

    if grep:
        output, err_out = await proc.communicate()
        is_present = grep in output.decode()
        return is_present
    else:
        await proc.wait()

    return_code: int = proc.returncode
    log.debug(f'{return_code} was returned by subprocess `{cmd}`')
    return return_code
