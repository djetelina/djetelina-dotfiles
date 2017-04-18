# coding=utf-8
"""
Config-like file, if you want to install different packages and/or plugins, edit this file only.
"""
from pathlib import Path, PosixPath
from typing import List

import packages

HOME = Path.home()
# Directories to create if they don't already exist
# These are created for vim plugins, so you can just clone into desired directory
# without getting any errors
directories: List[PosixPath] = [
    HOME / '.vim' / 'autoload',
    HOME / '.vim' / 'bundle',
    HOME / '.vim' / 'colors'
]

# Apt packages to install
apt: List[packages.AptPackage] = [
    packages.AptPackage(name='python2.7'),
    packages.AptPackage(name='shellcheck'),
    packages.AptPackage(name='python-pip'),
    packages.AptPackage(name='python3-pip'),
    packages.AptPackage(name='python3.6'),
    packages.AptPackage(name='zsh'),
    packages.AptPackage(name='curl'),
    packages.AptPackage(name='vim'),
]

pip: List[packages.PipPackage] = [
    packages.PipPackage(name='powerline-status', pip2=True),
    packages.PipPackage(name='python-jenkins'),
    packages.PipPackage(name='pydocstyle'),
    packages.PipPackage(name='flake8')
]

# Vim plugins to install
vim_plugins: List[packages.NonPackage] = [
    packages.NonPackage(
        name='pathogen',
        exists_path=HOME / '.vim' / 'autoload' / 'pathogen.vim',
        command_dir=None,
        install_command='curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim'
    ),
    packages.NonPackage(
        name='syntastic',
        exists_path=HOME / '.vim' / 'bundle' / 'syntastic',
        command_dir=HOME / '.vim' / 'bundle',
        install_command='git clone --depth=1 https://github.com/vim-syntastic/syntastic.git'
    ),
    packages.NonPackage(
        name='jedi-vim',
        exists_path=HOME / '.vim' / 'bundle' / 'jedi-vim',
        command_dir=HOME / '.vim' / 'bundle',
        install_command='git clone --recursive https://github.com/davidhalter/jedi-vim.git'
    ),
    packages.NonPackage(
        name='monokai',
        exists_path=HOME / '.vim' / 'colors' / 'monokai.vim',
        command_dir=None,
        install_command='curl -LSso ~/.vim/colors/monokai.vim '
                        'https://raw.githubusercontent.com/sickill/vim-monokai/master/colors/monokai.vim'
    )
]

# Zsh plugins to install
zsh_plugins: List[packages.NonPackage] = [
    packages.NonPackage(
        name='oh-my-zsh',
        exists_path=HOME / '.oh-my-zsh',
        command_dir=None,
        install_command='sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"'
    ),
    packages.NonPackage(
        name='k',
        exists_path=HOME / '.oh-my-zsh' / 'custom' / 'plugins' / 'k',
        command_dir=HOME / '.oh-my-zsh' / 'custom' / 'plugins',
        install_command='git clone https://github.com/supercrabtree/k'
    ),
    packages.NonPackage(
        name='zsh-syntax-highlighting',
        exists_path=HOME / '.oh-my-zsh' / 'custom' / 'plugins' / 'zsh-syntax-highlighting',
        command_dir=HOME / '.oh-my-zsh' / 'custom' / 'plugins',
        install_command='git clone https://github.com/zsh-users/zsh-syntax-highlighting.git'
    ),
    packages.NonPackage(
        name='directory history',
        exists_path=PosixPath('/usr/bin/dirhist'),
        command_dir=HOME,
        install_command='git clone https://github.com/tymm/zsh-directory-history && '
                        'sudo cp "$HOME/zsh-directory-history/dirhist" /usr/bin',
    ),
    packages.NonPackage(
        name='powerlevel9k',
        exists_path=HOME / '.oh-my-zsh' / 'custom' / 'themes' / 'powerlevel9k',
        command_dir=HOME / 'oh-my-zsh' / 'custom' / 'themes',
        install_command='git clone https://github.com/bhilburn/powerlevel9k.git'
    )
]
