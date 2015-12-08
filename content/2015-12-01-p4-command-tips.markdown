Title: p4 command line tips
Date: 2015-12-01 19:50
Tags: p4
Category: tech

#### Remove files from changelist without removing the edits
```
# p4 revert -k -c changelist path_to_file
```

#### Diff unopened local file against depot file
```
# p4 diff -f path_to_file
```

