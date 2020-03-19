const pairs = require('./pairs.js');

function aggregate(files) {
  const combinedData = {};

  files.forEach(arr => {
    const userInfo = arr.shift();
    const data = [
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
    ];
    const set = [
      ...arr[0].content.set,
      ...arr[2].content.set,
      ...arr[3].content.set,
      ...arr[4].content.set,
      ...arr[5].content.set,
      ...arr[6].content.set,
      ...arr[7].content.set,
      ...arr[8].content.set,
      ...arr[9].content.set,
      ...arr[1].content.set,
    ];
    combinedData[userInfo.content.user] = { data, set };
    return combinedData;
  });
}

module.exports = { aggregate };
