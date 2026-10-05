import json
from argparse import ArgumentParser
from .gensegm import generate_segmentations
from .combsegm import combine_segmentations

def gensegm_stdin(optional_boundary: str,
                  connecting_string: str) -> None:
  try:
    while (generic_segmentation := input()) != '':
      segmentations = list(generate_segmentations(optional_boundary,
                                                  connecting_string,
                                                  generic_segmentation))
      serialized = json.dumps(segmentations, ensure_ascii=False)
      print(serialized)
  except EOFError:
    pass

def combsegm_stdin(optional_boundary: str,
                   connecting_string: str) -> None:
  try:
    while (serialized_segmentations := input()) != '':
      segmentations = json.loads(serialized_segmentations)
      generic_segmentation = combine_segmentations(optional_boundary,
                                                   connecting_string,
                                                   segmentations)
      print(generic_segmentation)
  except EOFError:
    pass


parser = ArgumentParser(
  prog='ambisegm',
  description='Conversion between alternative segmentations of the same sequence and a single generic segmentation'
)
parser.add_argument(
  'optional_boundary',
  help='A string marking the possible split locations in the generic segmentation'
)
parser.add_argument(
  'connecting_string',
  help='A string connecting segments when no boundary is between them'
)
subparsers = parser.add_subparsers(required=True)
subparsers.add_parser(
  'generate-segmentations',
  help='Generate a list of alternative segmentations from a generic segmentation'
).set_defaults(func=gensegm_stdin)
subparsers.add_parser(
  'combine-segmentations',
  help='Generate a generic segmentation from a list of alternative segmentations'
).set_defaults(func=combsegm_stdin)
args = parser.parse_args()
args.func(args.optional_boundary, args.connecting_string)
