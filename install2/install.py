#!/usr/bin/env python3
# coding=utf-8
import sys
import getpass

import sh

OUTPUT_WIDTH = 80


def red(text):
    return '\033[0;31m{0}\033[0m'.format(text)


def green(text):
    return '\033[00;32m{0}\033[0m'.format(text)


def blue(text):
    return '\033[00;34m{0}\033[0m'.format(text)


def grey(text):
    return '\033[00;37m{0}\033[0m'.format(text)


def install_apt_package(package, password):
    try:
        dpkg_query_result = sh.dpkg_query('-W', "-f='${Status}'", package)
    except sh.ErrorReturnCode_1:
        if password is None:
            p = sh.apt_get('install', '-y', package, _bg=True)
        else:
            with sh.contrib.sudo(password=password, _with=True):
                p = sh.apt_get('install', '-y', package, _bg=True)
        print('{package:.<{spacing}}{status:.>29}'.format(package=package, status=blue('Installing'),
                                                          spacing=OUTPUT_WIDTH-17), end='\r')
        p.wait()
        print('{package:.<{spacing}}{status:.>29}         '.format(package=package, status=green('Installed!'),
                                                                   spacing=OUTPUT_WIDTH-17))

    else:
        print('{package:.<{spacing}}{status:.>29}'.format(package=package, status=grey('already installed'),
                                                          spacing=OUTPUT_WIDTH-17))


def install_from_curl(name, test_file, make_dirs, curl_args):
    pass


def install_from_git(name, test_file, cd_into, clone_args):
    pass


def main():
    print('\n')
    print(green('#' * OUTPUT_WIDTH))
    print(green('# {0:^{width}} #').format('DJetelina .files', width=OUTPUT_WIDTH-4))
    print(green('#' * OUTPUT_WIDTH))
    sh.git('pull')

    if sh.whoami() == 'root':
        password = None
    else:
        password = getpass.getpass(prompt='[sudo] password for {}: '.format(getpass.getuser()))
        with sh.contrib.sudo(password=password, _with=True):
            try:
                sh.sudo('-n', 'true')
            except sh.ErrorReturnCode_1:
                print(red('Invalid password :('))
                sys.exit(1)

    target = input(blue('Install GUI related packages? (y/n): '))
    if target == 'y':
        gui_packages = True
    elif target == 'n':
        gui_packages = False
    else:
        print(red('Unrecognized input'))
        sys.exit(1)

    apt_basic = ['python2.7', 'shellcheck', 'python-pip', 'python3-pip', 'zsh', 'curl', 'vim', 'apt-listchanges']
    apt_gui = ['i3', 'i3lock', 'i3blocks', 'i3status']

    print(green('\n{0:^{width}}').format('aptitude basic', width=OUTPUT_WIDTH))
    print(green('=' * OUTPUT_WIDTH))
    for package in apt_basic:
        install_apt_package(package, password)
    print(green('Done!'))
    if gui_packages:
        print(green('\n{0:^{width}}').format('aptitude GUI', width=OUTPUT_WIDTH))
        print(green('=' * OUTPUT_WIDTH))
        for package in apt_gui:
            install_apt_package(package, password)
        print(green('Done!'))

    pip2_packages = ['powerline-status']
    default_pip_packages = ['pydocstyle', 'flake8', 'pipenv']

    try:
        sh.which('pip2')
    except sh.ErrorReturnCode_1:
        pip2 = False
    else:
        pip2 = True

    print(green('\n{0:^{width}}').format('python2 packages', width=OUTPUT_WIDTH))
    print(green('=' * OUTPUT_WIDTH))
    if pip2:
        installed_packages = [installed.split('=')[0] for installed in sh.pip2('freeze', _iter=True)]
        for package in pip2_packages:
            if package in installed_packages:
                print('{package:.<{spacing}}{status:.>29}'.format(package=package, status=blue('Updating'),
                                                                  spacing=OUTPUT_WIDTH - 17), end='\r')
            else:
                print('{package:.<{spacing}}{status:.>29}'.format(package=package, status=blue('Installing'),
                                                                  spacing=OUTPUT_WIDTH - 17), end='\r')
            sh.pip2('-q', '-q', '-q', 'install', '--user', '--upgrade', package)

            print('{package:.<{spacing}}{status:.>29}         '.format(package=package, status=green('Up to date'),
                                                                       spacing=OUTPUT_WIDTH - 17))
    else:
        installed_packages = [installed.split('=')[0] for installed in sh.pip('freeze', _iter=True)]
        for package in pip2_packages:
            if package in installed_packages:
                print('{package:.<{spacing}}{status:.>29}'.format(package=package, status=blue('Updating'),
                                                                  spacing=OUTPUT_WIDTH - 17), end='\r')
            else:
                print('{package:.<{spacing}}{status:.>29}'.format(package=package, status=blue('Installing'),
                                                                  spacing=OUTPUT_WIDTH - 17), end='\r')
            sh.pip('-q', '-q', '-q', 'install', '--user', '--upgrade', package)

            print('{package:.<{spacing}}{status:.>29}         '.format(package=package, status=green('Up to date'),
                                                                       spacing=OUTPUT_WIDTH - 17))

    print(green('\n{0:^{width}}').format('python packages', width=OUTPUT_WIDTH))
    print(green('=' * OUTPUT_WIDTH))
    installed_packages = [installed.split('=')[0] for installed in sh.pip('freeze', _iter=True)]
    for package in default_pip_packages:
        if package in installed_packages:
            print('{package:.<{spacing}}{status:.>29}'.format(package=package, status=blue('Updating'),
                                                              spacing=OUTPUT_WIDTH - 17), end='\r')
        else:
            print('{package:.<{spacing}}{status:.>29}'.format(package=package, status=blue('Installing'),
                                                              spacing=OUTPUT_WIDTH - 17), end='\r')
        sh.pip('-q', '-q', '-q', 'install', '--user', '--upgrade', package)

        print('{package:.<{spacing}}{status:.>29}         '.format(package=package, status=green('Up to date'),
                                                                   spacing=OUTPUT_WIDTH - 17))

    install_from_curl('pathogen', '~/.vim/autoload/pathogen.vim', ['~/.vim/autoload', '~/.vim/bundle'],
                      curl_args=['-LSso', '~/.vim/autoload/pathogen.vim', 'https://tpo.pe/pathogen.vim'])
    install_from_git('Syntastic', '$HOME/.vim/bundle/syntastic', '~/.vim/bundle',
                     ['--depth=1', 'https://github.com/vim-syntastic/syntastic.git'])


if __name__ == '__main__':
    main()
