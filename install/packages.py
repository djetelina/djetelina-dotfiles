# coding=utf-8
"""
Classes for various packages.
"""
import asyncio
from pathlib import PosixPath
from typing import Union

from utils import async_subprocess


class BasePackage:
    def is_installed(self) -> bool:
        """
        :return: Whether the package is installed
        """
        pass

    def install(self):
        """
        Installs the package 
        """
        pass


# TODO apt and pip package classes


class NonPackage(BasePackage):
    """
    Various plugins etc. that aren't installed through any package manager, usually copied from git
    """
    def __init__(self, name: str, exists_path: PosixPath, command_dir: Union[PosixPath, None], install_command: str):
        self.name: str = name
        self.exists_path: PosixPath = exists_path
        self.command_dir: PosixPath = command_dir
        self.install_command: str = install_command

    def is_installed(self) -> bool:
        return self.exists_path.exists()

    def install(self):
        if self.command_dir is not None:
            # TODO uhhh, how does this work?
            pass
        async_subprocess(asyncio.get_event_loop(), self.install_command.split(" "), silent=True)
