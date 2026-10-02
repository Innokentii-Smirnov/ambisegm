from collections.abc import Iterable

def generate_segmentations(optional_boundary: str,
                           connecting_string: str,
                           generic_segmentation: str) -> Iterable[list[str]]:
  """Generate a set of possible segmentations from a
  generic segmentation with optional boundaries.
  :param optional_boundary:
  :param connecting_string: A string to use in place of the optional boundary
  when it is not treated as a boundary.
  :param generic_segmentation:
  :return: An iterator over the segmentations,
  represented as lists of strings
  """
  left, sep, right = generic_segmentation.partition(optional_boundary)
  if sep == '':
    yield [generic_segmentation]
  else:
    continuations = generate_segmentations(optional_boundary,
                                           connecting_string,
                                           right)
    for continuation in continuations:
      # A continuation always contains at least one element
      # because it is yielded by generate_segmenations,
      # and generate_segmenations always returns a list
      # with at least one-element
      first_element = left + connecting_string + continuation[0]
      if len(continuation) > 1:
        yield [first_element] + continuation[1:]
      else:
        yield [first_element]
      yield [left] + continuation

if __name__ == '__main__':
  optional_boundary = '(-)'
  connecting_string = '-'
  generic_segmentations = [
    'ma-a-nu(-)ne-eš-ši-⸢pa?⸣',
    'pu-u-ra-al-⸢li⸣-ni(-)ni-eš-⸢ša⸣',
    'te-eḫ-tu(-)li-el-li-e',
    'ḫu-u-te-er-na(-)aš(-)tu-u-ḫu-li-e-⸢da?-an?⸣',
    'ḫu-u-e-ni(-)e-waa(-)ni-ib-bi'
  ]
  for generic_segmentation in generic_segmentations:
    print(generic_segmentation)
    segmentations = generate_segmentations(optional_boundary,
                                           connecting_string,
                                           generic_segmentation)
    for segmentation in segmentations:
      print('\t' + (3 * ' ').join(segmentation))
