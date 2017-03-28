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
# Less syntax highlighting :)
export LESS=' -RN '
export LESSOPEN="| /usr/share/source-highlight/src-hilite-lesspipe.sh %s"
# Some variables
export PATH=$PATH:~/.local/bin:~/mygo/bin
export ZSH=~/.oh-my-zsh
export LANG=en_US.UTF-8
export EDITOR='vim'
export BROWSER='chrome'

###################
# PLUGIN SELECTOR #
###################
plugins=(command-not-found debian gitfast k zsh-syntax-highlighting dotenv heroku)

############################
# DIRECTORY HISTORY PLUGIN #
############################
# No oh-my-zsh hook :(
source ~/zsh-directory-history/directory-history.plugin.zsh
# Some key bindings for this
bindkey '\e[A' directory-history-search-backward
bindkey '\e[B' directory-history-search-forward
bindkey '^j' history-substring-search-up
bindkey '^k' history-substring-search-down

###########
# THEMING #
###########
ZSH_THEME="powerlevel9k/powerlevel9k"
POWERLEVEL9K_MODE='awesome-fontconfig'
POWERLEVEL9K_SHORTEN_DIR_LENGTH=3
POWERLEVEL9K_SHORTEN_STRATEGY="truncate_middle"
POWERLEVEL9K_PROMPT_ON_NEWLINE=false
POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(time context dir root_indicator)
POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=(status virtualenv vcs)
POWERLEVEL9K_TIME_BACKGROUND="green"
POWERLEVEL9K_TIME_FOREGROUND="black"
POWERLEVEL9K_DIR_HOME_BACKGROUND="green"
POWERLEVEL9K_DIR_HOME_FOREGROUND="black"
POWERLEVEL9K_DIR_HOME_SUBFOLDER_BACKGROUND="green"
POWERLEVEL9K_DIR_HOME_SUBFOLDER_FOREGROUND="black"
POWERLEVEL9K_DIR_DEFAULT_BACKGROUND="black"
POWERLEVEL9K_DIR_DEFAULT_FOREGROUND="green"
POWERLEVEL9K_OS_ICON_BACKGROUND="blue"
POWERLEVEL9K_OS_ICON_FOREGROUND="black"
POWERLEVEL9K_STATUS_OK_BACKGROUND="green"
POWERLEVEL9K_STATUS_OK_FOREGROUND="green"
POWERLEVEL9K_CONTEXT_DEFAULT_BACKGROUND="black"
POWERLEVEL9K_CONTEXT_DEFAULT_FOREGROUND="green"
POWERLEVEL9K_CONTEXT_ROOT_BACKGROUND="black"
POWERLEVEL9K_CONTEXT_ROOT_FOREGROUND="green"
POWERLEVEL9K_VIRTUALENV_BACKGROUND="black"
POWERLEVEL9K_VIRTUALENV_FOREGROUND="green"

###############
# KEYBINDINGS #
###############
bindkey "^[[1;5C" forward-word
bindkey "^[[1;5D" backward-word

###########
# ALIASES #
###########
source ~/.bash_aliases
source ~/.zsh_aliases

#################################
# JENKINS CLIE CUSTOM FUNCTIONS #
#################################
# Default api kinda sucks
# now instead of typing `jenkins start deployed_clientzone_test` 
# just do `deploy clientzone test`

# Eventually this will be replaced by custom script with loads more functionality I think
function deploy() {
    if [ -n "$1" ]; then
        if [ -n "$2" ]; then
                env="$2"
        else
                env="dev"
        fi

        jenkins start deployed_"$1"_"$env"
    else
        echo "I need an argument - what do you want to deploy?"
    fi
}

function unittest() {
    if [ -n "$1" ]; then
        if [ -n "$2" ]; then
                env="$2"
        else
                env="dev"
        fi

        jenkins start test_"$1"_"$env"
    else
        echo "I need an argument - what do you want to deploy?"
    fi
}

#----------------------------------------------------------------------

# Load oh-my-zsh, this should always be at the bottom
source $ZSH/oh-my-zsh.sh