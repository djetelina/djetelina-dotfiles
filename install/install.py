import os
import sys
import asyncio
import subprocess
from pathlib import Path, PosixPath

from tqdm import tqdm

import prerequisites as reqs

CURRENT_DIR: PosixPath = Path.cwd()
SCRIPT_DIR: PosixPath = PosixPath(os.path.dirname(os.path.realpath(__file__))).parent


async def async_subprocess(loop, cmd, silent=True):
    stdin = sys.stdin if not silent else open(os.devnull, 'wb')
    stdout = sys.stdout if not silent else open(os.devnull, 'wb')
    stderr = sys.stderr if not silent else open(os.devnull, 'wb')
    proc = await asyncio.create_subprocess_exec(*cmd,
        stdin=stdin, stdout=stdout, stderr=stderr
    )
    return proc.returncode


def install_apt(loop):
    print('Checking and installing apt packages')
    with tqdm(total=len(reqs.apt), desc='Apt packages', unit=' packages') as t:
        done = 0
        for package in reqs.apt:
            not_installed = subprocess.call(f'dpkg-query -s {package}'.split(),
                                            stdin=open(os.devnull, 'wb'), stdout=open(os.devnull, 'wb'))
            if not_installed:
                print(f'Apt package {package} required, you might be prompted for a password')
                subprocess.call(f'sudo apt-get install {package}'.split())
            done += 1
            t.update(done)


async def install_pip(loop):
    print('Checking and installing pip packages')
    with tqdm(total=len(reqs.pip2) + len(reqs.pip_default), desc='Pip packages', unit=' packages') as t:
        done = 0
        for package in reqs.pip2:
            await async_subprocess(loop, f'pip2 install --user --upgrade {package}'.split())
            done += 1
            t.update(done)
        for package in reqs.pip_default:
            await async_subprocess(loop, f'pip install --user --upgrade {package}'.split())
            done += 1
            t.update(done)


async def main(loop):
    install_apt(loop)
    await install_pip(loop)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
