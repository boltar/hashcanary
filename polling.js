var SmartPlugPowerMonitor = require("../../index.js");

var smartPlugPowerMonitor = new SmartPlugPowerMonitor({
  smartPlugIP: "192.168.1.136", // downstairs
  // smartPlugIP: "192.168.1.149", // desktop
  iftttMakerChannelKey: "<ifftt custom key>",
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

function pollingData(usage){
  console.log(usage.power);
}

function eventData(event, data){
  console.log(event, data);
}

// auto turn on at start
console.log("auto turn on...");
smartPlugPowerMonitor.smartPlug.setPowerState(1)
smartPlugPowerMonitor.start();
