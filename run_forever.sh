#!/bin/bash

while :
do
    streamlit run front_end.py --server.port 8080 --server.enableCORS false
    sleep 1
done