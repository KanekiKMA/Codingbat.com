def make_chocolate(small, big, goal):
  if((goal/5<=big)and(small>=goal-goal//5*5)):
    return (goal-goal//5*5)
  elif((goal/5>big)and(small>=goal-big*5)):
    return goal-big*5
  else:
    return -1
