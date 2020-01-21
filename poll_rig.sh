#!/bin/bash
set +x
cd /home/pi/hashcanary/examples/simple

sudo node downstairs.js > /home/pi/poll_pipe &
sleep infinity < /home/pi/poll_pipe &

