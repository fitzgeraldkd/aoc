import fs from 'fs';
import { parse } from 'path';

const processInputs = (path="inputs.txt") => {
  return fs
    .readFileSync(path, "utf8")
    .split("\n\n")
    .map(scanner => scanner.split('\n').slice(1).map(coords => JSON.parse(`[${coords}]`)))
    // .map(item => parseInt(item, 10));
    // .map(item => item.trim());
};

const rotations = [
  [3, 1, 2],
  [3, 2, 1],
  [1, 3, 2],
  [1, 2, 3],
  [2, 3, 1],
  [2, 1, 3],

  [-3, 1, 2],
  [-3, 2, 1],
  [1, -3, 2],
  [1, 2, -3],
  [2, -3, 1],
  [2, 1, -3],
]

const getDifference = (position1, position2) => {
  return position1.map((value, index) => value - position2[index]);
};

const rotateByAxis = ((scanner, axis) => {
  const swapped = {
    0: axis === 0 ? 0 : (axis === 1 ? 2 : 1),
    1: axis === 1 ? 1 : (axis === 2 ? 0 : 2),
    2: axis === 2 ? 2 : (axis === 0 ? 1 : 0),
  }
  const inverted = {
    0: axis === 1 ? -1 : 1,
    1: axis === 2 ? -1 : 1,
    2: axis === 0 ? -1 : 1
  }
  return scanner.map(coords => (
    [
      coords[swapped[0]] * inverted[0],
      coords[swapped[1]] * inverted[1],
      coords[swapped[2]] * inverted[2]
    ]
  ));
});

const alignScanner = ((scanner, difference) => {
  return scanner.map(coords => coords.map((coord, index) => coord + difference[index]));
});

const countAligned = ((scanner1, scanner2) => {
  const scanner2strings = scanner2.map(coord2 => coord2.toString());
  return scanner1.map(coord => coord.toString()).reduce((prev, coord) => (
    scanner2strings.includes(coord) ? prev + 1 : prev
  ), 0);
});

const checkOverlap = ((scanner1, scanner2) => {
  // console.log('Scan1', scanner1)
  // console.log('Scan2', scanner2)
  for (let i=0; i<scanner1.length; i++) {
    for (let j=0; j<scanner2.length; j++) {
      const difference = getDifference(scanner1[i], scanner2[j]);
      const scanner2aligned = alignScanner(scanner2, difference);
      // console.log('test')
      // console.log(scanner1);
      // console.log(scanner2);
      // console.log(scanner2aligned);
      const numberAligned = countAligned(scanner1, scanner2aligned)
      if (numberAligned >= 12) {
        offsets.push(difference);
        return scanner2aligned;
      }
      
    }
  }
  return false;
});

const mirror = (scanner => {
  return scanner.map(coords => [-1 * coords[0], coords[1], coords[2]]);
})

const iterateRotationsAndCheck = ((scanner1, scanner2) => {
  // // console.log('000211102221000211102221'.split('').map(val => parseInt(val, 10)))
  // for (let i=0; i<2; i++) {
  //   '000211102221000211102221'.split('').map(val => parseInt(val, 10)).forEach(axis => {
  //     // console.log(scanner2[0])
  //     scanner2 = rotateByAxis(scanner2, axis)
  //     const aligned = checkOverlap(scanner1, scanner2);
  //     // console.log(scanner2);
  //     if (aligned) return aligned;
  //   });
  //   scanner2 = mirror(scanner2);
  // }
  for (let x=0; x<4; x++) {
    scanner2 = rotateByAxis(scanner2, 0);
    for (let y=0; y<4; y++) {
      scanner2 = rotateByAxis(scanner2, 1);
      for (let z=0; z<4; z++) {
        scanner2 = rotateByAxis(scanner2, 2);
        const aligned = checkOverlap(scanner1, scanner2);
        if (aligned) return aligned;
      }
    }
  }
  return false;
});

const offsets = [[0, 0, 0]];

const part1 = (path) => {
  const inputs = processInputs(path);
  const scanners = [[0, 0, 0]];
  const unalignedScanners = [...inputs];
  const alignedScanners = [unalignedScanners.shift()]
  console.log(inputs[0]);
  console.log(iterateRotationsAndCheck(inputs[0], inputs[1]))
  let iterations = 0;
  while (unalignedScanners.length > 0) {
    console.log(unalignedScanners.length, 'scanners left.', iterations++, 'iterations.')
    const thisScanner = unalignedScanners.shift();
    let isAligned;
    for (const alignedScanner of alignedScanners) {
      isAligned = iterateRotationsAndCheck(alignedScanner, thisScanner);
      if (isAligned) break;
    }
    if (isAligned) {
      alignedScanners.push(isAligned);
    } else {
      unalignedScanners.push(thisScanner);
    }
  }

  const beacons = [];
  for (const scanner of alignedScanners) {
    scanner.map(beacon => beacon.toString()).forEach(beacon => {
      if (!beacons.includes(beacon)) beacons.push(beacon);
    })
  }
  console.log(JSON.stringify(offsets));
  return beacons.length;

};

const part2 = (path) => {
  const inputs = processInputs(path);
  // testing(inputs[0])


};

const testing = (scanner) => {
  console.log(scanner)
  let affectedScanner = scanner;
  console.log('000211102221000211102221'.split('').map(val => parseInt(val, 10)))
  '000211102221000211102221'.split('').map(val => parseInt(val, 10)).forEach(axis => {
    console.log(axis, affectedScanner[0], scanner[0]);
    affectedScanner = rotateByAxis(affectedScanner, axis);
    // const aligned = checkOverlap(scanner1, scanner2);
    // // console.log(scanner2);
    // if (aligned) return aligned;
    // scanner2 = rotateByAxis(scanner2, axis)
  })
}

// console.log(part1());
// console.log(part2());

export { part1, part2 };

const coords = '[[0,0,0],[-18,141,-1155],[81,7,-2326],[-1153,-7,-1203],[13,-1039,-2309],[1145,24,-1117],[-2350,13,-1042],[-1,-2358,-2359],[7,1338,-2337],[1250,1314,-1052],[2427,87,-1070],[-1142,-1165,-2379],[3707,53,-1210],[1145,56,-2313],[10,2434,-2398],[2348,-2,131],[2394,-17,-2349],[3649,55,-2266],[132,1356,-3524],[2453,-1116,-2255],[4848,149,-2297],[136,2391,-3592],[2360,-1078,-1085],[2487,1333,-2369],[3572,-1163,-1032],[2517,1315,-3437],[4889,-1109,-2256],[2409,-2260,-1156],[4865,-2233,-2389],[3704,-2335,-2423],[3708,-3524,-2317],[3660,-4772,-2280],[5959,-2355,-2423],[3725,-2249,-3543],[3694,-1148,-3517],[3604,-2420,-4688],[2420,-2243,-3456],[3586,-3566,-4640],[2531,-3467,-3556]]';

const calcManhattan = ((coords1, coords2) => {
  return Math.abs(coords1[0] - coords2[0]) + Math.abs(coords1[1] - coords2[1]) + Math.abs(coords1[2] - coords2[2])
});

const parsedCoords = JSON.parse(coords);
console.log(parsedCoords);
let maxDistance = 0;
for (let i=0; i<parsedCoords.length; i++) {
  for (let j=0; j<parsedCoords.length; j++) {
    const thisDistance = calcManhattan(parsedCoords[i], parsedCoords[j]);
    maxDistance = Math.max(maxDistance, thisDistance);
  }
}
console.log(maxDistance);