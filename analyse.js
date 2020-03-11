const shuffleSeed = require('shuffle-seed');
const fs = require('fs');
const path = require('path');

const telugu = [
	'అ',
	'న',
	'వ',
	'మ',
	'య',
	'ల',
	'ర',
	'ఒ',
	'జ',
	'ఠ',
	'ఆ',
	'ఉ',
	'ఊ',
	'ఎ',
	'ఏ',
	'ప',
	'ఫ',
	'ద',
	'డ',
	'బ',
	'త',
	'క',
	'హ',
	'ణ',
	'ఘ',
];

const teluguPairs = telugu.flatMap((v, i) =>
	telugu.slice(i + 1).map(w => [v, w])
);

function readFilesSync(dir) {
	const files = [];

	fs.readdirSync(dir).forEach(filename => {
		const name = path.parse(filename).name;
		const ext = path.parse(filename).ext;
		const filepath = path.resolve(dir, filename);
		const stat = fs.statSync(filepath);
		const isFile = stat.isFile();
		// console.log(name, filepath);
		if (isFile) {
			const content = require(filepath);
			files.push({ filepath, name, ext, content });
		} else files.push(readFilesSync(filepath));
	});
	files.sort((a, b) => {
		if (!(a & b)) return 0;
		return a.name.localeCompare(b.name, undefined, {
			numeric: true,
			sensitivity: 'base',
		});
	});

	return files;
}

const files = readFilesSync('Results');
console.log(files[0]);
