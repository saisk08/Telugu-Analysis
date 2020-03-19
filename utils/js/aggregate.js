const shuffleSeed = require('shuffle-seed');

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
    const set = shuffleSeed.unshuffle(
      [
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
      ],
      userInfo.content.user
    );
    combinedData[userInfo.content.user] = { data, set };
  });
  return combinedData;
}

module.exports = { aggregate };
