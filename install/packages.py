# coding=utf-8
"""
Classes for various packages.
"""
import asyncio
import logging
from pathlib import PosixPath
from typing import Union

from utils import async_subprocess

log = logging.getLogger(__name__)


class BasePackage:
    def __init__(self):
        self.name = None

    async def is_installed(self) -> bool:
        """
        :return: Whether the package is installed
        """
        pass

    async def install(self):
        """
        Installs the package 
        """
        pass

    def __str__(self):
        return self.name


# TODO apt package class

class PipPackage(BasePackage):
    """
    Packages on pip
    """
    def __init__(self, name: str, pip2: bool=False):
        self.name = name
        self.pip = 'pip2' if pip2 else 'pip'

    async def is_installed(self) -> bool:
        not_installed = await async_subprocess(f'{self.pip} freeze | grep "{self.name}"'.split())
        return not not_installed

    async def install(self):
        await async_subprocess(f'{self.pip} install --user {self.name}'.split())


class NonPackage(BasePackage):
    """
    Various plugins etc. that aren't installed through any package manager, usually copied from git
    """
    def __init__(self, name: str, exists_path: PosixPath, command_dir: Union[PosixPath, None], install_command: str):
        self.name: str = name
        self.exists_path: PosixPath = exists_path
        self.command_dir: PosixPath = command_dir
        self.install_command: str = install_command

    async def is_installed(self) -> bool:
        return self.exists_path.exists()

    async def install(self):
        if self.command_dir is not None:
            # TODO uhhh, how does this work?
            pass
        await async_subprocess(self.install_command.split(" "), silent=True)

