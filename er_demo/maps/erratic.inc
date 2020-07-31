define erratic position
(
  size [0.40 0.40 0.3]
  origin [-0.050 0 0 0]
  gui_nose 1
  drive "diff"
  localization "odom"
  odom_error [ 0.01 0.01 0.0 0.1 ]
  topurg(pose [ 0.050 0 -0.1 0 ])
)

