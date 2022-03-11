from markdown import markdown, markdownFromFile
import pdfkit

import markdown_preprocessor as mp
from game_systems.CoCSverige.CoCSverige import CoCSverige
import argparse

GAMESYSTEMS = [
    CoCSverige,
]


def get_systems():
    res = {}
    for instance in GAMESYSTEMS:
        res[instance.abbr] = instance

    return res


def get_systems_string():
    res = ""
    for instance in GAMESYSTEMS:
        res += f"\t{instance.abbr} - {instance.name}\n"
    return res


def main():
    parser = argparse.ArgumentParser(
        description="Markdown parser for Campange Generator")
    parser.add_argument('inputfile', nargs="?")
    parser.add_argument('-o', '--outputfile', help="Filepath for generated file")
    parser.add_argument('-s', '--gamesystem', help="Specify gamesystem the input file "
                                                   "should be generated by"
                        )
    parser.add_argument('-S', '--showsystems', action='store_true', help="Show available gamesystems")
    parser.add_argument('-H', '--html', action='store_true', help="Generate HTML instead of PDF")

    args = parser.parse_args()

    if args.showsystems:
        print("Available game systems are:\n" + get_systems_string())
        exit()
    elif not args.inputfile:
        print("No input file specified")
        exit()
    elif not args.gamesystem:
        print("No gamesystem specified. The available game systems are:\n"
              + get_systems_string())
        exit()

    elif not args.gamesystem in get_systems():
        print(f'No gamesystem called "{args.gamesystem}". The available game '
              'systems are:\n' + get_systems_string())
        exit()

    system = get_systems()[args.gamesystem]
    with open(args.inputfile) as file:
        res = mp.parse_markdown(file.read(), system)

    if args.html:
        with open((args.inputfile + '.html') if not args.outputfile else args.outputfile, 'w') as file:
            file.write(res)
            print("Done")
    else:
        try:
            pdfkit.from_string(res, (args.inputfile + '.pdf') if not args.outputfile else args.outputfile)
            print("Done")
        except OSError as e:
            print(e)


if __name__ == '__main__':
    main()
