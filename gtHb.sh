#!/bin/bash
# declare 
git config user.email "yvanesc"
git add --all
git status
echo "------------------------------"
echo "Comments to add for the commit"
read cmt
echo "$cmt"
git config user.name "yvanesc"
git commit -am "$cmt"
git push -u origin master
