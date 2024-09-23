#! /bin/bash

FILE_PATH=hosts.ini
counter=0
for i in $(grep 'ansible_host=' $FILE_PATH | awk '{print $2}' | cut -d'=' -f2)
do
    counter=$((counter+1))
    $(ssh $i -l user)
done
echo $counter