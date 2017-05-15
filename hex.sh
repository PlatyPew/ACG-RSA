#!/bin/bash

echo ---------- Public key 1 ----------
openssl rsa -pubin -text -noout -in publickey1.pem
echo
echo ---------- Public key 2 ----------
openssl rsa -pubin -text -noout -in publickey2.pem
