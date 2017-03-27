if [ "$HOST" = "david-Latitude-E7470" ]; then
    DEFAULT_USER="david"
else
    DEFAULT_USER="djetelina"
fi

export PATH=$PATH:~/.local/bin:~/mygo/bin
export ZSH=~/.oh-my-zsh
export LESS=' -RN '
export LESSOPEN="| /usr/share/source-highlight/src-hilite-lesspipe.sh %s"

ZSH_THEME="powerlevel9k/powerlevel9k"

# POWERLEVEL stuff
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

# Normal stufff
HYPHEN_INSENSITIVE="true"
ENABLE_CORRECTION="true"
COMPLETION_WAITING_DOTS="true"
DISABLE_UNTRACKED_FILES_DIRTY="true"
HIST_STAMPS="dd.mm.yyyy"

# ZSH Plugins
plugins=(command-not-found debian gitfast k)

source $ZSH/oh-my-zsh.sh

export LANG=en_US.UTF-8
export EDITOR='vim'

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

alias zshconfig="vim ~/.zshrc"
alias ssh="ssh -X"
bindkey '\e[A' directory-history-search-backward
bindkey '\e[B' directory-history-search-forward
bindkey '^j' history-substring-search-up
bindkey '^k' history-substring-search-down
bindkey "^[[1;5C" forward-word
bindkey "^[[1;5D" backward-word


source ~/.zsh_aliases
source ~/zsh-directory-history/directory-history.plugin.zsh
source ~/.bash_aliases
source /home/david/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
