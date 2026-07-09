#!/usr/bin/env python3
"Checks whether a TCP port is open on a given host."

import socket


def check_port(host, port):
    "
    Check if a TCP port is open.

    Args:
        host (str): Hostname or IP address.
        port (int): Port number.

    Returns:
        bool: True if the port is open, False otherwise.
    "
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(2)
            result = sock.connect_ex((host, port))
            return result == 0
    except Exception:
        return False
