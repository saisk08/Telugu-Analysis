const shuffleSeed = require('shuffle-seed');
const shortid = require('shortid');
const fs = require('fs');

shortid.characters(
  '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_$'
);

function aggregate(files, version1 = false) {
  const combinedData = {};
  const mapping = {};

  files.forEach(arr => {
    // Combine data
    let userInfo = null;
    // Becasue of the order in which the files are placed in the array
    if (arr[0].name.endsWith('-info')) userInfo = arr.shift();
    else userInfo = arr.pop();
    const temp = userInfo.name.slice(0, -5);
    const id = version1 ? shortid.generate() : temp;
    mapping[temp] = id;
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
    if (version1) combinedData[id] = { data, userInfo };
  });
  fs.writeFileSync('map.json', mapping);
  return combinedData;
}

module.exports = { aggregate };
