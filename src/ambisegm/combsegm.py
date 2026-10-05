from collections.abc import Iterable

def remove_prefix_from_first(segmentation: list[str],
                             prefix: str,
                             connecting_string: str) -> list[str]:
  """Remove a prefix from the first segment of a segmentation,
  dropping this segment if it has become empty.
  :param segmentation:
  :return: The modified segmentation.
  """
  if len(segmentation) > 1:
    tail = segmentation[1:]
  else:
    tail = []
  if segmentation[0] == prefix:
    return tail
  else:
    first_segment = segmentation[0]
    pref_with_conn = prefix + connecting_string
    assert first_segment.startswith(pref_with_conn)
    new_first = first_segment.removeprefix(pref_with_conn)
    if len(new_first) == 0:
      return tail
    else:
      return [new_first] + tail

def combine_segmentations(optional_boundary: str,
                          connecting_string: str,
                          segmentations: Iterable[list[str]]) -> str:
  """Combine a set of possible segmentations to a
  generic segmentation with optional boundaries.
  :param segmentations: An iterable of segmentations,
  represented as lists of strings
  :param optional_boundary:
  :param connecting_string: A string to use in place of the
  optional boundary when it is not treated as a boundary.
  :return: The generic segmentation with optional boundaries as a string
  """
  non_empty = list(
    filter(lambda segmentation: len(segmentation) > 0, segmentations)
  )
  if len(non_empty) == 0:
    return ''
  # Find the segmentation with the shortest first segment
  with_shortest_first_segment = min(
    non_empty,
    key = lambda segmentation: len(segmentation[0])
  )
  shortest_first_segment = with_shortest_first_segment[0]
  # Remove the shortes segment from the beginning
  # of all the segmentations
  without_prefix = map(
    lambda segmentation: remove_prefix_from_first(
      segmentation, shortest_first_segment, connecting_string
    ),
    non_empty
  )
  tail = combine_segmentations(
    optional_boundary,
    connecting_string,
    without_prefix
  )
  return shortest_first_segment + \
    optional_boundary + tail

if __name__ == '__main__':
  optional_boundary = '(-)'
  connecting_string = '-'
  segmentation_lists = [
    [
      ['ḫu-u-e-ni', 'e-waa-ni-ib-bi'],
      ['ḫu-u-e-ni-e-waa', 'ni-ib-bi']
    ],
    [
      ['ḫu-u-e-ni', 'e-waa-ni-ib-bi'],
      ['ḫu-u-e-ni-e-waa', 'ni-ib-bi'],
      ['ḫu-u-e-ni', 'e-waa', 'ni-ib-bi']
    ],
    [
      ['ḫu-u-e-ni-e-waa-ni-ib-bi'],
      ['ḫu-u-e-ni', 'e-waa-ni-ib-bi'],
      ['ḫu-u-e-ni-e-waa', 'ni-ib-bi']
    ],
    [
      ['ḫu-u-e-ni-e-waa-ni-ib-bi'],
      ['ḫu-u-e-ni', 'e-waa-ni-ib-bi'],
      ['ḫu-u-e-ni-e-waa', 'ni-ib-bi'],
      ['ḫu-u-e-ni', 'e-waa', 'ni-ib-bi']
    ],
    [
      ['te-eḫ-tu-li-el-li-e'],
      ['te-eḫ-tu', 'li-el-li-e']
    ]
  ]
  for segmentations in segmentation_lists:
    generic_segmentation = combine_segmentations(
      optional_boundary, connecting_string, segmentations
    )
    print(generic_segmentation)
