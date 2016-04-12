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
