colorscheme monokai
syntax enable
set nocompatible
execute pathogen#infect()
filetype plugin indent on
set smartindent
set ruler
set backspace=2
set tabstop=4
set softtabstop=4
set expandtab
set number
set showcmd
set cursorline
set wildmenu
set lazyredraw
set showmatch
set incsearch
set hlsearch
set rtp+=$HOME/.local/lib/python2.7/site-packages/powerline/bindings/vim/
set whichwrap+=<,>,h,l,[,]
set laststatus=2
set t_Co=256
set mouse=a
set list
set listchars=tab:>-
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*

let g:syntastic_always_populate_loc_list = 1
let g:syntastic_aggregate_errors = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0
let g:syntastic_python_checkers = ['flake8', 'pydocstyle', 'python']
let g:syntastic_python_flake8_args = "--ignore E501,E126,F401,E124,E402,W503,E121"
let g:syntastic_sh_shellcheck_args = "-e SC2059 -e SC2046"