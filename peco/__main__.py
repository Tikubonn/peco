
import json
import argparse
from .parser import parse

if __name__ == "__main__":
  try:
    argparser = argparse.ArgumentParser(
      description = "transform text file with peco template engine.",
    )
    argparser.add_argument(
      "-v",
      "--version",
      help = "print version and exit.",
      action = "version",
      version = "peco version 0.9.0"
    )
    argparser.add_argument(
      "-f",
      "--input-file", 
      dest = "input_file",
      help = "take an input file name. if you didn't use this option, peco use standard-input.",
      type = argparse.FileType("r", encoding="utf-8"),
      default="-"
    )
    argparser.add_argument(
      "-p"
      "--parameter-file",
      dest = "parameter_file",
      help = "take a parameter file name that must be .json file format. if you didn't use this option, peco use empty associative-array.",
      type = argparse.FileType("r", encoding="utf-8"))
    argparser.add_argument(
      "-o",
      "--output-file", 
      dest = "output_file",
      help = "take an output file name. if you didn't use this option, peco use standard-output.",
      type = argparse.FileType("w", encoding="utf-8"),
      default="-"
    )
    arguments = argparser.parse_args()
    template = parse(arguments.input_file)
    parameter = {}
    if arguments.parameter_file is not None:
      parameter = json.load(arguments.parameter_file)
    template.render(arguments.output_file, **parameter)
  except KeyboardInterrupt:
    pass
