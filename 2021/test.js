import { part1 as day01part1, part2 as day01part2 } from './01-sonar-sweep/01-sonar-sweep.js';
import { part1 as day02part1, part2 as day02part2 } from './02-dive/02-dive.js';
import { part1 as day03part1, part2 as day03part2 } from './03-binary-diagnostic/03-binary-diagnostic.js';
import { part1 as day04part1, part2 as day04part2 } from './04-giant-squid/04-giant-squid.js';
import { part1 as day12part1, part2 as day12part2 } from './12-passage-pathing/12-passage-pathing.js';
import { part1 as day13part1, part2 as day13part2 } from './13-transparent-origami/13-transparent-origami.js';
import { part1 as day14part1, part2 as day14part2 } from './14-extended-polymerization/14-extended-polymerization.js';
import { part1 as day15part1, part2 as day15part2 } from './15-chiton/15-chiton.js';
import { part1 as day16part1, part2 as day16part2 } from './16-packet-decoder/16-packet-decoder.js';
import { part1 as day17part1, part2 as day17part2 } from './17-trick-shot/17-trick-shot.js';

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
    day: 2,
    title: 'Dive!',
    inputs: './02-dive/inputs.txt',
    parts: [
      {func: day02part1, solution: 1507611},
      {func: day02part2, solution: 1880593125}
    ]
  },
  {
    day: 3,
    title: 'Binary Diagnostic',
    inputs: './03-binary-diagnostic/inputs.txt',
    parts: [
      {func: day03part1, solution: 4138664},
      {func: day03part2, solution: 4273224}
    ]
  },
  {
    day: 4,
    title: 'Giant Squit',
    inputs: './04-giant-squid/inputs.txt',
    parts: [
      {func: day04part1, solution: 49686},
      {func: day04part2, solution: 26878}
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
  },
  {
    day: 15,
    title: 'Chiton',
    inputs: './15-chiton/inputs.txt',
    parts: [
      {func: day15part1, solution: 523},
      {func: day15part2, solution: 2876}
    ]
  },
  {
    day: 16,
    title: 'Packet Decoder',
    inputs: './16-packet-decoder/inputs.txt',
    parts: [
      {func: day16part1, solution: 974},
      {func: day16part2, solution: 180616437720}
    ]
  },
  {
    day: 17,
    title: 'Trick Shot',
    inputs: './17-trick-shot/inputs.txt',
    parts: [
      {func: day17part1, solution: 10296},
      {func: day17part2, solution: 2371}
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