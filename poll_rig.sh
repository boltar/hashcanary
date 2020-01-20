#!/bin/bash
set +x
cd /home/pi/smart-plug-power-monitor/examples/simple

sudo node downstairs.js > /home/pi/poll_pipe &
sleep infinity < /home/pi/poll_pipe &

