#!/bin/bash

strval1=$(rc-service btrhgsd status | sed 's/*//g' | sed 's/://g')

if [ "$strval1" = "  status started" ]; then
    doas rc-service btrhgsd restart
fi

if [ "$strval1" = "  status stopped" ]; then
    doas rc-service btrhgsd start
fi