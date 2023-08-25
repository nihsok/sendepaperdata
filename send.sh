#!/bin/bash
python3 ~/sendepaperdata/img2grayfb.py tmp.png
timeout 2 curl -X POST  -H "Content-Type: application/octet-stream" --data-binary @tmp.buf http://192.168.10.108
