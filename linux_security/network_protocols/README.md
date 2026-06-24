# Network Protocols: Auditing and Securing


exercice 2-harden.sh

find /          -> find in all the system, begining at the filesystem root /
-xdev           -> do not pass to other mount / partitions 
-type d         -> find directorys
-perm 0002      -> permission bit write in others | special | owner | group | others |
-print          -> prints find item {}
-exec           -> keeps find's results and tell to execute some thing
-chmod o-w      -> dont allow others to write o = others -w = remove write
{} +            -> {} item finded -> + execute in batch
