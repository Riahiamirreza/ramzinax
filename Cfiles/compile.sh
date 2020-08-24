#!/bin/sh

gcc message_to_byte.c -o secret.out
gcc byte_to_message.c -o read.out

