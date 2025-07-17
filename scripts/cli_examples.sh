#!/bin/bash
echo "hello world" | tinty "l.*" yellow
echo "hello world" | tinty "(ll).*(ld)" red,bg_blue blue,bg_red
