#!/usr/bin/env python
# -- coding: utf-8 --

from multiprocessing import Process
import socket
import time
import os


def wait_for_service(host: str, port: int, max_retries=60):
    """Wait for services."""
    if host or port:
        retry_number = 0
        while retry_number < max_retries:
            try:
                print("Trying to connect on {}:{} - {}/{}".format(host, port, retry_number, max_retries))
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(5)
                s.connect((host, port))
                print('Connected!')
                break
            except socket.error as e:
                retry_number += 1
                print(f"Error... Trying in 1 s ({e.message})")
                time.sleep(1)
                if retry_number >= max_retries:
                    print('Max number of retries has been reached. Aborting!')
                    raise
            finally:
                s.close()


def main():
    process_list = []
    services = os.getenv('WAIT_FOR', '').split(',')
    print(services)
    for service in services:
        host, port = service.split(':')
        process = Process(target=wait_for_service, args=(host, int(port)))
        process_list.append(process)
        process.start()
    for process in process_list:
        process.join()
    print("OK!")


main()
