# Given a binary array, find the maximum number of consecutive 1s in this array.

## Follow up: solve it without converting the integer to a string?

### Efficeint solution : 
  Instead of reversing complete number we need to figure out midpoint of number reverse till there and check it with other half.
  if it matches it is palindrome else it is not. 

#### full reverse : o{n}
#### mid point reverse : o{n/2}
