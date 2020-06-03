def checkSubset(lng, shrt):
  count_lng = collections.Counter(lng) 
  count_shrt = collections.Counter(shrt) 

  for key in count_shrt: 
      if key not in count_lng: 
          return False
      if count_shrt[key] > count_lng[key]: 
          return False
  return True
