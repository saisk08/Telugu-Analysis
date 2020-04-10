const shuffleSeed = require('shuffle-seed');
const shortid = require('shortid');

shortid.characters(
  '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'
);

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
    combinedData[shortid.generate()] = { data, userInfo };
  });
  return combinedData;
}

module.exports = { aggregate };
