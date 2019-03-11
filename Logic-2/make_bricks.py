def make_bricks(small, big, goal):
  if(((goal//5<=big)and(small>=goal-goal//5*5))or((goal//5>big)and(small>=goal-big*5))):
    return True
  else:
    return False
