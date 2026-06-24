## Network Protocols: Auditing and Securing

### exercice 2-harden.sh

- `find /`  
  searches the entire system starting from the root directory `/`

- `-xdev`  
  does not cross other filesystems or mounted partitions

- `-type d`  
  searches only directories

- `-perm 0002`  
  finds files with write permission for others

- `-print`  
  prints the results

- `-exec`  
  executes a command on the found results

- `chmod o-w`  
  removes write permission for others (`o`)

- `{}`  
  represents the currently found item

- `+`  
  executes commands in batch (more efficient)
