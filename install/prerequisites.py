from pathlib import Path, PosixPath
from typing import List

import packages

HOME = Path.home()

existing_dirs: List[PosixPath] = [
    HOME / '.vim' / ' autoload',
    HOME / '.vim' / 'bundle',
    HOME / '.vim' / 'colors'
]

apt: List[str] = [
    'python2.7',
    'shellcheck',
    'python-pip',
    'python3-pip',
    'python3.6',
    'zsh',
    'curl',
    'vim',
]

pip2: List[str] = [
    'powerline-status'
]

pip_default: List[str] = [
    'python-jenkins',
    'pydocstyle',
    'flake8'
]
vim_plugins: List[packages.NonPackageRequisite] = [
    packages.NonPackageRequisite(
        name='pathogen',
        exists_path=HOME / '.vim' / 'autoload' / 'pathogen.vim',
        command_dir=None,
        install_command='curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim'
    ),
    packages.NonPackageRequisite(
        name='syntastic',
        exists_path=HOME / '.vim' / 'bundle' / 'syntastic',
        command_dir=HOME / '.vim' / 'bundle',
        install_command='git clone --depth=1 https://github.com/vim-syntastic/syntastic.git'
    ),
    packages.NonPackageRequisite(
        name='jedi-vim',
        exists_path=HOME / '.vim' / 'bundle' / 'jedi-vim',
        command_dir=HOME / '.vim' / 'bundle',
        install_command='git clone --recursive https://github.com/davidhalter/jedi-vim.git'
    ),
    packages.NonPackageRequisite(
        name='monokai',
        exists_path=HOME / '.vim' / 'colors' / 'monokai.vim',
        command_dir=None,
        install_command='curl -LSso ~/.vim/colors/monokai.vim '
                        'https://raw.githubusercontent.com/sickill/vim-monokai/master/colors/monokai.vim'
    )
]

zsh_plugins: List[packages.NonPackageRequisite] = [
    packages.NonPackageRequisite(
        name='oh-my-zsh',
        exists_path=HOME / '.oh-my-zsh',
        command_dir=None,
        install_command='sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"'
    ),
    packages.NonPackageRequisite(
        name='k',
        exists_path=HOME / '.oh-my-zsh' / 'custom' / 'plugins' / 'k',
        command_dir=HOME / '.oh-my-zsh' / 'custom' / 'plugins',
        install_command='git clone https://github.com/supercrabtree/k'
    ),
    packages.NonPackageRequisite(
        name='zsh-syntax-highlighting',
        exists_path=HOME / '.oh-my-zsh' / 'custom' / 'plugins' / 'zsh-syntax-highlighting',
        command_dir=HOME / '.oh-my-zsh' / 'custom' / 'plugins',
        install_command='git clone https://github.com/zsh-users/zsh-syntax-highlighting.git'
    ),
    packages.NonPackageRequisite(
        name='directory history',
        exists_path=PosixPath('/usr/bin/dirhist'),
        command_dir=HOME,
        install_command='git clone https://github.com/tymm/zsh-directory-history && '
                        'sudo cp "$HOME/zsh-directory-history/dirhist" /usr/bin',
    ),
    packages.NonPackageRequisite(
        name='powerlevel9k',
        exists_path=HOME / '.oh-my-zsh' / 'custom' / 'themes' / 'powerlevel9k',
        command_dir=HOME / 'oh-my-zsh' / 'custom' / 'themes',
        install_command='git clone https://github.com/bhilburn/powerlevel9k.git'
    )
]
