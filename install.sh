#!/usr/bin/env bash


# Copy the VimIDE configuration.
cp .vimrc ~/.vimrc
cp .ycm_extra_conf.py ~/.ycm_extra_conf


# Install Vundle plugin.
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim


# Install VimIDE included 3 party plugins.
vim +PluginInstall +qall


