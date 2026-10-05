.dictionary | keys | map(select(
  contains("(-)") and
  (startswith("(-)") | not) and
  (endswith("(-)") | not) and
  (startswith("](-)") | not) and
  (endswith("(-)[") | not) and
  (startswith("]x(-)") | not) and
  (endswith("(-)x[") | not) and
  (startswith("x(-)") | not) and
  (endswith("(-)x") | not) and
  (endswith("(-) ") | not)
)) | join("\n")
