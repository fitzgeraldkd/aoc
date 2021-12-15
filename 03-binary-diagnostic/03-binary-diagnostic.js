import fs from 'fs';

const processInputs = (path="inputs.txt") => {
  return fs
    .readFileSync(path, "utf8")
    .split("\n");
};

const countDigits = (inputs, atIndex) => {
  return inputs.reduce((digits, item) => {
    for (let i=(atIndex ? atIndex : 0); i < (atIndex ? atIndex+1 : item.length); i++) {
      const index = atIndex ? 0 : i;
      if (digits[index] !== undefined) {
        if (item[i] === '1') digits[index]++
        else digits[index]--
      } else digits[index] = item[i] === '1' ? 1 : -1;
    }
    return digits;
  }, []);
};

const part1 = (path) => {
  const inputs = processInputs(path);
  const digitCount = countDigits(inputs);
  const gamma = parseInt(digitCount.map(count => count > 0 ? 1 : 0).join(''), 2);
  const epsilon = parseInt(digitCount.map(count => count < 0 ? 1 : 0).join(''), 2);
  return gamma * epsilon;
};

const part2 = (path) => {
  const inputs = processInputs(path);
  let oxygen = [...inputs];
  let carbonDiox = [...inputs];

  let i = 0;
  while (oxygen.length > 1) {
    const oneMoreCommon = countDigits(oxygen, i)[0] >= 0;
    oxygen = oxygen.filter(value => value[i] === (oneMoreCommon ? '1' : '0'));
    i++;
  }

  i = 0;
  while (carbonDiox.length > 1) {
    const oneMoreCommon = countDigits(carbonDiox, i)[0] >= 0;
    carbonDiox = carbonDiox.filter(value => value[i] === (oneMoreCommon ? '0' : '1'));
    i++;
  }
  
  return parseInt(oxygen[0], 2) * parseInt(carbonDiox[0], 2);
};

export { part1, part2 };