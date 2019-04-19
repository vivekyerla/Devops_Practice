#!/bin/bash

#This Script will ping list of servers and list the status

SERVER_FILE="/opt/servers"

if [[ ! -e "${SERVER_FILE}" ]]
then
  echo "Can not Open ${SERVER_FILE}." >&2
  exit 1
fi

for SERVER in $(cat ${SERVER_FILE})
do
  echo "Pinging ${SERVER}"
  ping -c 1 ${SERVER} &> /dev/null
  if [[ "${?}" -ne 0 ]]
  then 
    echo "${SERVER} is down."
  else
    echo "${SERVER} up"
  fi
done  

