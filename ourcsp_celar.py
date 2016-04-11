from cspbase import *
from propagators import *
def sat_abseq(d, eqv):
	vara = d[0]
	varb = d[1]
	output = []
	for i in vara.dom:
		for j in varb.dom:
			if abs(i - j) == eqv:
				output.append((i, j))
	return output
csp = SCSP(' CELAR6SUB0 ')
x13 = Variable('x13', [ 16,30,44,58,72,86,100,114,128,142,156,254,268,282,296,310,324,338,352,366,380,394,414,428,442,456,470,484,498,512,526,540,554,652,666,680,694,708,722,736,750,764,778,792 ])
csp.add_var( x13 )
x14 = Variable('x14', [ 16,30,44,58,72,86,100,114,128,142,156,254,268,282,296,310,324,338,352,366,380,394,414,428,442,456,470,484,498,512,526,540,554,652,666,680,694,708,722,736,750,764,778,792 ])
csp.add_var( x14 )
x15 = Variable('x15', [ 16,30,44,58,72,86,100,114,128,142,156,254,268,282,296,310,324,338,352,366,380,394,414,428,442,456,470,484,498,512,526,540,554,652,666,680,694,708,722,736,750,764,778,792 ])
csp.add_var( x15 )
x16 = Variable('x16', [ 16,30,44,58,72,86,100,114,128,142,156,254,268,282,296,310,324,338,352,366,380,394,414,428,442,456,470,484,498,512,526,540,554,652,666,680,694,708,722,736,750,764,778,792 ])
csp.add_var( x16 )
x321 = Variable('x321', [ 16,30,44,58,72,86,100,114,128,142,156,254,268,282,296,310,324,338,352,366,380,394,414,428,442,456,470,484,498,512,526,540,554,652,666,680,694,708,722,736,750,764,778,792 ])
csp.add_var( x321 )
x322 = Variable('x322', [ 16,30,44,58,72,86,100,114,128,142,156,254,268,282,296,310,324,338,352,366,380,394,414,428,442,456,470,484,498,512,526,540,554,652,666,680,694,708,722,736,750,764,778,792 ])
csp.add_var( x322 )
x323 = Variable('x323', [ 16,30,44,58,72,86,100,114,128,142,156,254,268,282,296,310,324,338,352,366,380,394,414,428,442,456,470,484,498,512,526,540,554,652,666,680,694,708,722,736,750,764,778,792 ])
csp.add_var( x323 )
x324 = Variable('x324', [ 16,30,44,58,72,86,100,114,128,142,156,254,268,282,296,310,324,338,352,366,380,394,414,428,442,456,470,484,498,512,526,540,554,652,666,680,694,708,722,736,750,764,778,792 ])
csp.add_var( x324 )
x519 = Variable('x519', [ 30,44,58,72,86,100,114,128,142,268,282,296,310,324,338,352,366,380,428,442,456,470,484,498,512,526,540,666,680,694,708,722,736,750,764,778 ])
csp.add_var( x519 )
x520 = Variable('x520', [ 30,44,58,72,86,100,114,128,142,268,282,296,310,324,338,352,366,380,428,442,456,470,484,498,512,526,540,666,680,694,708,722,736,750,764,778 ])
csp.add_var( x520 )
x557 = Variable('x557', [ 30,44,58,72,86,100,114,128,142,268,282,296,310,324,338,352,366,380,428,442,456,470,484,498,512,526,540,666,680,694,708,722,736,750,764,778 ])
csp.add_var( x557 )
x558 = Variable('x558', [ 30,44,58,72,86,100,114,128,142,268,282,296,310,324,338,352,366,380,428,442,456,470,484,498,512,526,540,666,680,694,708,722,736,750,764,778 ])
csp.add_var( x558 )
x593 = Variable('x593', [ 30,44,58,72,86,100,114,128,142,268,282,296,310,324,338,352,366,380,428,442,456,470,484,498,512,526,540,666,680,694,708,722,736,750,764,778 ])
csp.add_var( x593 )
x594 = Variable('x594', [ 30,44,58,72,86,100,114,128,142,268,282,296,310,324,338,352,366,380,428,442,456,470,484,498,512,526,540,666,680,694,708,722,736,750,764,778 ])
csp.add_var( x594 )
x597 = Variable('x597', [ 30,44,58,72,86,100,114,128,142,268,282,296,310,324,338,352,366,380,428,442,456,470,484,498,512,526,540,666,680,694,708,722,736,750,764,778 ])
csp.add_var( x597 )
x598 = Variable('x598', [ 30,44,58,72,86,100,114,128,142,268,282,296,310,324,338,352,366,380,428,442,456,470,484,498,512,526,540,666,680,694,708,722,736,750,764,778 ])
csp.add_var( x598 )
x599 = Variable('x599', [ 30,44,58,72,86,100,114,128,142,268,282,296,310,324,338,352,366,380,428,442,456,470,484,498,512,526,540,666,680,694,708,722,736,750,764,778 ])
csp.add_var( x599 )
x600 = Variable('x600', [ 30,44,58,72,86,100,114,128,142,268,282,296,310,324,338,352,366,380,428,442,456,470,484,498,512,526,540,666,680,694,708,722,736,750,764,778 ])
csp.add_var( x600 )
x613 = Variable('x613', [ 30,44,58,72,86,100,114,128,142,268,282,296,310,324,338,352,366,380,428,442,456,470,484,498,512,526,540,666,680,694,708,722,736,750,764,778 ])
csp.add_var( x613 )
x614 = Variable('x614', [ 30,44,58,72,86,100,114,128,142,268,282,296,310,324,338,352,366,380,428,442,456,470,484,498,512,526,540,666,680,694,708,722,736,750,764,778 ])
csp.add_var( x614 )
x629 = Variable('x629', [ 30,44,58,72,86,100,114,128,142,268,282,296,310,324,338,352,366,380,428,442,456,470,484,498,512,526,540,666,680,694,708,722,736,750,764,778 ])
csp.add_var( x629 )
x630 = Variable('x630', [ 30,44,58,72,86,100,114,128,142,268,282,296,310,324,338,352,366,380,428,442,456,470,484,498,512,526,540,666,680,694,708,722,736,750,764,778 ])
csp.add_var( x630 )
x631 = Variable('x631', [ 30,44,58,72,86,100,114,128,142,268,282,296,310,324,338,352,366,380,428,442,456,470,484,498,512,526,540,666,680,694,708,722,736,750,764,778 ])
csp.add_var( x631 )
x632 = Variable('x632', [ 30,44,58,72,86,100,114,128,142,268,282,296,310,324,338,352,366,380,428,442,456,470,484,498,512,526,540,666,680,694,708,722,736,750,764,778 ])
csp.add_var( x632 )
x665 = Variable('x665', [ 16,30,44,58,72,86,100,114,128,142,156,254,268,282,296,310,324,338,352,366,380,394,414,428,442,456,470,484,498,512,526,540,554,652,666,680,694,708,722,736,750,764,778,792 ])
csp.add_var( x665 )
x666 = Variable('x666', [ 16,30,44,58,72,86,100,114,128,142,156,254,268,282,296,310,324,338,352,366,380,394,414,428,442,456,470,484,498,512,526,540,554,652,666,680,694,708,722,736,750,764,778,792 ])
csp.add_var( x666 )
x765 = Variable('x765', [ 16,30,44,58,72,86,100,114,128,142,156,254,268,282,296,310,324,338,352,366,380,394,414,428,442,456,470,484,498,512,526,540,554,652,666,680,694,708,722,736,750,764,778,792 ])
csp.add_var( x765 )
x766 = Variable('x766', [ 16,30,44,58,72,86,100,114,128,142,156,254,268,282,296,310,324,338,352,366,380,394,414,428,442,456,470,484,498,512,526,540,554,652,666,680,694,708,722,736,750,764,778,792 ])
csp.add_var( x766 )
x767 = Variable('x767', [ 16,30,44,58,72,86,100,114,128,142,156,254,268,282,296,310,324,338,352,366,380,394,414,428,442,456,470,484,498,512,526,540,554,652,666,680,694,708,722,736,750,764,778,792 ])
csp.add_var( x767 )
x768 = Variable('x768', [ 16,30,44,58,72,86,100,114,128,142,156,254,268,282,296,310,324,338,352,366,380,394,414,428,442,456,470,484,498,512,526,540,554,652,666,680,694,708,722,736,750,764,778,792 ])
csp.add_var( x768 )
x785 = Variable('x785', [ 16,30,44,58,72,86,100,114,128,142,156,254,268,282,296,310,324,338,352,366,380,394,414,428,442,456,470,484,498,512,526,540,554,652,666,680,694,708,722,736,750,764,778,792 ])
csp.add_var( x785 )
x786 = Variable('x786', [ 16,30,44,58,72,86,100,114,128,142,156,254,268,282,296,310,324,338,352,366,380,394,414,428,442,456,470,484,498,512,526,540,554,652,666,680,694,708,722,736,750,764,778,792 ])
csp.add_var( x786 )
c = Constraint('', [ x13,x14 ])
c.add_satisfying_tuples(sat_abseq(c.scope, 238 ))
csp.add_constraint(c)
c = Constraint('', [ x15,x16 ])
c.add_satisfying_tuples(sat_abseq(c.scope, 238 ))
csp.add_constraint(c)
c = Constraint('', [ x321,x322 ])
c.add_satisfying_tuples(sat_abseq(c.scope, 238 ))
csp.add_constraint(c)
c = Constraint('', [ x323,x324 ])
c.add_satisfying_tuples(sat_abseq(c.scope, 238 ))
csp.add_constraint(c)
c = Constraint('', [ x519,x520 ])
c.add_satisfying_tuples(sat_abseq(c.scope, 238 ))
csp.add_constraint(c)
c = Constraint('', [ x557,x558 ])
c.add_satisfying_tuples(sat_abseq(c.scope, 238 ))
csp.add_constraint(c)
c = Constraint('', [ x593,x594 ])
c.add_satisfying_tuples(sat_abseq(c.scope, 238 ))
csp.add_constraint(c)
c = Constraint('', [ x597,x598 ])
c.add_satisfying_tuples(sat_abseq(c.scope, 238 ))
csp.add_constraint(c)
c = Constraint('', [ x599,x600 ])
c.add_satisfying_tuples(sat_abseq(c.scope, 238 ))
csp.add_constraint(c)
c = Constraint('', [ x613,x614 ])
c.add_satisfying_tuples(sat_abseq(c.scope, 238 ))
csp.add_constraint(c)
c = Constraint('', [ x629,x630 ])
c.add_satisfying_tuples(sat_abseq(c.scope, 238 ))
csp.add_constraint(c)
c = Constraint('', [ x631,x632 ])
c.add_satisfying_tuples(sat_abseq(c.scope, 238 ))
csp.add_constraint(c)
c = Constraint('', [ x665,x666 ])
c.add_satisfying_tuples(sat_abseq(c.scope, 238 ))
csp.add_constraint(c)
c = Constraint('', [ x765,x766 ])
c.add_satisfying_tuples(sat_abseq(c.scope, 238 ))
csp.add_constraint(c)
c = Constraint('', [ x767,x768 ])
c.add_satisfying_tuples(sat_abseq(c.scope, 238 ))
csp.add_constraint(c)
c = Constraint('', [ x785,x786 ])
c.add_satisfying_tuples(sat_abseq(c.scope, 238 ))
csp.add_constraint(c)
csp.add_soft_constraint(SoftConstraint('', [ x13,x15 ], lambda a, b: 0 if abs(a - b) >  59  else   1000 ,mc=  1000 ))
csp.add_soft_constraint(SoftConstraint('', [ x13,x16 ], lambda a, b: 0 if abs(a - b) >  186  else   100 ,mc=  100 ))
csp.add_soft_constraint(SoftConstraint('', [ x13,x321 ], lambda a, b: 0 if abs(a - b) >  10  else   1000 ,mc=  1000 ))
csp.add_soft_constraint(SoftConstraint('', [ x13,x322 ], lambda a, b: 0 if abs(a - b) >  186  else   100 ,mc=  100 ))
csp.add_soft_constraint(SoftConstraint('', [ x13,x323 ], lambda a, b: 0 if abs(a - b) >  168  else   1000 ,mc=  1000 ))
csp.add_soft_constraint(SoftConstraint('', [ x13,x324 ], lambda a, b: 0 if abs(a - b) >  56  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x13,x557 ], lambda a, b: 0 if abs(a - b) >  91  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x13,x558 ], lambda a, b: 0 if abs(a - b) >  265  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x13,x599 ], lambda a, b: 0 if abs(a - b) >  26  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x13,x600 ], lambda a, b: 0 if abs(a - b) >  200  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x13,x665 ], lambda a, b: 0 if abs(a - b) >  177  else   100 ,mc=  100 ))
csp.add_soft_constraint(SoftConstraint('', [ x13,x666 ], lambda a, b: 0 if abs(a - b) >  7  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x13,x767 ], lambda a, b: 0 if abs(a - b) >  62  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x13,x768 ], lambda a, b: 0 if abs(a - b) >  233  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x14,x15 ], lambda a, b: 0 if abs(a - b) >  186  else   100 ,mc=  100 ))
csp.add_soft_constraint(SoftConstraint('', [ x14,x16 ], lambda a, b: 0 if abs(a - b) >  59  else   1000 ,mc=  1000 ))
csp.add_soft_constraint(SoftConstraint('', [ x14,x321 ], lambda a, b: 0 if abs(a - b) >  168  else   100 ,mc=  100 ))
csp.add_soft_constraint(SoftConstraint('', [ x14,x322 ], lambda a, b: 0 if abs(a - b) >  11  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x14,x323 ], lambda a, b: 0 if abs(a - b) >  56  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x14,x324 ], lambda a, b: 0 if abs(a - b) >  151  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x14,x557 ], lambda a, b: 0 if abs(a - b) >  265  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x14,x558 ], lambda a, b: 0 if abs(a - b) >  408  else   100 ,mc=  100 ))
csp.add_soft_constraint(SoftConstraint('', [ x14,x599 ], lambda a, b: 0 if abs(a - b) >  200  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x14,x600 ], lambda a, b: 0 if abs(a - b) >  343  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x14,x665 ], lambda a, b: 0 if abs(a - b) >  8  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x14,x666 ], lambda a, b: 0 if abs(a - b) >  177  else   100 ,mc=  100 ))
csp.add_soft_constraint(SoftConstraint('', [ x14,x767 ], lambda a, b: 0 if abs(a - b) >  121  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x14,x768 ], lambda a, b: 0 if abs(a - b) >  60  else   100 ,mc=  100 ))
csp.add_soft_constraint(SoftConstraint('', [ x15,x321 ], lambda a, b: 0 if abs(a - b) >  10  else   1000 ,mc=  1000 ))
csp.add_soft_constraint(SoftConstraint('', [ x15,x322 ], lambda a, b: 0 if abs(a - b) >  186  else   100 ,mc=  100 ))
csp.add_soft_constraint(SoftConstraint('', [ x15,x323 ], lambda a, b: 0 if abs(a - b) >  168  else   1000 ,mc=  1000 ))
csp.add_soft_constraint(SoftConstraint('', [ x15,x324 ], lambda a, b: 0 if abs(a - b) >  56  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x15,x557 ], lambda a, b: 0 if abs(a - b) >  91  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x15,x558 ], lambda a, b: 0 if abs(a - b) >  265  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x15,x599 ], lambda a, b: 0 if abs(a - b) >  26  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x15,x600 ], lambda a, b: 0 if abs(a - b) >  200  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x15,x665 ], lambda a, b: 0 if abs(a - b) >  177  else   100 ,mc=  100 ))
csp.add_soft_constraint(SoftConstraint('', [ x15,x666 ], lambda a, b: 0 if abs(a - b) >  7  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x15,x767 ], lambda a, b: 0 if abs(a - b) >  62  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x15,x768 ], lambda a, b: 0 if abs(a - b) >  233  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x16,x321 ], lambda a, b: 0 if abs(a - b) >  168  else   100 ,mc=  100 ))
csp.add_soft_constraint(SoftConstraint('', [ x16,x322 ], lambda a, b: 0 if abs(a - b) >  11  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x16,x323 ], lambda a, b: 0 if abs(a - b) >  56  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x16,x324 ], lambda a, b: 0 if abs(a - b) >  151  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x16,x557 ], lambda a, b: 0 if abs(a - b) >  265  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x16,x558 ], lambda a, b: 0 if abs(a - b) >  408  else   100 ,mc=  100 ))
csp.add_soft_constraint(SoftConstraint('', [ x16,x599 ], lambda a, b: 0 if abs(a - b) >  200  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x16,x600 ], lambda a, b: 0 if abs(a - b) >  343  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x16,x665 ], lambda a, b: 0 if abs(a - b) >  8  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x16,x666 ], lambda a, b: 0 if abs(a - b) >  177  else   100 ,mc=  100 ))
csp.add_soft_constraint(SoftConstraint('', [ x16,x767 ], lambda a, b: 0 if abs(a - b) >  121  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x16,x768 ], lambda a, b: 0 if abs(a - b) >  60  else   100 ,mc=  100 ))
csp.add_soft_constraint(SoftConstraint('', [ x321,x323 ], lambda a, b: 0 if abs(a - b) >  178  else   1000 ,mc=  1000 ))
csp.add_soft_constraint(SoftConstraint('', [ x321,x324 ], lambda a, b: 0 if abs(a - b) >  84  else   100 ,mc=  100 ))
csp.add_soft_constraint(SoftConstraint('', [ x321,x557 ], lambda a, b: 0 if abs(a - b) >  99  else   100 ,mc=  100 ))
csp.add_soft_constraint(SoftConstraint('', [ x321,x558 ], lambda a, b: 0 if abs(a - b) >  274  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x321,x594 ], lambda a, b: 0 if abs(a - b) >  216  else   100 ,mc=  100 ))
csp.add_soft_constraint(SoftConstraint('', [ x321,x599 ], lambda a, b: 0 if abs(a - b) >  33  else   100 ,mc=  100 ))
csp.add_soft_constraint(SoftConstraint('', [ x321,x600 ], lambda a, b: 0 if abs(a - b) >  209  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x321,x631 ], lambda a, b: 0 if abs(a - b) >  192  else   100 ,mc=  100 ))
csp.add_soft_constraint(SoftConstraint('', [ x321,x665 ], lambda a, b: 0 if abs(a - b) >  168  else   100 ,mc=  100 ))
csp.add_soft_constraint(SoftConstraint('', [ x321,x666 ], lambda a, b: 0 if abs(a - b) >  12  else   100 ,mc=  100 ))
csp.add_soft_constraint(SoftConstraint('', [ x321,x767 ], lambda a, b: 0 if abs(a - b) >  57  else   100 ,mc=  100 ))
csp.add_soft_constraint(SoftConstraint('', [ x321,x768 ], lambda a, b: 0 if abs(a - b) >  224  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x322,x323 ], lambda a, b: 0 if abs(a - b) >  84  else   100 ,mc=  100 ))
csp.add_soft_constraint(SoftConstraint('', [ x322,x324 ], lambda a, b: 0 if abs(a - b) >  178  else   1000 ,mc=  1000 ))
csp.add_soft_constraint(SoftConstraint('', [ x322,x557 ], lambda a, b: 0 if abs(a - b) >  274  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x322,x558 ], lambda a, b: 0 if abs(a - b) >  416  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x322,x599 ], lambda a, b: 0 if abs(a - b) >  209  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x322,x600 ], lambda a, b: 0 if abs(a - b) >  351  else   100 ,mc=  100 ))
csp.add_soft_constraint(SoftConstraint('', [ x322,x665 ], lambda a, b: 0 if abs(a - b) >  12  else   100 ,mc=  100 ))
csp.add_soft_constraint(SoftConstraint('', [ x322,x666 ], lambda a, b: 0 if abs(a - b) >  186  else   100 ,mc=  100 ))
csp.add_soft_constraint(SoftConstraint('', [ x322,x767 ], lambda a, b: 0 if abs(a - b) >  130  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x322,x768 ], lambda a, b: 0 if abs(a - b) >  53  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x323,x557 ], lambda a, b: 0 if abs(a - b) >  257  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x323,x558 ], lambda a, b: 0 if abs(a - b) >  433  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x323,x594 ], lambda a, b: 0 if abs(a - b) >  57  else   100 ,mc=  100 ))
csp.add_soft_constraint(SoftConstraint('', [ x323,x599 ], lambda a, b: 0 if abs(a - b) >  192  else   100 ,mc=  100 ))
csp.add_soft_constraint(SoftConstraint('', [ x323,x600 ], lambda a, b: 0 if abs(a - b) >  368  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x323,x631 ], lambda a, b: 0 if abs(a - b) >  351  else   100 ,mc=  100 ))
csp.add_soft_constraint(SoftConstraint('', [ x323,x665 ], lambda a, b: 0 if abs(a - b) >  56  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x323,x666 ], lambda a, b: 0 if abs(a - b) >  171  else   100 ,mc=  100 ))
csp.add_soft_constraint(SoftConstraint('', [ x323,x767 ], lambda a, b: 0 if abs(a - b) >  122  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x323,x768 ], lambda a, b: 0 if abs(a - b) >  65  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x324,x557 ], lambda a, b: 0 if abs(a - b) >  116  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x324,x558 ], lambda a, b: 0 if abs(a - b) >  258  else   100 ,mc=  100 ))
csp.add_soft_constraint(SoftConstraint('', [ x324,x599 ], lambda a, b: 0 if abs(a - b) >  56  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x324,x600 ], lambda a, b: 0 if abs(a - b) >  193  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x324,x665 ], lambda a, b: 0 if abs(a - b) >  152  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x324,x666 ], lambda a, b: 0 if abs(a - b) >  56  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x324,x767 ], lambda a, b: 0 if abs(a - b) >  65  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x324,x768 ], lambda a, b: 0 if abs(a - b) >  211  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x519,x597 ], lambda a, b: 0 if abs(a - b) >  293  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x519,x598 ], lambda a, b: 0 if abs(a - b) >  434  else   1000 ,mc=  1000 ))
csp.add_soft_constraint(SoftConstraint('', [ x520,x597 ], lambda a, b: 0 if abs(a - b) >  116  else   1000 ,mc=  1000 ))
csp.add_soft_constraint(SoftConstraint('', [ x520,x598 ], lambda a, b: 0 if abs(a - b) >  293  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x557,x593 ], lambda a, b: 0 if abs(a - b) >  154  else   1000 ,mc=  1000 ))
csp.add_soft_constraint(SoftConstraint('', [ x557,x594 ], lambda a, b: 0 if abs(a - b) >  330  else   100 ,mc=  100 ))
csp.add_soft_constraint(SoftConstraint('', [ x557,x597 ], lambda a, b: 0 if abs(a - b) >  47  else   1000 ,mc=  1000 ))
csp.add_soft_constraint(SoftConstraint('', [ x557,x598 ], lambda a, b: 0 if abs(a - b) >  130  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x557,x599 ], lambda a, b: 0 if abs(a - b) >  66  else   1000 ,mc=  1000 ))
csp.add_soft_constraint(SoftConstraint('', [ x557,x600 ], lambda a, b: 0 if abs(a - b) >  112  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x557,x613 ], lambda a, b: 0 if abs(a - b) >  47  else   1000 ,mc=  1000 ))
csp.add_soft_constraint(SoftConstraint('', [ x557,x614 ], lambda a, b: 0 if abs(a - b) >  130  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x557,x665 ], lambda a, b: 0 if abs(a - b) >  274  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x557,x666 ], lambda a, b: 0 if abs(a - b) >  106  else   1000 ,mc=  1000 ))
csp.add_soft_constraint(SoftConstraint('', [ x557,x767 ], lambda a, b: 0 if abs(a - b) >  151  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x557,x768 ], lambda a, b: 0 if abs(a - b) >  321  else   100 ,mc=  100 ))
csp.add_soft_constraint(SoftConstraint('', [ x557,x785 ], lambda a, b: 0 if abs(a - b) >  47  else   1000 ,mc=  1000 ))
csp.add_soft_constraint(SoftConstraint('', [ x557,x786 ], lambda a, b: 0 if abs(a - b) >  126  else   100 ,mc=  100 ))
csp.add_soft_constraint(SoftConstraint('', [ x558,x593 ], lambda a, b: 0 if abs(a - b) >  330  else   100 ,mc=  100 ))
csp.add_soft_constraint(SoftConstraint('', [ x558,x594 ], lambda a, b: 0 if abs(a - b) >  471  else   1000 ,mc=  1000 ))
csp.add_soft_constraint(SoftConstraint('', [ x558,x597 ], lambda a, b: 0 if abs(a - b) >  224  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x558,x598 ], lambda a, b: 0 if abs(a - b) >  47  else   1000 ,mc=  1000 ))
csp.add_soft_constraint(SoftConstraint('', [ x558,x599 ], lambda a, b: 0 if abs(a - b) >  242  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x558,x600 ], lambda a, b: 0 if abs(a - b) >  66  else   1000 ,mc=  1000 ))
csp.add_soft_constraint(SoftConstraint('', [ x558,x613 ], lambda a, b: 0 if abs(a - b) >  224  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x558,x614 ], lambda a, b: 0 if abs(a - b) >  47  else   1000 ,mc=  1000 ))
csp.add_soft_constraint(SoftConstraint('', [ x558,x665 ], lambda a, b: 0 if abs(a - b) >  423  else   1000 ,mc=  1000 ))
csp.add_soft_constraint(SoftConstraint('', [ x558,x666 ], lambda a, b: 0 if abs(a - b) >  274  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x558,x767 ], lambda a, b: 0 if abs(a - b) >  321  else   100 ,mc=  100 ))
csp.add_soft_constraint(SoftConstraint('', [ x558,x768 ], lambda a, b: 0 if abs(a - b) >  466  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x558,x785 ], lambda a, b: 0 if abs(a - b) >  224  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x558,x786 ], lambda a, b: 0 if abs(a - b) >  47  else   1000 ,mc=  1000 ))
csp.add_soft_constraint(SoftConstraint('', [ x593,x597 ], lambda a, b: 0 if abs(a - b) >  107  else   1000 ,mc=  1000 ))
csp.add_soft_constraint(SoftConstraint('', [ x593,x598 ], lambda a, b: 0 if abs(a - b) >  284  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x593,x613 ], lambda a, b: 0 if abs(a - b) >  107  else   1000 ,mc=  1000 ))
csp.add_soft_constraint(SoftConstraint('', [ x593,x614 ], lambda a, b: 0 if abs(a - b) >  284  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x593,x631 ], lambda a, b: 0 if abs(a - b) >  265  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x593,x632 ], lambda a, b: 0 if abs(a - b) >  88  else   1000 ,mc=  1000 ))
csp.add_soft_constraint(SoftConstraint('', [ x593,x665 ], lambda a, b: 0 if abs(a - b) >  112  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x593,x666 ], lambda a, b: 0 if abs(a - b) >  68  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x593,x767 ], lambda a, b: 0 if abs(a - b) >  12  else   100 ,mc=  100 ))
csp.add_soft_constraint(SoftConstraint('', [ x593,x768 ], lambda a, b: 0 if abs(a - b) >  154  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x593,x785 ], lambda a, b: 0 if abs(a - b) >  107  else   1000 ,mc=  1000 ))
csp.add_soft_constraint(SoftConstraint('', [ x593,x786 ], lambda a, b: 0 if abs(a - b) >  279  else   100 ,mc=  100 ))
csp.add_soft_constraint(SoftConstraint('', [ x594,x597 ], lambda a, b: 0 if abs(a - b) >  284  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x594,x598 ], lambda a, b: 0 if abs(a - b) >  424  else   1000 ,mc=  1000 ))
csp.add_soft_constraint(SoftConstraint('', [ x594,x613 ], lambda a, b: 0 if abs(a - b) >  284  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x594,x614 ], lambda a, b: 0 if abs(a - b) >  424  else   1000 ,mc=  1000 ))
csp.add_soft_constraint(SoftConstraint('', [ x594,x631 ], lambda a, b: 0 if abs(a - b) >  406  else   1000 ,mc=  1000 ))
csp.add_soft_constraint(SoftConstraint('', [ x594,x632 ], lambda a, b: 0 if abs(a - b) >  265  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x594,x665 ], lambda a, b: 0 if abs(a - b) >  68  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x594,x666 ], lambda a, b: 0 if abs(a - b) >  242  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x594,x767 ], lambda a, b: 0 if abs(a - b) >  172  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x594,x768 ], lambda a, b: 0 if abs(a - b) >  13  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x594,x785 ], lambda a, b: 0 if abs(a - b) >  284  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x594,x786 ], lambda a, b: 0 if abs(a - b) >  424  else   1000 ,mc=  1000 ))
csp.add_soft_constraint(SoftConstraint('', [ x597,x613 ], lambda a, b: 0 if abs(a - b) >  2  else   1000 ,mc=  1000 ))
csp.add_soft_constraint(SoftConstraint('', [ x597,x614 ], lambda a, b: 0 if abs(a - b) >  177  else   100 ,mc=  100 ))
csp.add_soft_constraint(SoftConstraint('', [ x597,x665 ], lambda a, b: 0 if abs(a - b) >  218  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x597,x666 ], lambda a, b: 0 if abs(a - b) >  44  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x597,x767 ], lambda a, b: 0 if abs(a - b) >  100  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x597,x768 ], lambda a, b: 0 if abs(a - b) >  259  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x597,x785 ], lambda a, b: 0 if abs(a - b) >  2  else   1000 ,mc=  1000 ))
csp.add_soft_constraint(SoftConstraint('', [ x597,x786 ], lambda a, b: 0 if abs(a - b) >  172  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x598,x613 ], lambda a, b: 0 if abs(a - b) >  177  else   100 ,mc=  100 ))
csp.add_soft_constraint(SoftConstraint('', [ x598,x614 ], lambda a, b: 0 if abs(a - b) >  2  else   1000 ,mc=  1000 ))
csp.add_soft_constraint(SoftConstraint('', [ x598,x665 ], lambda a, b: 0 if abs(a - b) >  361  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x598,x666 ], lambda a, b: 0 if abs(a - b) >  218  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x598,x768 ], lambda a, b: 0 if abs(a - b) >  418  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x598,x785 ], lambda a, b: 0 if abs(a - b) >  177  else   100 ,mc=  100 ))
csp.add_soft_constraint(SoftConstraint('', [ x598,x786 ], lambda a, b: 0 if abs(a - b) >  2  else   1000 ,mc=  1000 ))
csp.add_soft_constraint(SoftConstraint('', [ x599,x665 ], lambda a, b: 0 if abs(a - b) >  200  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x599,x666 ], lambda a, b: 0 if abs(a - b) >  26  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x599,x767 ], lambda a, b: 0 if abs(a - b) >  87  else   100 ,mc=  100 ))
csp.add_soft_constraint(SoftConstraint('', [ x599,x768 ], lambda a, b: 0 if abs(a - b) >  256  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x600,x665 ], lambda a, b: 0 if abs(a - b) >  343  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x600,x666 ], lambda a, b: 0 if abs(a - b) >  200  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x600,x767 ], lambda a, b: 0 if abs(a - b) >  256  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x600,x768 ], lambda a, b: 0 if abs(a - b) >  401  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x613,x665 ], lambda a, b: 0 if abs(a - b) >  218  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x613,x666 ], lambda a, b: 0 if abs(a - b) >  42  else   1000 ,mc=  1000 ))
csp.add_soft_constraint(SoftConstraint('', [ x613,x765 ], lambda a, b: 0 if abs(a - b) >  47  else   1000 ,mc=  1000 ))
csp.add_soft_constraint(SoftConstraint('', [ x613,x766 ], lambda a, b: 0 if abs(a - b) >  224  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x613,x768 ], lambda a, b: 0 if abs(a - b) >  258  else   100 ,mc=  100 ))
csp.add_soft_constraint(SoftConstraint('', [ x613,x785 ], lambda a, b: 0 if abs(a - b) >  28  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x613,x786 ], lambda a, b: 0 if abs(a - b) >  172  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x614,x665 ], lambda a, b: 0 if abs(a - b) >  359  else   1000 ,mc=  1000 ))
csp.add_soft_constraint(SoftConstraint('', [ x614,x666 ], lambda a, b: 0 if abs(a - b) >  218  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x614,x765 ], lambda a, b: 0 if abs(a - b) >  126  else   100 ,mc=  100 ))
csp.add_soft_constraint(SoftConstraint('', [ x614,x766 ], lambda a, b: 0 if abs(a - b) >  47  else   1000 ,mc=  1000 ))
csp.add_soft_constraint(SoftConstraint('', [ x614,x767 ], lambda a, b: 0 if abs(a - b) >  258  else   100 ,mc=  100 ))
csp.add_soft_constraint(SoftConstraint('', [ x614,x768 ], lambda a, b: 0 if abs(a - b) >  418  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x614,x785 ], lambda a, b: 0 if abs(a - b) >  177  else   100 ,mc=  100 ))
csp.add_soft_constraint(SoftConstraint('', [ x614,x786 ], lambda a, b: 0 if abs(a - b) >  25  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x629,x631 ], lambda a, b: 0 if abs(a - b) >  266  else   1000 ,mc=  1000 ))
csp.add_soft_constraint(SoftConstraint('', [ x629,x632 ], lambda a, b: 0 if abs(a - b) >  125  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x629,x768 ], lambda a, b: 0 if abs(a - b) >  134  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x630,x631 ], lambda a, b: 0 if abs(a - b) >  442  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x630,x632 ], lambda a, b: 0 if abs(a - b) >  266  else   1000 ,mc=  1000 ))
csp.add_soft_constraint(SoftConstraint('', [ x630,x768 ], lambda a, b: 0 if abs(a - b) >  31  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x631,x767 ], lambda a, b: 0 if abs(a - b) >  241  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x631,x768 ], lambda a, b: 0 if abs(a - b) >  400  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x632,x767 ], lambda a, b: 0 if abs(a - b) >  83  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x665,x767 ], lambda a, b: 0 if abs(a - b) >  121  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x665,x768 ], lambda a, b: 0 if abs(a - b) >  60  else   100 ,mc=  100 ))
csp.add_soft_constraint(SoftConstraint('', [ x665,x785 ], lambda a, b: 0 if abs(a - b) >  218  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x665,x786 ], lambda a, b: 0 if abs(a - b) >  361  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x666,x767 ], lambda a, b: 0 if abs(a - b) >  62  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x666,x768 ], lambda a, b: 0 if abs(a - b) >  233  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x666,x785 ], lambda a, b: 0 if abs(a - b) >  44  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x666,x786 ], lambda a, b: 0 if abs(a - b) >  214  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x765,x767 ], lambda a, b: 0 if abs(a - b) >  146  else   1 ,mc=  1 ))
csp.add_soft_constraint(SoftConstraint('', [ x767,x785 ], lambda a, b: 0 if abs(a - b) >  100  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x767,x786 ], lambda a, b: 0 if abs(a - b) >  259  else   10 ,mc=  10 ))
csp.add_soft_constraint(SoftConstraint('', [ x768,x785 ], lambda a, b: 0 if abs(a - b) >  259  else   10 ,mc=  10 ))
bb = BB(csp, UB= 160 )
#bb.trace_on()
bb.bb_search(prop_GAC)
