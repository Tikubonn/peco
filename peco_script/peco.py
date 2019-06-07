
from argparse import ArgumentParser, FileType
from peco.parser import parse
import json


def __main__():
    argparser = ArgumentParser(
        description="transform text file with peco template engine.",
    )
    argparser.add_argument(
        "input_file",
        help="take an input file name. if you didn't use this option, peco use standard-input.",
        type=FileType(mode="r", encoding="utf-8"),
        default="-",
        nargs="?"
    )
    argparser.add_argument(
        "--parameter",
        dest="parameter",
        help="take a parameter text that must be .json file format. if you didn't use this option, peco use empty associative-array.",
        default=None
    )
    argparser.add_argument(
        "-p",
        "--parameter-file",
        dest="parameter_file",
        help="take a parameter file name that must be .json file format. if you didn't use this option, peco use empty associative-array.",
        type=FileType(mode="r", encoding="utf-8")
    )
    argparser.add_argument(
        "-o",
        "--output-file",
        dest="output_file",
        help="take an output file name. if you didn't use this option, peco use standard-output.",
        type=FileType(mode="w", encoding="utf-8"),
        default="-"
    )
    argparser.add_argument(
        "-v",
        "--version",
        help="print version and exit.",
        action="version",
        version="peco version 0.9.0"
    )
    arguments = argparser.parse_args()
    # main
    template = parse(arguments.input_file)
    parameter = {}
    if arguments.parameter is not None:
        parameter = json.loads(arguments.parameter)
    elif arguments.parameter_file is not None:
        parameter = json.load(arguments.parameter_file)
    template.render(arguments.output_file, **parameter)


def main():
    try:
        __main__()
    except KeyboardInterrupt:
        pass
