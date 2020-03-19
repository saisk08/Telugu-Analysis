const shuffleSeed = require('shuffle-seed');
const pairs = require('./pairs');

function aggregate(files) {
  const combinedData = {};

  files.forEach(arr => {
    // Combine data
    const userInfo = arr.shift();

    const data = shuffleSeed.unshuffle(
      [
        ...arr[0].content.data,
        ...arr[2].content.data,
        ...arr[3].content.data,
        ...arr[4].content.data,
        ...arr[5].content.data,
        ...arr[6].content.data,
        ...arr[7].content.data,
        ...arr[8].content.data,
        ...arr[9].content.data,
        ...arr[1].content.data,
      ],
      userInfo.content.user
    );
    combinedData[userInfo.content.user] = { data, userInfo };
  });
  combinedData.pairs = pairs;
  return combinedData;
}

module.exports = { aggregate };
