###########
# GENERAL #
###########
# Self-explanatory settings
DEFAULT_USER=`whoami`
HYPHEN_INSENSITIVE="true"
ENABLE_CORRECTION="true"
COMPLETION_WAITING_DOTS="true"
DISABLE_UNTRACKED_FILES_DIRTY="true"
HIST_STAMPS="dd.mm.yyyy"
# Some variables
export PATH=$PATH:~/.local/bin:~/mygo/bin:/usr/local/bin/:$HOME/Library/Python/3.6/bin/:/usr/local/opt/libressl/bin
fpath+=~/.zfunc
export fpath=(~/.scli/zsh_completion.d $fpath); autoload -U compinit && compinit
export ZSH=~/.oh-my-zsh
export LANG=en_US.UTF-8
export EDITOR='vim'
#export BROWSER='chrome'
export BROWSER="open /Applications/Google\ Chrome.app/"
#Linux commit signing
export GPG_TTY=$(tty)
export CPPFLAGS=-I/usr/local/opt/openssl/include
export LDFLAGS=-L/usr/local/opt/openssl/lib

###################
# PLUGIN SELECTOR #
###################
plugins=(command-not-found debian gitfast k zsh-syntax-highlighting dotenv zsh-autosuggestions pip heroku)

###########
# THEMING #
###########
ZSH_THEME="powerlevel9k/powerlevel9k"
POWERLEVEL9K_MODE='nerdfont-complete'
POWERLEVEL9K_SHORTEN_DIR_LENGTH=2
POWERLEVEL9K_SHORTEN_STRATEGY="truncate_middle"
POWERLEVEL9K_DIR_OMIT_FIRST_CHARACTER=true
POWERLEVEL9K_FOLDER_ICON=''
POWERLEVEL9K_HOME_SUB_ICON=''
POWERLEVEL9K_DIR_PATH_SEPARATOR=' '
POWERLEVEL9K_PROMPT_ON_NEWLINE=false
POWERLEVEL9K_COMMAND_EXECUTION_TIME_THRESHOLD=0
POWERLEVEL9K_COMMAND_EXECUTION_TIME_PRECISION=0
POWERLEVEL9K_TIME_FORMAT="%D{%H:%M}"
POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(time context dir dir_writable root_indicator)
POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=(status disk_usage background_jobs kubecontext command_execution_time virtualenv vcs)
POWERLEVEL9K_COMMAND_EXECUTION_TIME_BACKGROUND="black"
POWERLEVEL9K_COMMAND_EXECUTION_TIME_FOREGROUND="green"
POWERLEVEL9K_TIME_BACKGROUND="black"
POWERLEVEL9K_TIME_FOREGROUND="green"
POWERLEVEL9K_DIR_HOME_BACKGROUND="green"
POWERLEVEL9K_DIR_HOME_FOREGROUND="black"
POWERLEVEL9K_DIR_HOME_SUBFOLDER_BACKGROUND="green"
POWERLEVEL9K_DIR_HOME_SUBFOLDER_FOREGROUND="black"
POWERLEVEL9K_DIR_DEFAULT_BACKGROUND="black"
POWERLEVEL9K_DIR_DEFAULT_FOREGROUND="green"
POWERLEVEL9K_OS_ICON_BACKGROUND="blue"
POWERLEVEL9K_OS_ICON_FOREGROUND="black"
POWERLEVEL9K_STATUS_OK_BACKGROUND="green"
POWERLEVEL9K_STATUS_OK_FOREGROUND="black"
POWERLEVEL9K_CONTEXT_DEFAULT_BACKGROUND="black"
POWERLEVEL9K_CONTEXT_DEFAULT_FOREGROUND="green"
POWERLEVEL9K_CONTEXT_ROOT_BACKGROUND="black"
POWERLEVEL9K_CONTEXT_ROOT_FOREGROUND="green"
POWERLEVEL9K_VIRTUALENV_BACKGROUND="black"
POWERLEVEL9K_VIRTUALENV_FOREGROUND="green"
POWERLEVEL9K_KUBECONTEXT_BACKGROUND="green"
POWERLEVEL9K_KUBECONTEXT_FOREGROUND="black"
POWERLEVEL9K_DISK_USAGE_ONLY_WARNING=true

###############
# KEYBINDINGS #
###############
bindkey "^[[1;5C" forward-word
bindkey "^[[1;5D" backward-word
# PyCharm
bindkey "\e\eOD" backward-word
bindkey "\e\eOC" forward-word

###########
# ALIASES #
###########
source ~/.bash_aliases
source ~/.zsh_aliases

test -e "${HOME}/.iterm2_shell_integration.zsh" && source "${HOME}/.iterm2_shell_integration.zsh"

#----------------------------------------------------------------------

# Load oh-my-zsh, this should always be at the bottom
source $ZSH/oh-my-zsh.sh
unsetopt correct_all
