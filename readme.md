Seros ARS-Regendi Rating System
===============================

This script is used for getting the rating of states.

###Required things:
- Python 2.7
- lxml (http://lxml.de/)

***

###The script is using the following formular:

Version: 210413

**The international Reputation:**

If Int. Rep < 0 -> Wruf = -Rf
If Int. Rep >= 0 -> Wruf = Int. Rep

**Next step is the regentfactor (Rf)**

Rf = (Popularity + Influence) * Election in %

**Now the qualitative factor "The Statefactor"**

STf = Rf + Wruf

If STf > 1 then just the decimal place is used and is added by 1 (e.g. STf = 4.3 => 1.3)
If STf > 0 && STf < 1 then STf stays the same (e.g. STf = 0.6 => 0.6)
If STf < 0 then STf becomes 0

**Quantitative factors**

This part comes by the user Himami.

X1 = Gov.-Debt / nom. GDP
X2 = new debt / nom. GDP
X3 = interest payment / state income

**Award for points**

X1 over -30% = 5 points
X1 under -30% = 4 points
X1 under -50% = 3 points
X1 under -80% = 2 points
X1 under -100% = 1 points
X1 under -150% = 0 points

X2 over 0% = 3 points
X2 under 0% = 2 points
X2 under -3% = 1 points
X2 under -6% = 0 points

X3 over 0% = 5 points
X3 under 0% = 4 points
X3 under -3% = 2 points
X3 under -6% = 1 points
X3 under -8% = 0 points

**Yearly economic growth (X4)**

state-template dependent factor (Y)
Code:
superpower: 2.0%
industrial power: 2.2%
ressource power: 1.9%
Emerging nation: 2.5%
industrial country: 1.9%
postcommunistic: 2.3%
fundamentalist: 2.6%
developing country: 1.3%

Formular - calculating X4
Economy previous year >= Y => 2 points
0 < Economy previous year < Y => 1 points
Economy previous year = 0 => 0 points
Economy previous year < 0 => -1 points

All points get added together

Rating-points = X1 + X2 + X3 + X4 + STf

**State-template bonus**

superpower, industrial power: +3 points
ressource power: +1 points
industrial country, Emerging nation: +- 0 points
postcommunistic, fundamentalist, developing country: -1 points

The bonus gets added

**Sign**

X1, X2, X3 and X4 are considered.

If the difference between the 2 highest numbers are equal or higher than 2 => "-"
If the difference between the 2 lowest numbers are equal or higher than 2 => "+"
If both happens no sign will be added.

Highest possible Score: 16 points

Rating = Points
- AAA   = 98% - 100%
- AA    = 86% - 98%
- A     = 74% - 86%
- BBB   = 62% - 74%
- BB    = 50% - 62%
- B     = 38% - 50%
- CCC   = 26% - 38%
- CC    = 14% - 26%
- C     = 2% - 14%
- D     = 0% - 2%

Rating = Points
- AAA   = 15,68 - 16
- AA    = 13,76 - 15,68
- A     = 11,84 - 13,76
- BBB   = 9,92 - 11,84
- BB    = 8,00 - 9,92
- B     = 6,08 - 8,00
- CCC   = 4,16 - 6,08
- CC    = 2,24 - 4,16
- C     = 0,32 - 2,24
- D     = 0 - 0,32

Therefore following will be used:

Rating  = Points
- AAA   = 15 - 16
- AA    = 13 - 15
- A     = 11 - 13
- BBB   = 9 - 11
- BB    = 8 - 9
- B     = 6 - 8
- CCC   = 4 - 6
- CC    = 2 - 4
- C     = 1 - 2
- D     = 0 - 1
