#!/bin/bash

openssl pkeyutl -decrypt -in cipher1.bin -inkey privatekey1.pem -out dmessage1.txt
openssl pkeyutl -decrypt -in cipher2.bin -inkey privatekey2.pem -out dmessage2.txt

echo Saved as dmessage1.txt and dmessage2.txt
