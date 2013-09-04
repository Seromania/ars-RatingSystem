REM  *****  BASIC  *****

Sub Main
Dim I as Integer
myDoc = thisComponent
mySheet = myDoc.sheets(0)

for I = 0 to 150
   zelle = mySheet.getCellByPosition(1,I)
   if zelle.string = "AAA" then
   		bereich = mySheet.getCellByPosition(0,I)
   		bereich.CellBackColor = &H1f4c21
   		bereich = mySheet.getCellByPosition(1,I)
   		bereich.CellBackColor = &H1f4c21
		
   elseif zelle.string = "AA+" then
   		bereich = mySheet.getCellByPosition(0,I)
   		bereich.CellBackColor = &H2E7331
   		bereich = mySheet.getCellByPosition(1,I)
   		bereich.CellBackColor = &H2E7331	
   elseif zelle.string = "AA" then
   		bereich = mySheet.getCellByPosition(0,I)
   		bereich.CellBackColor = &H2E7331
   		bereich = mySheet.getCellByPosition(1,I)
   		bereich.CellBackColor = &H2E7331
   elseif zelle.string = "AA-" then
   		bereich = mySheet.getCellByPosition(0,I)
   		bereich.CellBackColor = &H2E7331
   		bereich = mySheet.getCellByPosition(1,I)
   		bereich.CellBackColor = &H2E7331		
   
   elseif zelle.string = "A+" then
   		bereich = mySheet.getCellByPosition(0,I)
   		bereich.CellBackColor = &H3D9941
		bereich = mySheet.getCellByPosition(1,I)
   		bereich.CellBackColor = &H3D9941		
   elseif zelle.string = "A" then
   		bereich = mySheet.getCellByPosition(0,I)
   		bereich.CellBackColor = &H3D9941
		bereich = mySheet.getCellByPosition(1,I)
   		bereich.CellBackColor = &H3D9941
   elseif zelle.string = "A-" then
   		bereich = mySheet.getCellByPosition(0,I)
   		bereich.CellBackColor = &H3D9941
		bereich = mySheet.getCellByPosition(1,I)
   		bereich.CellBackColor = &H3D9941	
   
   elseif zelle.string = "BBB+" then
   		bereich = mySheet.getCellByPosition(0,I)
   		bereich.CellBackColor = &HA16A1A		
   		bereich = mySheet.getCellByPosition(1,I)
   		bereich.CellBackColor = &HA16A1A	
   elseif zelle.string = "BBB" then
   		bereich = mySheet.getCellByPosition(0,I)
   		bereich.CellBackColor = &HA16A1A		
   		bereich = mySheet.getCellByPosition(1,I)
   		bereich.CellBackColor = &HA16A1A
   elseif zelle.string = "BBB-" then
   		bereich = mySheet.getCellByPosition(0,I)
   		bereich.CellBackColor = &HA16A1A		
   		bereich = mySheet.getCellByPosition(1,I)
   		bereich.CellBackColor = &HA16A1A	
   
   elseif zelle.string = "BB+" then
   		bereich = mySheet.getCellByPosition(0,I)
   		bereich.CellBackColor = &HCA8F3B
   		bereich = mySheet.getCellByPosition(1,I)
   		bereich.CellBackColor = &HCA8F3B		
   elseif zelle.string = "BB" then
   		bereich = mySheet.getCellByPosition(0,I)
   		bereich.CellBackColor = &HCA8F3B
   		bereich = mySheet.getCellByPosition(1,I)
   		bereich.CellBackColor = &HCA8F3B	
   elseif zelle.string = "BB-" then
   		bereich = mySheet.getCellByPosition(0,I)
   		bereich.CellBackColor = &HCA8F3B
   		bereich = mySheet.getCellByPosition(1,I)
   		bereich.CellBackColor = &HCA8F3B	
   
   elseif zelle.string = "B+" then
   		bereich = mySheet.getCellByPosition(0,I)
   		bereich.CellBackColor = &HC8A067		
   		bereich = mySheet.getCellByPosition(1,I)
   		bereich.CellBackColor = &HC8A067		
   elseif zelle.string = "B" then
   		bereich = mySheet.getCellByPosition(0,I)
   		bereich.CellBackColor = &HC8A067		
   		bereich = mySheet.getCellByPosition(1,I)
   		bereich.CellBackColor = &HC8A067
   elseif zelle.string = "B-" then
   		bereich = mySheet.getCellByPosition(0,I)
   		bereich.CellBackColor = &HC8A067		
   		bereich = mySheet.getCellByPosition(1,I)
   		bereich.CellBackColor = &HC8A067		
   	
   elseif zelle.string = "CCC+" then
   		bereich = mySheet.getCellByPosition(0,I)
   		bereich.CellBackColor = &Hee4000
   		bereich = mySheet.getCellByPosition(1,I)
   		bereich.CellBackColor = &Hee4000
   elseif zelle.string = "CCC" then
   		bereich = mySheet.getCellByPosition(0,I)
   		bereich.CellBackColor = &Hee4000
   		bereich = mySheet.getCellByPosition(1,I)
   		bereich.CellBackColor = &Hee4000
   elseif zelle.string = "CCC-" then
   		bereich = mySheet.getCellByPosition(0,I)
   		bereich.CellBackColor = &Hee4000
   		bereich = mySheet.getCellByPosition(1,I)
   		bereich.CellBackColor = &Hee4000		
   
   elseif zelle.string = "CC+" then
   		bereich = mySheet.getCellByPosition(0,I)
   		bereich.CellBackColor = &HD40000
   		bereich = mySheet.getCellByPosition(1,I)
   		bereich.CellBackColor = &HD40000		
   elseif zelle.string = "CC" then
   		bereich = mySheet.getCellByPosition(0,I)
   		bereich.CellBackColor = &HD40000
   		bereich = mySheet.getCellByPosition(1,I)
   		bereich.CellBackColor = &HD40000
   elseif zelle.string = "CC-" then
   		bereich = mySheet.getCellByPosition(0,I)
   		bereich.CellBackColor = &HD40000
   		bereich = mySheet.getCellByPosition(1,I)
   		bereich.CellBackColor = &HD40000	
   
   elseif zelle.string = "C+" then
   		bereich = mySheet.getCellByPosition(0,I)
   		bereich.CellBackColor = &HD40000
   		bereich = mySheet.getCellByPosition(1,I)
   		bereich.CellBackColor = &HD40000	
   elseif zelle.string = "C" then
   		bereich = mySheet.getCellByPosition(0,I)
   		bereich.CellBackColor = &HD40000
   		bereich = mySheet.getCellByPosition(1,I)
   		bereich.CellBackColor = &HD40000
   elseif zelle.string = "C-" then
   		bereich = mySheet.getCellByPosition(0,I)
   		bereich.CellBackColor = &HD40000
   		bereich = mySheet.getCellByPosition(1,I)
   		bereich.CellBackColor = &HD40000		
   		
   elseif zelle.string = "D" then
   		bereich = mySheet.getCellByPosition(0,I)
   		bereich.CellBackColor = &H800000
   		bereich = mySheet.getCellByPosition(1,I)
   		bereich.CellBackColor = &H800000	
		
	elseif zelle.string = "NR" then
   		bereich = mySheet.getCellByPosition(0,I)
   		bereich.CellBackColor = vbBlack
   		bereich = mySheet.getCellByPosition(1,I)
   		bereich.CellBackColor = vbBlack
   endif
next I

for I=7 to 17
 zelle = mySheet.getCellByPosition(3,I)
   if zelle.string = "AAA" then
   		bereich = mySheet.getCellByPosition(3,I)
   		bereich.CellBackColor = &H1f4c21
		bereich = mySheet.getCellByPosition(4,I)
   		bereich.CellBackColor = &H1f4c21
   		
   elseif zelle.string = "AA" then
   		bereich = mySheet.getCellByPosition(3,I)
   		bereich.CellBackColor = &H2E7331
   		bereich = mySheet.getCellByPosition(4,I)
   		bereich.CellBackColor = &H2E7331		
   		
   elseif zelle.string = "A" then
   		bereich = mySheet.getCellByPosition(3,I)
   		bereich.CellBackColor = &H3D9941
		bereich = mySheet.getCellByPosition(4,I)
   		bereich.CellBackColor = &H3D9941		
   		
   elseif zelle.string = "BBB" then
   		bereich = mySheet.getCellByPosition(3,I)
   		bereich.CellBackColor = &HA16A1A		
   		bereich = mySheet.getCellByPosition(4,I)
   		bereich.CellBackColor = &HA16A1A
   				
   elseif zelle.string = "BB" then
   		bereich = mySheet.getCellByPosition(3,I)
   		bereich.CellBackColor = &HCA8F3B
   		bereich = mySheet.getCellByPosition(4,I)
   		bereich.CellBackColor = &HCA8F3B	
   		
   elseif zelle.string = "B" then
   		bereich = mySheet.getCellByPosition(3,I)
   		bereich.CellBackColor = &HC8A067		
   		bereich = mySheet.getCellByPosition(4,I)
   		bereich.CellBackColor = &HC8A067
   			
   elseif zelle.string = "CCC" then
   		bereich = mySheet.getCellByPosition(3,I)
   		bereich.CellBackColor = &Hee4000
   		bereich = mySheet.getCellByPosition(4,I)
   		bereich.CellBackColor = &Hee4000		
   	
   elseif zelle.string = "CC" then
   		bereich = mySheet.getCellByPosition(3,I)
   		bereich.CellBackColor = &HD40000
   		bereich = mySheet.getCellByPosition(4,I)
   		bereich.CellBackColor = &HD40000		
		
   elseif zelle.string = "C" then
   		bereich = mySheet.getCellByPosition(3,I)
   		bereich.CellBackColor = &HD40000
   		bereich = mySheet.getCellByPosition(4,I)
   		bereich.CellBackColor = &HD40000		
   		
   elseif zelle.string = "D" then
   		bereich = mySheet.getCellByPosition(3,I)
   		bereich.CellBackColor = &H800000
   		bereich = mySheet.getCellByPosition(4,I)
   		bereich.CellBackColor = &H800000	
   	
   elseif zelle.string = "NR" then
   		bereich = mySheet.getCellByPosition(3,I)
   		bereich.CellBackColor = vbBlack
   		bereich = mySheet.getCellByPosition(4,I)
   		bereich.CellBackColor = vbBlack
   		
   endif
next I
End Sub