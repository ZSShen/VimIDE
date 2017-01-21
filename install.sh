#!/usr/bin/env bash


# Copy the VimIDE configuration.
{
    cp .vimrc ~/.vimrc
    cp .ycm_extra_conf.py ~/.ycm_extra_conf
} &> /dev/null

# Install Vundle plugin.
echo "Installing Vundle ..."
echo ""
{
    git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
} &> /dev/null

# Install VimIDE included 3 party plugins.
echo "Installing VimIDE included plugins ..."
echo "Within 5 minutes ..."
echo ""
{
    vim +PluginInstall +qall
} &> /dev/null

echo "Installing YCM Clang completer ..."
echo "Need 15 to 20 minutes ..."
echo ""
{
    cd ~/.vim/bundle/YouCompleteMe
    ./install.py --clang-completer
} > /dev/null

