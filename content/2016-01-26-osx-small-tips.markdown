Title: osx small tips
Date: 2016-01-26 18:03
Tags: osx
Category: tech

### Encrypt / Decrypt file
```
# brew install gpg
# gpg -c file.txt          // encrypt
# gpg file.txt.gpg         // decrypt
```

### Reset the DNS cache
```
sudo killall -HUP mDNSResponder
```

### Copy file path to clipboard
In `Finder`, after right click the file, hold `Alt`, `copy as path option` will appear.


### Go to file/path in file selector
Click `Command + Shift + G` will trigger the `Go to` dialog.

### Screen capture
`cmd+shift+3`: Full screen

`cmd+shift+4`: Selected area

[参考链接][1]

### Mount NTFS manually
编辑 `/etc/fstab`, 可以用 Label 或者 UUID。UUID 可以通过 `diskutil info /Volumes/Data` 来得到。
```
LABEL=Data none ntfs rw,auto,nobrowse
UUID=731EE82C-92D2-4A83-A44F-29120B67C7B1 none ntfs rw,auto,nobrowse
```
保存后，弹出USB，然后重新插拔。注意，这时 Finder 里面不会再看到这些分区，需要从 Terminal 中打开。
```
cd /Volumes
open -a Finder ./
```

[1]: https://www.zhihu.com/question/19550327
