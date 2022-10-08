import fs from 'fs';
import { parse } from 'path';

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
}

const getType4Body = (body, data) => {
  const groups = [];
  for (let i=0; i<body.length; i+=5) {
    const newGroup = body.slice(i, i+5)
    groups.push(newGroup);
    if (newGroup[0] === '0') break;
  }
  return groups.map(value => value.slice(1)).join('')
}

const getOtherBody = (body, data) => {
  console.log('Getting Other Body:', body)
  const lengthTypeId = body[0];
  if (lengthTypeId === '0') {
    // console.log('test')
    const totalLength = body.slice(1, 16);
    const subBody = body.slice(16);
    const dividingIndex = determineEnd(subBody);
    console.log('Sub Body', subBody, 'Body', body)
    const endIndex = determineEnd(subBody.slice(dividingIndex))
    const subpacketA = subBody.slice(0, dividingIndex);
    const subpacketB = subBody.slice(dividingIndex, dividingIndex + endIndex);
    data.queue.push(subpacketA, subpacketB);
    const packets = [subpacketA, subpacketB]
    return { lengthTypeId, totalLength, packets }
  } else {
    // number of sub-packets
    const packetCount = body.slice(1, 12);
    const subBody = body.slice(12);
    let thisStart = 0
    const packets = [];
    while (packets.length < parseInt(packetCount, 2)) {
      const newStart = determineEnd(subBody.slice(thisStart))
      // console.log(thisStart, thisStart + newStart);
      packets.push(subBody.slice(thisStart, thisStart + newStart))
      thisStart += newStart;
    }
    // console.log(packets)
    data.queue.push(...packets)
    return { lengthTypeId, packetCount, packets };
    for (let i=0; i<parseInt(packetCount, 2); i++) {
      packets.push(body.slice(12+11*i, 12+11*(i+1)))
    }
    return { lengthTypeId, packetCount, packets }
  }
};

const determineEnd = body => {
  if (body.length === 0 ) {
    console.log('error');
    return null;
  }
  console.log(body.length)
  const packetVersion = body.slice(0, 3);
  const packetTypeId = body.slice(3, 6);
  console.log('   Determing End:', body, '\n   Version:', packetVersion, '\n   Type ID:', packetTypeId)
  if (packetTypeId === '100') {
    let i = 6;
    while (body[i] !== '0') {
      // console.log('here')
      i += 5;
    }
    return i + 5;
  } else {
    const lengthTypeId = body.slice(6, 7);
    const subBody = body.slice(7);
    console.log('     Length Type ID:', lengthTypeId, '\n     Sub Body:', subBody)
    if (lengthTypeId === '0') {
      console.log('nonrecursive', subBody.slice(0, 15), 7 + parseInt(subBody.slice(0, 15), 2))
      return 7 + parseInt(subBody.slice(0, 15), 2);
    } else {
      console.log('recursive', determineEnd(subBody))
      return determineEnd(subBody);
    }
  }
}

const processPackets = data => {
  while (data.queue.length > 0) {
    // console.log(data.queue);
    const packet = data.queue.pop();
    const version = packet.slice(0, 3);
    const typeId = packet.slice(3, 6);
    const body = packet.slice(6);
    const parsedBody = typeId === '100' ? getType4Body(body, data) : getOtherBody(body, data);
    console.log('This Packet', packet, '\nVersion', version, '\nType ID', typeId, '\nBody', body, '\nParsed Body', parsedBody, '\n');
    data.packets.push({version, typeId, parsedBody})
  }
  return data;
}

const part1 = (path) => {
  const inputs = processInputs(path);
  // console.log(inputs);
  // console.log(inputs.map(value => hex2dec[value]).join(''))
  const packet = inputs.map(value => hex2dec[value]).join('')
  console.log(packet);
  return processPackets({packets: [], queue: [packet]})
  // // const header = packet.slice(0, 6);
  // // const body = packet.slice(6);
  // // console.log(packet)
  // // console.log(header, body)
  // // console.log(splitPacket(packet))
  // const packets = [];
  // // packets.push(splitPacket(packet));
  // let totalVersion = 0;
  // const queue = [packet];
  // while (queue.length > 0) {
  //   // console.log('queue:',queue);
  //   const thisPacket = queue.pop();
  //   packets.push(thisPacket);
  //   const parsedPacket = splitPacket(thisPacket);
  //   totalVersion += parseInt(parsedPacket.version, 2);
  //   // console.log(parsedPacket);
  //   if ('parsedBody' in parsedPacket && 'packets' in parsedPacket.parsedBody) {
  //     // console.log('test');
  //     queue.push(...parsedPacket.parsedBody.packets);

  //   }
  // }
  // console.log(packets);
  // return totalVersion

};

const part2 = (path) => {
  const inputs = processInputs(path);

};

console.log('\n\n\n\n\n\n\n\n\n\n\n')
console.log(part1());
console.log(part2());

export { part1, part2 };