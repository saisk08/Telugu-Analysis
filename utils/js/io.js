const fs = require('fs');
const path = require('path');

function jsonReader(dir) {
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
    } else files.push(jsonReader(filepath));
  });
  return files;
}

function jsonWriter(filepath, data) {
  const stringData = JSON.stringify(data);
  fs.mkdirSync(path.dirname(filepath), { recursive: true });
  fs.writeFileSync(filepath, stringData);
}

module.exports = { jsonReader, jsonWriter };
