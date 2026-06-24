## Network Protocols: Auditing and Securing

### exercice 2-harden.sh

- `find /`  
  procura em todo o sistema a partir da raiz `/`

- `-xdev`  
  não atravessa outras partições/mounts

- `-type d`  
  procura apenas diretórios

- `-perm 0002`  
  encontra ficheiros com permissão de escrita para others

- `-print`  
  mostra os resultados

- `-exec`  
  executa um comando nos resultados

- `chmod o-w`  
  remove permissão de escrita para others (`o`)

- `{}`  
  representa o item encontrado

- `+`  
  executa em lote (mais eficiente)
