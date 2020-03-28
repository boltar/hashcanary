#!/bin/bash
set +x
cd /home/pi/hashcanary/examples/simple

if [[ -z "${p_color}" ]]; then
  p_color="blue"
fi

sudo  p_color=$p_color node downstairs.js > /home/pi/poll_pipe &
sleep infinity < /home/pi/poll_pipe &
