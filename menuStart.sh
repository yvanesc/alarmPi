#!/bin/bash
echo "select the operation ************  1)operation 1 2)operation 2 3)operation 3 4)operation 4 "

read n
case $n in
    1) echo "opn 1";;
    2) commands for opn 2;;
    3) commands for opn 3;;
    4) commands for  opn 4;;
    *) invalid option;;
esac