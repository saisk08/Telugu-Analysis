/* eslint-disable no-console */
// To pre-process the data and output a combined file which has all the values in an agreed upon order
const chalk = require('chalk');
const spwan = require('child_process').spawn;
const { jsonReader, jsonWriter } = require('./utils/js/io');
const { aggregate } = require('./utils/js/aggregate');

const info = chalk.hex('#0074D9').bold;
const success = chalk.hex('#2EcC40').bold;
// Read the files
console.log(`${info('[INFO]:')} Reading files`);
const files = jsonReader('Results');
console.log(`${success('[DONE]:')} Files read`);

// Aggregate the data into a single json file
console.log(`${info('[INFO]:')} Aggregating data...`);
const data = aggregate(files);
console.log(`${success('[DONE]:')} Aggregation done`);

// Write the aggregated in file
console.log(`${info('[INFO]:')} Writing to file`);
jsonWriter('data.json', data);
console.log(`${success('[DONE]:')} Data written`);

// Run the python script
console.log(`${info('[INFO]:')} Run python analysis script`);
spwan('python', 'main.py');
console.log(`${success('[DONE]:')} Profiles created and analysis updated`);
