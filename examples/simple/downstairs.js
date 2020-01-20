var SmartPlugPowerMonitor = require("../../index.js");
const fs = require('fs');
var prev_date = new Date(2000, 1, 1, 0, 0, 0);

var smartPlugPowerMonitor = new SmartPlugPowerMonitor({
   smartPlugIP: "192.168.1.136", // miner downstairs
  //smartPlugIP: "192.168.1.149", // desktop
  iftttMakerChannelKey: "<your_ifttt_key_here>",
  pollIntervalSeconds: 1,
  startTimeWindowSeconds: 3,
  endTimeWindowSeconds: 60*15, // 15 minutes
  startEventName: "rig started",
  endEventName: "rig down",
  pollingCallback: pollingData,
  wattsThreshold: 800,
  cooldownPeriodSeconds: 60,
  eventCallback: eventData
});

function check_new_day(usage) {
  curr_date = new Date(usage.timestamp);

  // if date or year (not very likely unless there was an exact jump of 365 or 366 days) is different, 
  // and the new time is newer
  return (curr_date.getDate() != prev_date.getDate() || curr_date.getYear() != prev_date.getYear()) && 
      curr_date > prev_date;
  
}

function write_log(usage) {

  fs.appendFile('power_usage.txt', curr_date.toLocaleString() + ' | ' + usage.power + '\n', (err) => {
    if (err) throw err;
    console.log('updated usage log');
  });

  prev_date = curr_date;

}

function pollingData(usage){
  
  if (check_new_day(usage)) {
    write_log(usage);
  }
  console.log(curr_date.toLocaleString() + " | " + usage.power);
  var spawn = require("child_process").spawn; 
      
  var process = spawn('python',["/home/pi/unicorn-hat/examples/equalizer.py", usage.power]);
}

function eventData(event, data){
  console.log(event, data);
}

// auto turn on at start
console.log("auto turn on...");
smartPlugPowerMonitor.smartPlug.setPowerState(1)
smartPlugPowerMonitor.start();
