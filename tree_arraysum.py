def tree_arraysum(arr):
  if len(arr) < 2:
    return ''
  left = 0
  right = 0

  depth = 1
  i_start = 1
  i_end = 2
  i_mid = 2

  i = 1
  while i < len(arr):
    if arr[i] == -1:
      pass
    elif i < i_mid:
      left += arr[i]
    else:
      right += arr[i]
    
    if i == i_end:
      i_start = i_end + 1
      depth += 1
      i_end = i_start + 2**depth - 1
      i_mid = -(-(i_start + i_end)//2)
      print(i_start, i_mid, i_end)
    i += 1
  print(left, right)
  return '' if right == left else ('Right' if right > left else 'Left')