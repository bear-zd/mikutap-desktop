# mikutap-desktop
使用python写的一个模仿mikutap的桌面程序，专门解决想我这样摸鱼必须有声音的人的需求，原版：https://aidn.jp/mikutap/

代码写的很粑粑，仅仅是给自己玩着用，希望未来能使用其他语言进行编写。修改代码播放自己想要的音乐。

原本是使用playsound播放音乐，但是在异步模式下会导致内存泄漏，所以使用了pygame做音乐播放。
