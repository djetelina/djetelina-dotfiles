from pathlib import PosixPath
from typing import Union


class NonPackageRequisite:
    def __init__(self, name: str, exists_path: PosixPath, command_dir: Union[PosixPath, None], install_command: str):
        self.name: str = name
        self.exists_path: PosixPath = exists_path
        self.command_dir: PosixPath = command_dir
        self.install_command: str = install_command

    def is_installed(self) -> bool:
        return self.exists_path.exists()
