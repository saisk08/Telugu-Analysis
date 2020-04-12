/* eslint-disable no-console */
// To pre-process the data and output a combined file which has all the values in an agreed upon order
const chalk = require('chalk');
// const spwan = require('child_process').spawn;
const { jsonReader, jsonWriter } = require('./utils/js/io');
const { aggregate } = require('./utils/js/aggregate');

const info = chalk.hex('#0074D9').bold;
const success = chalk.hex('#2EcC40').bold;
// Read the files
console.log(`${info('[INFO]:')} Reading files`);
const ver1Files = jsonReader('expData/ver1');
const ver2Files = jsonReader('expData/ver2');
console.log(`${success('[DONE]:')} Files read`);

// Aggregate the data into a single json file
console.log(`${info('[INFO]:')} Aggregating data...`);
const ver1Data = aggregate(ver1Files);
const ver2Data = aggregate(ver2Files);
console.log(`${success('[DONE]:')} Aggregation done`);

// Write the aggregated in file
console.log(`${info('[INFO]:')} Writing to file`);
jsonWriter('ver1.json', ver1Data);
jsonWriter('ver2.json', ver2Data);
console.log(`${success('[DONE]:')} Data written`);
