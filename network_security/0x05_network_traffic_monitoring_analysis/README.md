# Network Traffic Monitoring & Analysis



## Flag 03

at Wireshark filter ```tcp``` to watch only the packets

```Packets: 7, Displayed: 7```


### how many initial SYN are

tcp.flags.syn == 1 && tcp.flags.ack == 0

packets 7, ```Displayed 1```

### How many SYS + ACK  exist

tcp.flags.syn == 1 && tcp.flags.ack == 1

Displayed : 1

SYN (without ACK) = 1
SYN+ACK = 1
Total de pacotes no stream = 7

## FIN

Displayed : 2

### Find destination port

tcp.flags.syn == 1 && tcp.flags.ack == 0 -> expand transmission control protocol

DST port: 8080


## Flag 04

filters: ftp or tcp.port == 21

double click, find PASS

## Flag 05

-> follow ->TCP stream

important: missing bytes

calculate the message

