const fs = require('fs');
const path = require('path');

function readFilesSync(dir) {
  const files = [];

  fs.readdirSync(dir).forEach(filename => {
    const { name } = path.parse(filename);
    const { ext } = path.parse(filename);
    const filepath = path.resolve(dir, filename);
    const stat = fs.statSync(filepath);
    const isFile = stat.isFile();
    if (isFile) {
      const content = JSON.parse(fs.readFileSync(filepath));
      files.push({ filepath, name, ext, content });
    } else files.push(readFilesSync(filepath));
  });
  return files;
}

module.exports = { readFilesSync };
