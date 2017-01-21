# **VimIDE**  

VimIDE is configured to be efficient for source code exploration and development under ***Mac*** and ***Linux***. It is now targeting on ***C++*** and ***Python***.    


## **Installation**
Assume the absolute path of your local repo is `REPO_DIRECTORY`.  
```shell
$ git clone https://github.com/ZSShen/VimIDE.git REPO_DIRECTORY
$ cd REPO_DIRECTORY
$ ./install.sh
```

## **Usage**
Assume the absolute path of your project is `PROJECT_DIRECTORY`.  
```shell
$ cp REPO_DIRECTORY/.ycm_extra_conf.py PROJECT_DIRECTORY
```
The configuration should be copied only once. Then launch your Vim:  
```shell
$ vim PROJECT_DIRECTORY
```

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


## **Contact**
Please contact me via the mail andy.zsshen@gmail.com.  
Note that the configuration is still under tuning. Recommendation and bug report are desired.  
