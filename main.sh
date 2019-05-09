#!/bin/sh
cd "$(/home/superior/Documents/repos/twilioScript "$0")";
CWD="$(pwd)"
echo $CWD
python send_sms.py