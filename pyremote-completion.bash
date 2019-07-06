#!/usr/bin/env bash

_pyremote_completions()
{
    if [ "${#COMP_WORDS[@]}" != "2" ]; then
        return
    fi
    
    COMPREPLY=($(compgen -W "$(pyremote.py --autocompletion)" "${COMP_WORDS[1]}"))
}

complete -F _pyremote_completions pyremote.py
complete -F _pyremote_completions pyremote