#include <GUIConstants_x.au3>

Global $DownPath = "http://sdeveci.com/sductf/flagctf.txt", $CongFile = @TempDir & "flagctf.txt"

$DownStat = InetGet($DownPath, @TempDir & "\flagctf.txt", 1, 0);Background

If Not $DownStat Then
	MsgBox(64, "", "HATA!")
	Exit
Else
	MsgBox(64, "", "Where ?")
EndIf
