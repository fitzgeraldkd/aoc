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
  };
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
  switch (parseInt(packet.type, 2)) {
    case 0:
      return packet.contents.reduce((prev, sub) => prev + calculateValue(sub), 0);
    case 1:
      return packet.contents.reduce((prev, sub) => prev * calculateValue(sub), 1);
    case 2:
      return Math.min(...packet.contents.map(sub => calculateValue(sub)));
    case 3:
      return Math.max(...packet.contents.map(sub => calculateValue(sub)));
    case 4:
      return parseInt(packet.contents, 2);
    case 5:
      return (calculateValue(packet.contents[0]) > calculateValue(packet.contents[1])) ? 1 : 0;
    case 6:
      return (calculateValue(packet.contents[0]) < calculateValue(packet.contents[1])) ? 1 : 0;
    case 7:
      return (calculateValue(packet.contents[0]) === calculateValue(packet.contents[1])) ? 1 : 0;
  }
}

const part1 = (path) => {
  const inputs = processInputs(path);
  const packet = inputs.map(value => hex2dec[value]).join('');
  const processed = processPacket(packet);
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
  let results = calculateValue(processed);
  return results;
};

// console.log(part1());
// console.log(part2());

export { part1, part2 };