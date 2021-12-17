import fs from 'fs';

const processInputs = (path="inputs.txt") => {
  return fs
    .readFileSync(path, "utf8")
    .split("")
    // .map(item => parseInt(item, 10));
    // .map(item => item.trim());
};

const hex2dec = {
  '0': '0000',
  '1': '0001',
  '2': '0010',
  '3': '0011',
  '4': '0100',
  '5': '0101',
  '6': '0110',
  '7': '0111',
  '8': '1000',
  '9': '1001',
  'A': '1010',
  'B': '1011',
  'C': '1100',
  'D': '1101',
  'E': '1110',
  'F': '1111',
}

const dec2hex = {
  '0000': '0',
  '0001': '1',
  '0010': '2',
  '0011': '3',
  '0100': '4',
  '0101': '5',
  '0110': '6',
  '0111': '7',
  '1000': '8',
  '1001': '9',
  '1010': 'A',
  '1011': 'B',
  '1100': 'C',
  '1101': 'D',
  '1110': 'E',
  '1111': 'F'
};

const processLiteral = body => {
  const groups = [];
  let i;
  for (i=0; i<body.length; i+=5) {
    const newGroup = body.slice(i, i+5)
    groups.push(newGroup);
    if (newGroup[0] === '0') break;
  }
  return {
    value: groups.map(value => value.slice(1)).join(''),
    length: i+5+6
  }
}

const processPacket = (packet) => {
  const version = packet.slice(0, 3);
  const type = packet.slice(3, 6);
  let length;
  let data;
  if (type === '100') {
    const literal = processLiteral(packet.slice(6));
    data = literal.value
    length = literal.length;
    // packets.push({version: version, type: type, value: data.value})
  } else {
    const lengthType = packet.slice(6, 7);
    data = [];
    let currentLength = 0;
    if (lengthType === '0') {
      length = parseInt(packet.slice(7, 22), 2);
      while (currentLength < length) {
        const subpacket = processPacket(packet.slice(22+currentLength));
        data.push(subpacket);
        currentLength += subpacket.length;
      }
      length += 22;
      // packets.push({version: version, type: type, lengthType: lengthType})
    } else {
      let i = 18;
      const count = parseInt(packet.slice(7, 18), 2);
      while (data.length < count) {
        const subpacket = processPacket(packet.slice(18+currentLength));
        data.push(subpacket);
        currentLength += subpacket.length;
      }
      length = currentLength + 18;
    }
  }
  return {version: version, type: type, length: length, contents: data};
};

const calculateValue = packet => {
  console.log(packet);
  let value;
  switch (parseInt(packet.type, 2)) {
    case 0:
      console.log('sum');
      value = packet.contents.reduce((prev, sub) => prev + calculateValue(sub), 0);
      break;
    case 1:
      console.log('product');
      value = packet.contents.reduce((prev, sub) => prev * calculateValue(sub), 1);
      break;
    case 2:
      console.log('minimum');
      // const subpackets = packet.contents;
      // console.log(subpackets);
      // console.log(subpackets.map(sub => calculateValue(sub)))
      value = Math.min(...packet.contents.map(sub => calculateValue(sub)));
      break;
    case 3:
      console.log('maximum');
      value = Math.max(...packet.contents.map(sub => calculateValue(sub)));
      break;
    case 4:
      value = parseInt(packet.contents, 2);
      break;
    case 5:
      console.log('greater than');
      value = (calculateValue(packet.contents[0]) > calculateValue(packet.contents[1])) ? 1 : 0;
      break;
    case 6:
      console.log('less than');
      value = (calculateValue(packet.contents[0]) < calculateValue(packet.contents[1])) ? 1 : 0;
      break;
    case 7:
      console.log('greater than');
      value = (calculateValue(packet.contents[0]) === calculateValue(packet.contents[1])) ? 1 : 0;
      break;
  }
  return value;
}

const part1 = (path) => {
  const inputs = processInputs(path);
  const packet = inputs.map(value => hex2dec[value]).join('');
  console.log(packet);
  const processed = processPacket(packet);
  console.log(JSON.stringify(processed))
  let versionSum = 0;
  const queue = [processed];
  while (queue.length > 0) {
    const thisPacket = queue.pop();
    versionSum += parseInt(thisPacket.version, 2);
    if (Array.isArray(thisPacket.contents)) {
      queue.push(...thisPacket.contents);
    }
  }
  return versionSum
};

const part2 = (path) => {
  const inputs = processInputs(path);
  const packet = inputs.map(value => hex2dec[value]).join('');
  const processed = processPacket(packet);
  console.log(JSON.stringify(processed))
  let results = calculateValue(processed);
  return results;
};

console.log('\n\n\n\n\n\n\n\n\n\n\n')
// console.log(part1());
console.log(part2());

export { part1, part2 };