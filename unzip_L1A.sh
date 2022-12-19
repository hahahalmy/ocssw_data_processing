#!/bin/bash

thread=20

find . -name "*.bz2" | parallel --j $thread bzip2 -d -k
