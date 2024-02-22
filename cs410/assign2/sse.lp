\ENCODING=ISO-8859-1
\Problem name: 

Maximize
 obj1: vdef
Subject To
 c1:  z1 + z2 + z3 + z4 + z5  = 1
 c2:  x1 + x2 + x3 + x4 + x5  = 2
 c3:  - 5 x1 + 1000 z1 + vdef <= 999
 c4:  - 7 x2 + 1000 z2 + vdef <= 998
 c5:  - 3 x3 + 1000 z3 + vdef <= 1000
 c6:  - 9 x4 + 1000 z4 + vdef <= 997
 c7:  - 10 x5 + 1000 z5 + vdef <= 997
 c8:  2 x1 + vatt >= 2
 c9:  4 x2 + vatt >= 3
 c10: 7 x3 + vatt >= 5
 c11: 5 x4 + vatt >= 4
 c12: 9 x5 + vatt >= 6
 c13: 2 x1 + 1000 z1 + vatt <= 1002
 c14: 4 x2 + 1000 z2 + vatt <= 1003
 c15: 7 x3 + 1000 z3 + vatt <= 1005
 c16: 5 x4 + 1000 z4 + vatt <= 1004
 c17: 9 x5 + 1000 z5 + vatt <= 1006
Bounds
 0 <= x1 <= 1
 0 <= x2 <= 1
 0 <= x3 <= 1
 0 <= x4 <= 1
 0 <= x5 <= 1
 0 <= z1 <= 1
 0 <= z2 <= 1
 0 <= z3 <= 1
 0 <= z4 <= 1
 0 <= z5 <= 1
      vdef Free
      vatt Free
Binaries
 z1  z2  z3  z4  z5 
End
