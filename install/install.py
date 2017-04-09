# coding=utf-8
"""Install dotfiles and workplace with this file :)"""
import asyncio
import logging as log
import os
import subprocess
from pathlib import Path, PosixPath

from tqdm import tqdm

import requirements as reqs
from utils import async_subprocess

CURRENT_DIR: PosixPath = Path.cwd()
SCRIPT_DIR: PosixPath = PosixPath(os.path.dirname(os.path.realpath(__file__))).parent


def install_apt():
    """
    Installs all apt packages
    """
    log.debug('Install apt start')
    print('Checking and installing apt packages')
    with tqdm(total=len(reqs.apt), desc='Apt packages', unit=' packages') as t:
        done = 0
        for package in reqs.apt:
            log.debug(f'Starting apt install of {package}')
            not_installed = subprocess.call(f'dpkg-query -s {package}'.split(),
                                            stdin=open(os.devnull, 'wb'), stdout=open(os.devnull, 'wb'))
            string_installed = 'is not' if not_installed else 'is'
            log.debug(f'Apt package {package} {string_installed} installed')
            if not_installed:
                log.debug(f'Apt package {package} needs to be installed, calling apt-get install')
                print(f'Apt package {package} required, you might be prompted for a password')
                subprocess.call(f'sudo apt-get install {package}'.split())
            done += 1
            t.update(done)
            log.debug(f'Done with apt install of {package}')
    log.debug('Install apt end')


async def install_pip(loop: asyncio.events.AbstractEventLoop):
    """
    Installs all pip packages for both python2.7 and system default python
    
    :param loop:    Event loop
    """
    log.debug('Install pip start')
    print('Checking and installing pip packages')
    with tqdm(total=len(reqs.pip2) + len(reqs.pip_default), desc='Pip packages', unit=' packages') as t:
        done = 0
        log.debug('Starting with pip2')
        for package in reqs.pip2:
            log.debug(f'Installing pip2 package {package}')
            await async_subprocess(loop, f'pip2 install --user --upgrade {package}'.split())
            done += 1
            t.update(done)
            log.debug(f'Done with installing pip2 package {package}')
        log.debug('Starting with default pip')
        for package in reqs.pip_default:
            log.debug(f'Installing default pip package {package}')
            await async_subprocess(loop, f'pip install --user --upgrade {package}'.split())
            done += 1
            t.update(done)
            log.debug(f'Done with installing default pip package {package}')
    log.debug('Install pip end')


def create_directories():
    """
    Creates all required directories if they don't exist
    """
    #TODO the new loading bar should soon be ready
    log.debug('Create directories start')
    done = 0
    for directory in reqs.directories:
        if not directory.exists():
            log.info(f"Creating directory {directory} that didn't exist")
            directory.mkdir(parentrs=True, exist_ok=True)
        else:
            log.debug(f'Directory {directory} already exists')
        done += 1
    log.debug('Create directories end')


async def main(loop):
    """
    Main function, it's important not to mess around with the order.
    
    :param loop:    Event loop
    """
    log.debug('Starting the main function')
    create_directories()
    install_apt()
    await install_pip(loop)

if __name__ == '__main__':
    loop: asyncio.events.AbstractEventLoop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
