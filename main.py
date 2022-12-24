import cmd
import importlib
import os
import re

class AdventOfCodeShell(cmd.Cmd):
    intro = ''
    prompt = '(AoC) '

    def do_run(self, arg):
        """
        Run every day's solution for each year: RUN
        Run every day's solution for a single year: RUN 2017
        Run a specific day's solution: RUN 2017 1
        """
        parsed_args = self.parse_arg(arg)
        years = self.get_years() if len(parsed_args) == 0 else [f'year_{parsed_args[0]}']
        days = None if len(parsed_args) <= 1 else [f'day_{parsed_args[1].rjust(2, "0")}']

        for year in years:
            for day in (days or self.get_days(year)):
                solution = importlib.import_module(f'{year}.{day}.solution')
                print(f'Running year {year.split("_")[1]} day {day.split("_")[1]}')
                print('Part 1:', solution.part_1())
                print('Part 2:', solution.part_2())

    def do_quit(self, arg):
        """
        Exit the CLI.
        """
        return True

    def get_days(self, year: str):
        return sorted([name for name in os.listdir(year) if os.path.isdir(f'{year}/{name}') and re.fullmatch(r'day_\d{2}', name)])

    def get_years(self):
        return sorted([name for name in os.listdir('.') if os.path.isdir(name) and re.fullmatch(r'year_\d{4}', name)])

    def parse_arg(self, arg):
        return tuple(arg.split(' ')) if arg else tuple()

if __name__ == '__main__':
    AdventOfCodeShell().cmdloop()
