def pos_neg(a, b, negative):
  return((not negative and a*b<0)or(negative and a<0 and b<0))