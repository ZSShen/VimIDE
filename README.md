# **VimIDE**  

VimIDE is configured to be efficient for source code exploration and development under ***Mac*** and ***Linux***. It is now targeting on ***C++*** and ***Python***. Since all the configuration is managed by [Vundle], please make sure that Vundle is properly installed if you interest in VimIDE.  


## **Installation**


## **Usage**


## **Plugin**  
The primary plugins which VimIDE leverages for configuration.  

### [Monota]
Enhanced ***Monokai-like*** color scheme for c++.  

### [PowerLine]
PowerLine allows you to create better-looking, more functional Vim status bar.  

### [NERDTree]
NERDTree works as the ***project drawer*** which helps you to explore filesystem and to open files and directories.  

**Customization**
  + Automatically turn on NERDTree when vim starts up on opening a directory.  
  + Show hidden files.  
  + Map `<C-N>` to toggle NERDTree.  

### [YouCompleteMe]
An ultimate source code exploration and completion engine for most of the prevalent programming languages.  

**Customization**  
  + Reimplement the plugin `.ycm_extra_conf.py` for YCM to enhance the preciseness for C families.  
  + Map `<F12>` to command `YcmCompleter GoTo`.  


[Vundle]:https://github.com/VundleVim/Vundle.vim
[Monota]:https://github.com/filfirst/Monota
[NERDTree]:https://github.com/scrooloose/nerdtree
[PowerLine]:https://github.com/Lokaltog/vim-powerline
[YouCompleteMe]:https://github.com/Valloric/YouCompleteMeUse
