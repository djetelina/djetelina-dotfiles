# coding=utf-8
"""Classes for various packages."""
import os
import logging
from pathlib import PosixPath
from typing import Union

from utils import async_subprocess

log = logging.getLogger(__name__)


class BasePackage:
    """Base package"""
    def __init__(self, name: str):
        self.name: str = name
        self._command = None

    async def is_installed(self) -> bool:
        """
        :return: Whether the package is installed
        """
        pass

    async def install(self):
        """Installs the package"""
        pass

    async def check_or_install(self):
        """Checks whether the package needs to be installed and if yes installs it"""
        log.debug(f'Starting check or install of {self.__class__.__name__} called {self.name}')
        installed = await self.is_installed()
        string_installed = 'is already' if installed else 'is not'
        log.debug(f'{self} {string_installed} installed')
        if not installed:
            log.info(f"Requirement \033[00;34m'{self.name}'\033[0m needs to be installed, some action may be required.")
            log.info(f'Now calling `{self.command}`')
            await self.install()
            log.info(f'{self} has been installed')

    @property
    def command(self):
        return self._command

    @command.setter
    def command(self, command):
        self._command = command

    def __str__(self):
        return '%s %s' % (self.__class__.__name__, self.name)


# TODO apt package class

class PipPackage(BasePackage):
    """Packages on pip"""
    def __init__(self, name: str, pip2: bool = False):
        super().__init__(name)
        self.pip = 'pip2' if pip2 else 'pip'

    async def is_installed(self) -> bool:
        return await async_subprocess(f'{self.pip} freeze', grep=f"{self.name}")

    async def install(self):
        await async_subprocess(f'{self.pip} install --user {self.name}')

    @property
    def command(self):
        return f'{self.pip} install --user {self.name}'


class NonPackage(BasePackage):
    """
    Various plugins etc. that aren't installed through any package manager, usually copied from git
    """
    def __init__(self, name: str, exists_path: PosixPath, command_dir: Union[PosixPath, None], install_command: str):
        super().__init__(name)
        self.exists_path: PosixPath = exists_path
        self.command_dir: PosixPath = command_dir
        self.install_command: str = install_command
        self.command = install_command

    async def is_installed(self) -> bool:
        return self.exists_path.exists()

    async def install(self):
        if self.command_dir is not None:
            os.chdir(str(self.command_dir))
        await async_subprocess(self.install_command, silent=True)
