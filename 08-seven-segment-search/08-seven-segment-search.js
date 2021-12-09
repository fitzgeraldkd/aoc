const fs = require('fs');
const inputs = fs
  .readFileSync("inputs.txt", "utf8")
  .split("\n")
  .map(item => item.split(' | ').map(node => node.split(' ')));
  // .map(item => item.split(' '));
  // .map(item => item.trim());

console.log(inputs);

// const part1 = (inputs) => {
//   let sum = 0;

//   for (const input of inputs) {
//     for (const digit of input[1]) {
//       console.log(digit);
//       if ([2, 3, 4, 7].includes(digit.length)) sum++
//     }
//   }
//   return sum;
// };

// const results1 = part1(inputs);

// console.log(results1);

const NUMBERS = {
  0: ['top', 'tleft', 'tright', 'bleft', 'bright', 'bottom'],
  1: ['tright', 'bright'],
  2: ['top', 'tright', 'middle', 'bleft', 'bottom'],
  3: ['top', 'tright', 'middle', 'bright', 'bottom'],
  4: ['tleft', 'tright', 'middle', 'bright'],
  5: ['top', 'tleft', 'middle', 'bright', 'bottom'],
  6: ['top', 'tleft', 'middle', 'bleft', 'bright', 'bottom'],
  7: ['top', 'tright', 'bright'],
  8: ['top', 'tleft', 'tright', 'middle', 'bleft', 'bright', 'bottom'],
  9: ['top', 'tleft', 'tright', 'middle', 'bright', 'bottom']
};

const part2 = (inputs) => {
  let sum = 0;

  for (const input of inputs) {
    const lines = {
      a: ['top', 'tleft', 'tright', 'middle', 'bleft', 'bright', 'bottom'],
      b: ['top', 'tleft', 'tright', 'middle', 'bleft', 'bright', 'bottom'],
      c: ['top', 'tleft', 'tright', 'middle', 'bleft', 'bright', 'bottom'],
      d: ['top', 'tleft', 'tright', 'middle', 'bleft', 'bright', 'bottom'],
      e: ['top', 'tleft', 'tright', 'middle', 'bleft', 'bright', 'bottom'],
      f: ['top', 'tleft', 'tright', 'middle', 'bleft', 'bright', 'bottom'],
      g: ['top', 'tleft', 'tright', 'middle', 'bleft', 'bright', 'bottom'],
    };

    const exclusions = {
      0: [],
      1: [],
      2: [],
      3: [],
      4: [],
      5: [],
      6: [],
      7: [],
      8: [],
      9: []
    }

    const values ={};
    for (const digit of [...input[0], ...input[1]]) {
      console.log(digit);

      if (digit.length === 2) {
        values[digit.split('').sort().join('')] = 1;
        [2, 5, 6].forEach(num => exclusions[num].push(digit.split('')))
        // 1
        // digit.split('').forEach(char => {
          for (const char in lines) {
            if (digit.includes(char)) {
              lines[char] = lines[char].filter(pos => ['tright', 'bright'].includes(pos))
            } else {
              lines[char] = lines[char].filter(pos => !(['tright', 'bright'].includes(pos)))
            }
          }
        // });
      }
      
      if (digit.length === 3) {
        values[digit.split('').sort().join('')] = 7;
        // 7
        for (const char in lines) {
          if (digit.includes(char)) {
            lines[char] = lines[char].filter(pos => ['top', 'tright', 'bright'].includes(pos))
          } else {
            lines[char] = lines[char].filter(pos => !(['top', 'tright', 'bright'].includes(pos)))
          }
        }
      }
      
      if (digit.length === 4) {
        values[digit.split('').sort().join('')] = 4;
        // 4
        for (const char in lines) {
          if (digit.includes(char)) {
            lines[char] = lines[char].filter(pos => ['tleft', 'tright', 'middle', 'bright'].includes(pos))
          } else {
            lines[char] = lines[char].filter(pos => !(['tleft', 'tright', 'middle', 'bright'].includes(pos)))
          }
        }
      }

      if (digit.length === 6) {
        // 0, 6, 9
        values[digit.split('').sort().join('')] = [0, 6, 9];

        digit.split('').forEach(char => {
          // lines[char] = lines[char].filter(pos => ['top', 'tleft', 'bright', 'bottom'].includes(pos))
        });
      }

      if (digit.length === 5) {
        // 2, 3, 5
        values[digit.split('').sort().join('')] = [2, 3, 5];
        digit.split('').forEach(char => {
          // lines[char] = lines[char].filter(pos => ['top', 'middle', 'bottom'].includes(pos))
        });
      }

      if (digit.length === 7) {
        values[digit.split('').sort().join('')] = 8;
      }
    }
    // console.log(lines);
    // console.log(values);

    for (let i=0; i<5; i++) {
      let occurs = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0
      }
      console.log('iteration', i);
      console.log(values);
      for (const value in values) {
        if (!Array.isArray(values[value])) {
          occurs[values[value]] = 'complete'
          value.split('').forEach(pos => {
            lines[pos] = lines[pos].filter(thisPos => NUMBERS[values[value]].includes(thisPos))
          })
          // console.log(lines);
        }
        if (Array.isArray(values[value])) {
          if (values[value].length === 1) {
            values[value] = values[value][0];
            occurs[values[value]] = 'complete'
            if (value === 'abcdg') console.log('setting', values[value][0])
          } else {
            values[value] = values[value].filter(digit => {
              if (occurs[digit] === 'complete') return false;
              if (occurs[digit] === 0) {occurs[digit] = value}
              else {occurs[digit] = 'multi'}
              for (const exSet of exclusions[digit]) {
                if (exSet.every(num => value.includes(num))) return false;
              }
              const letters = value.split('');
              // console.log(value);
              const positions = [];
              for (const letter of letters) {
                positions.push(...lines[letter])
                // console.log(letter, lines[letter]);
                // console.log(digit, NUMBERS[digit])
                // if (!lines[letter].some(line => NUMBERS[digit].includes(line))) return false;
              }
              // return true;
              // console.log(NUMBERS[digit])
              // console.log(positions)
              return NUMBERS[digit].every(line => positions.includes(line))
            })
          }
        }
      }
      for (const occur in occurs) {
        if (![0, 'multi', 'complete'].includes(occurs[occur])) {
          values[occurs[occur]] = parseInt(occur)
        }
      }
    }
    console.log(values);


    // console.log(input[1])

    const thisOutput = [];
    for (const outputDigit of input[1]) {
      // console.log(outputDigit);
      thisOutput.push(values[outputDigit.split('').sort().join('')])
    }
    sum += parseInt(thisOutput.join(''));
    // console.log(thisOutput);
    // console.log(sum);

  }
  return sum;
};

const results2 = part2(inputs);

console.log(results2);