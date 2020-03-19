// To pre-process the data and output a combined file which has all the values in an agreed upon order

// read the files
// aggregate the data into a single json file
// write the aggregated in file
const { readFilesSync } = require('./utils/js/io');
const { aggregate } = require('./utils/js/aggregate');

const files = readFilesSync('Results');
aggregate(files);
