# coding=utf-8
"""Install dotfiles and workplace with this file :)"""
import asyncio
import logging
import os
import subprocess
import argparse
from pathlib import Path, PosixPath
from traceback import format_exc
from typing import List, Callable

import requirements as reqs

CURRENT_DIR: PosixPath = Path.cwd()
SCRIPT_DIR: PosixPath = PosixPath(os.path.dirname(os.path.realpath(__file__))).parent


def install_apt():
    """Installs all apt packages"""
    log.info('Checking and installing apt packages')
    done = 0
    for package in reqs.apt:
        log.debug(f'Starting apt install of {package}')
        not_installed = subprocess.call(f'dpkg-query -s {package}'.split(),
                                        stdin=open(os.devnull, 'wb'), stdout=open(os.devnull, 'wb'))
        string_installed = 'is not' if not_installed else 'is'
        log.debug(f'Apt package {package} {string_installed} installed')
        if not_installed:
            log.info(f'Apt package {package} needs to be installed, calling apt-get install')
            subprocess.call(f'sudo apt-get install {package}'.split())
        done += 1
        log.debug(f'Done with apt install of {package}')
    log.debug('Install apt end')


async def install_pip():
    """
    Installs all pip packages for both python2.7 and system default python
    
    :param loop:    Event loop
    """
    log.info('Checking and installing pip packages')
    for package in reqs.pip:
        asyncio.ensure_future(package.check_or_install())


def create_directories():
    """Creates all required directories if they don't exist"""
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


def parse_arguments():
    parser = argparse.ArgumentParser(description='Script for setting up workplace on Debian based systems')
    parser.add_argument('logging') #TODO


async def main():
    """Main function, it's important not to mess around with the order."""
    log.debug('Starting the main function')
    create_directories()
    install_apt()
    async_installs: List[Callable] = [install_pip]
    for item in async_installs:
        asyncio.ensure_future(item())


def setup_logging():
    """Sets up logging"""
    log.setLevel(logging.DEBUG)

    console: logging.Handler = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter_console: logging.Formatter = logging.Formatter(
        '\033[92m{asctime}\033[0m: '
        '{message}',
        "%H:%M:%S",
        style='{'
    )
    console.setFormatter(formatter_console)
    log.addHandler(console)

    log_file: logging.Handler = logging.FileHandler(CURRENT_DIR / 'dotfiles.log', 'w', 'utf-8')
    log_file.setLevel(logging.DEBUG)
    formatter_file: logging.Formatter = logging.Formatter(
        '[{asctime}] {name}.{funcName}():{lineno} | {levelname} | {message}', "%d.%m.%Y %H:%M:%S", style='{'
    )
    log_file.setFormatter(formatter_file)
    log.addHandler(log_file)


if __name__ == '__main__':
    log: logging.Logger = logging.getLogger()
    setup_logging()
    loop: asyncio.events.AbstractEventLoop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
        pending = asyncio.Task.all_tasks()
        loop.run_until_complete(asyncio.gather(*pending))
        log.debug('Closing loop')
        loop.close()
    except Exception as e:
        log.error(f'Something unexpected happened:\n\n{format_exc()}')
