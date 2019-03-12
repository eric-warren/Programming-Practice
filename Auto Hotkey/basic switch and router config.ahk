Numpad4::
 {
	Gui, Font, cBlack
	Gui, Add, Button, gRouter, Router
	Gui, Add, Button, gSWitch, Switch
	Gui, +AlwaysOnTop
	Gui, Show, ConfigIP?
	return

	Router:
	Gui Destroy
	InputBox, Num, What Router Number?
	Device := "R"
	Gui Destroy
	main(Device, Num)
	return
	Switch:
	Gui Destroy
	InputBox, Num, What Switch Number?
	Device := "S"
	Gui Destroy
	Main(Device, Num)
	return

Main(Device, Num){
	Send, enable
	Send, {Enter}
    	Sleep, 50
	Send, Configure Terminal
	Send, {Enter}
    	Sleep, 50
	Send, hostname warr0181-%Device%%Num%
	Send, {Enter}
    	Sleep, 50
	Send, enable secret class
	Send, {Enter}
    	Sleep, 50
	Send, banner motd "NO UNAUTHORIZED ACCESS Warr0181"
	Send, {Enter}
    	Sleep, 50
	Send, line console 0
	Send, {Enter}
    	Sleep, 50
	Send, password cisco
	Send, {Enter}
    	Sleep, 50
	Send, login
	Send, {Enter}
    	Sleep, 50
	Send, exit
	Send, {Enter}
    	Sleep, 50
	Send, line vty 0 4
	Send, {Enter}
    	Sleep, 50
	Send, password cisco
	Send, {Enter}
    	Sleep, 50
	Send, login
	Send, {Enter}
    	Sleep, 50
	Send, exec-timeout 15
	Send, {Enter}
    	Sleep, 50
	Send, exit
	Send, {Enter}
    	Sleep, 50
	Send, no logging console
	Send, {Enter}
    	Sleep, 50
	Send, no ip domain-lookup
	Send, {Enter}
    	Sleep, 50
	Send, line console 0
	Send, {Enter}
    	Sleep, 50
	Send, exec-timeout 15
	Send, {Enter}
    	Sleep, 50
	Send, exit
	Send, {Enter}
    	Sleep, 50
	RouterGui()

RouterGui(){
	Gui, Font, cBlack
	Gui, Add, Button, gConfigIP, Configure IPs
	Gui, Add, Button, gSkipConfigIP, Do Not
	Gui, +AlwaysOnTop
	Gui, Show, ConfigIP?
	return

ConfigIP:
Int := "Default"
Gui Destroy
InputBox, Int, Enter desired interface
Send, Interface %int%
Send, {Enter}
InputBox, IP, Enter desired IP for interface %Int%
InputBox, Mask, Enter desired Subnet-mask for interface %Int%
Send, Ip Address %IP% %Mask%
Send, {Enter}
Sleep, 50
Send, No Shutdown
Send, {Enter}
Sleep, 50
Send, Exit
Send, {Enter}
Sleep, 50
MyGui()
	return
SkipConfigIP:
Gui Destroy
	return
}
}
