import { part1 as day01part1, part2 as day01part2 } from './01-sonar-sweep/01-sonar-sweep.js';
import { part1 as day12part1, part2 as day12part2 } from './12-passage-pathing/12-passage-pathing.js';
import { part1 as day13part1, part2 as day13part2 } from './13-transparent-origami/13-transparent-origami.js';
import { part1 as day14part1, part2 as day14part2 } from './14-extended-polymerization/14-extended-polymerization.js';

const puzzles = [
  {
    day: 1,
    title: 'Sonar Sweep',
    inputs: './01-sonar-sweep/inputs.txt',
    parts: [
      {func: day01part1, solution: 1475},
      {func: day01part2, solution: 1516}
    ]
  },
  {
    day: 12,
    title: 'Passage Pathing',
    inputs: './12-passage-pathing/inputs.txt',
    parts: [
      {func: day12part1, solution: 4720},
      {func: day12part2, solution: 147848}
    ]
  },
  {
    day: 13,
    title: 'Transparent Origami', 
    inputs: './13-transparent-origami/inputs.txt', 
    parts: [
      {func: day13part1, solution: 708},
      {func: day13part2, solution: "#### ###  #    #  # ###  ###  #### #  #\n#    #  # #    #  # #  # #  # #    #  #\n###  ###  #    #  # ###  #  # ###  ####\n#    #  # #    #  # #  # ###  #    #  #\n#    #  # #    #  # #  # # #  #    #  #\n#### ###  ####  ##  ###  #  # #    #  #"}
    ]
  },
  {
    day: 14,
    title: 'Extended Polymerization',
    inputs: './14-extended-polymerization/inputs.txt',
    parts: [
      {func: day14part1, solution: 3306},
      {func: day14part2, solution: 3760312702877}
    ]
  }
];

const summary = {};
for (const puzzle of puzzles) {
  const record = {};
  console.log(`~~~ Day ${puzzle.day} - ${puzzle.title} ~~~~~~~~~~`.toUpperCase());
  console.log();
  for (let i=0; i<puzzle.parts.length; i++) {
    const startTime = performance.now();
    const solution = puzzle.parts[i].func(puzzle.inputs);
    const endTime = performance.now();
    const runTime = ((endTime - startTime) / 1000).toFixed(4);
    const pass = solution===puzzle.parts[i].solution;
    console.log(`Part ${i+1} (${pass ? 'PASS' : 'FAIL'}, ${runTime} sec):`);
    console.log(solution);
    console.log();
    record[`passPart${i+1}`] = pass;
    record[`timePart${i+1}`] = `${runTime} sec`;
  }
  summary[`day${puzzle.day}`] = record;
}

console.log('SUMMARY:');
console.table(summary);