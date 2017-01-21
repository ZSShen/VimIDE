#!/usr/bin/env bash


# Copy the VimIDE configuration.
{
    cp .vimrc ~/.vimrc
    cp .ycm_extra_conf.py ~/.ycm_extra_conf
} &> /dev/null

# Install Vundle plugin.
echo "Installing Vundle ..."
{
    git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
} > /dev/null

# Install VimIDE included 3 party plugins.
echo "Installing VimIDE included plugins ..."
{
    vim +PluginInstall +qall
} > /dev/null

