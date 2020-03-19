// To pre-process the data and output a combined file which has all the values in an agreed upon order

const { jsonReader, jsonWriter } = require('./utils/js/io');
const { aggregate } = require('./utils/js/aggregate');

// Read the files
const files = jsonReader('Results');
// Aggregate the data into a single json file
const data = aggregate(files);
// Write the aggregated in file
jsonWriter('Combined/data.json', data);
