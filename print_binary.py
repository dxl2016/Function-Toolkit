def print_binary(k):
  end = 1 << k   
  for i in range(end): 
    arg = bin(i)[2:].zfill(k)
    print(''.join([str(int(x)) for x in arg]))
