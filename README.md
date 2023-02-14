# Size_file
Finding file by Size

```bash
 find / -type f -size +700M -exec ls -lh {} \; 2> /dev/null | awk '{ print $NF ": " $5 }' | sort -nk 2,2
 ```
