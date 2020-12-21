# System
alias ssh="ssh -X"
alias vim="vim -u ~/.vimrc"
alias aptu='sudo apt update && sudo apt upgrade && sudo apt autoremove'
alias brewu='brew update; brew upgrade; brew cleanup; brew doctor'
alias ccat='pygmentize -O style=monokai -f console256 -g'
alias vpn_pico='security find-generic-password -s "VPN" -w | sudo openconnect -q --user=$(whoami) --authgroup=default --passwd-on-stdin --non-inter VPN_ADDRESS --reconnect-timeout 12000'
