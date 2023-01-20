
#Function used to print the prompts
function prints(){
    cls
    Write-Output "**********WRITE EXIT TO TERMINATE SCRIPT*********"
    Write-Output "1.`t Update Computer"
    Write-Output "2.`t Change Computer Settings"
    Write-Output "3.`t Install Automate Agent"
    Write-Output "4.`t Turn Off Windows Defender"
    Write-Output "5.`t Change Computer Name"
    Write-Output "6.`t Create LAdmin"
    Write-Output "7.`t Create Helpdesk"
    Write-Output "8.`t Debload"
    Write-Output "9.`t Disk Maintenance"
    Write-Output "10.`t Join Domain"
    Write-Output "11.`t Pull from PDQ"
    #Write-Output "12 `t Delete Script"
}

#Prompts the user for type of computer setup
#Connects to the manual prompts and performs automatic setup
#Automation done calling each function sequentially
function f0(){
    $loop = 1
    while ($loop -eq 1) {
        cls
        Write-Output "WHAT KIND OF SETUP WOULD YOU LIKE TO DO"
        Write-Output "1. Prompts"
        Write-Output "2. Automatic Setup"
        $choice = Read-Host "->"
        if ($choice -eq "exit") {break}
        if ($choice -eq 1) {choice}
        elseif ($choice -eq 2) {
            cls
            
            $loop2 = 1
            while ($loop2 -eq 1){
                write-output "What kind of device will it be"
                Write-Output "1. Domain Device `t | Update | Settings | Automate | Defender | Computer Name | Debloat | Disk Management | Domain | Helpdesk" 
                write-output "2. Non Domain Device `t | Update | Settings | Automate | Defender | Computer Name | Debloat | Disk Management | Ladmin" 
                $choice2 = Read-Host "->"
            
                if ($choice2 -eq 1) {
                f1
                f2
                f4
                f8
                f9
                f5
                f7
                f10
                f3
                $loop2 = 0
                }
                if ($choice2 -eq 2) {
                f1
                f2
                f4
                f8
                f9
                f5
                f6
                f3
                $loop2=0
                }
                if ($choice2 -eq "exit") {break}
            }
        }
        elseif ($choice -eq "exit") {
        $loop=0
        break
        }
    }
}

#Routes the user to either the type of setup
#Prompts the user to activate enable the powershell exception policy
function f1(){
    cls
    write-host "BEFORE PROCEEDING, ENSURE POWERSHELL SCRIPTING IS TURNED ON" -ForegroundColor Red -BackgroundColor Black
    write-host "SCROLL DOWN ON THE WINDOWS PAGE AND CLICK ACCEPT" -ForegroundColor Red -BackgroundColor Black
    pause
    Start-Process ms-settings:developers -
    echo "starting windows settings"
    Read-Host "Press Enter to begin"
    cls
    
    $loop=1
    while($loop -eq 1){
    cls
    Write-Output "WHAT TYPE OF UPDATE. "
    Write-Output "1.`t Windows Updates Only"
    Write-Output "2.`t Manufacturer Updates Only"
    Write-Output "3.`t BOTH"
    $utype = Read-Host "->`t "
    
        if ($utype -eq 1){f1v2
        $loop=0}
        elseif ($utype -eq 2){f1v1
        $loop=0}
        elseif ($utype -eq 3){
        f1v2
        f1v1
        $loop=0}
        elseif ($utype -eq "exit"){
        $loop=0
        break}
   }
}

#Performs manufacturer updates based on the manufacturer of the computer
function f1v1(){

    $mf = wmic bios get manufacturer | Out-String
    $lenovo="LENOVO"
    $hp="HP"
    $hp2="Hewlett-Packard"
    if ($mf.Contains($hp)){
        
        wget https://hpia.hpcloud.hp.com/downloads/hpia/hp-hpia-5.1.5.exe -UseBasicParsing -OutFile "HP_Image_Assistant.exe" 
        ./"HP_Image_assistant.exe"
    }
    elseif ($mf.Contains($lenovo)){
        
        wget https://download.lenovo.com/pccbbs/thinkvantage_en/system_update_5.07.0136.exe -UseBasicParsing -OutFile "Lenovo_System_Update.exe" 
        ./"lenovo_system_update.exe"
        }
    elseif ($mf.Contains($hp2)){
        
        #wget https://hpia.hpcloud.hp.com/downloads/hpia/hp-hpia-5.1.5.exe -UseBasicParsing -OutFile "HP_Image_Assistant.exe"
        #./"HP_Image_assistant.exe"
        }
    else {
    Write-Output "looking for $val"
    Write-Output "DOES NOT MATCH BECAUSE |$mfr|----------|$mf|"
        pause
    }
}

#Performs windows updates
function f1v2 (){

    start powershell {


        Set-PSRepository -Name 'PSGallery' -InstallationPolicy Trusted
        Install-PackageProvider -name NuGet -Force
        Install-Module PSWindowsUpdate 
	    Get-WindowsUpdate -AcceptAll
	    Install-WindowsUpdate 
    }
  
}

#Disables certain power functions and changes other computer settings
function f2(){
    powercfg.exe /hibernate off
    powercfg.exe /h off
    powercfg /x -hibernate-timeout-ac 0
    powercfg /x -hibernate-timeout-dc 0
    powercfg /x -disk-timeout-ac 0
    powercfg /x -disk-timeout-dc 0
    powercfg /x -monitor-timeout-ac 0
    powercfg /x -monitor-timeout-dc 0
    Powercfg /x -standby-timeout-ac 0
    powercfg /x -standby-timeout-dc 0

    netsh advfirewall firewall set rule group="remote desktop" new enable=yes
    reg add "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f

    set-timezone -Id "Eastern Standard Time"
}

#Executes tha autoamte agent locally installed on to the computer
function f3(){
    ./"automate agent.msi"
                                                                                                               
}

#Turns off all windows defender
function f4(){
    netsh advfirewall set allprofiles state off
}


#Prompts the user and routes to the desired type of computer name change
function f5(){

    $loop2=1
    while ($loop2=1){
        cls
        Write-Output "TYPE OF COMPUTER NAME CHANGE"
        Write-Output "1. CUSTOM"
        Write-Output "2. Prompted"
        $choice = read-host "->`t"
        if ($choice -eq 1){
            $loop2=0
            f5v2   
            break
        }
        elseif ($choice -eq 2){
            $loop2=0
            f5v1
            break
        }
        elseif ($choice -eq "exit"){
        $loop=0
        break}
    }

    $loop=1

    while ($loop = 1){
        cls
        Write-host "WOULD YOU LIKE TO REBOOT THE MACHINE Y/N" -ForegroundColor Red -BackgroundColor Black
        $restart = Read-Host "-> `t"
        if ($restart.ToLower() -eq "y"){Restart-Computer -Confirm}
        elseif ($restart.ToLower() -eq "yes"){Restart-Computer -Confirm}
        elseif ($restart.ToLower() -eq "n"){
        $loop=0
        break}
        elseif ($restart.ToLower() -eq "no"){
        $loop=0
        break}
        elseif ($restart.ToLower() -eq "exit"){
        $loop=0
        break}
    }

            
}

#Prompts the user for for the desired computer name
function f5v1(){
    $serial = [String](get-wmiobject -Class win32_bios | select SerialNumber)
    $sn = $serial.Substring($serial.Length - 4,3)
    $loop = 1

    while ($loop -eq 1){
        cls
        $num=0
        Write-Output "Is the computer a Desktop(1) or Laptop(2)"
        $machine = @(0,0)
        $machine[0]= 'D'
        $machine[1]= 'L'
        foreach ($a in $machine){
            $num++
            write-output "$num. $a"
        }
    
    $machinenum = Read-Host "Is the machine a Desktop or Laptop"
    if ($machinenum -eq 1) {$loop = 0}
    elseif ($machinenum -eq 2 ) {$loop = 0}
    elseif ($machinenum -eq "exit"){
    $loop=0
    break}
    }

    $loop=1
    while ($loop -eq 1){
        cls
        $num=0
        $lct = @(0,0,0,0,0,0,0,0,0,0,0,0)
        $lct[0]='1400'
        $lct[1]='1339'
        $lct[2]='1350'
        $lct[3]='OGCP'
        $lct[4]='1330'
        $lct[5]='250'
        $lct[6]='111'
        $lct[7]='350'
        $lct[8]='501'
        $lct[9]='FSP'
        $lct[10]='500M'
        $lct[11]='MC'
        foreach ($b in $lct){
            $num++
            write-output "$num. $b"
        }
        $lctnum = Read-Host "Pick A Location`t"
        if ($lctnum -eq 1){$loop=0}
        elseif ($lctnum -eq 2){$loop=0}
        elseif ($lctnum -eq 3){$loop=0}
        elseif ($lctnum -eq 4){$loop=0}
        elseif ($lctnum -eq 5){$loop=0}
        elseif ($lctnum -eq 6){$loop=0}
        elseif ($lctnum -eq 7){$loop=0}
        elseif ($lctnum -eq 8){$loop=0}
        elseif ($lctnum -eq 9){$loop=0}
        elseif ($lctnum -eq 10){$loop=0}
        elseif ($lctnum -eq 11){$loop=0}
        elseif ($lctnum -eq 12){$loop=0}
        elseif ($lctnum -eq "exit"){break}#################################

    }
    
    $loop=1
    while ($loop -eq 1){
        cls
        $num=0
        $dpt = @(0,0,0,0,0,0,0,0,0,0,0,0,0)
        $dpt[0]='ENG'
        $dpt[1]='ACC'
        $dpt[2]='AEM'
        $dpt[3]='FPA'
        $dpt[4]='FIN'
        $dpt[5]='LEA'
        $dpt[6]='LEG'
        $dpt[7]='NEO'
        $dpt[8]='PRM'
        $dpt[9]='PRP'
        $dpt[10]='RIS'
        $dpt[11]='IT'
        $dpt[12]='HR'
        foreach ($c in $dpt){
            $num++
            write-output "$num. $c"
        }
    
    $dptnum = Read-Host "Pick A Department"
    if ($dptnum -eq 1){$loop=0}
        elseif ($dptnum -eq 2){$loop=0}
        elseif ($dptnum -eq 3){$loop=0}
        elseif ($dptnum -eq 4){$loop=0}
        elseif ($dptnum -eq 5){$loop=0}
        elseif ($dptnum -eq 6){$loop=0}
        elseif ($dptnum -eq 7){$loop=0}
        elseif ($dptnum -eq 8){$loop=0}
        elseif ($dptnum -eq 9){$loop=0}
        elseif ($dptnum -eq 10){$loop=0}
        elseif ($dptnum -eq 11){$loop=0}
        elseif ($dptnum -eq 12){$loop=0}
        elseif ($dptnum -eq 13){$loop=0}
        elseif ($dptnum -eq "exit") {break}
    }

    $loop=1
    while ($loop -eq 1){
        cls
        $num=0
        $lcl = @(0,0,0,0)
        $lcl[0]=1
        $lcl[1]=2
        $lcl[2]=3
        $lcl[3]=4
        foreach ($d in $lcl){
            $num++
            write-output "$num. $d"
        }
        $lclnum = Read-Host "Pick its Life Cycle"
        if ($lclnum -eq 1) {$loop = 0}
        elseif ($lclnum -eq 2) {$loop=0}
        elseif ($lclnum -eq 3) {$loop=0}
        elseif ($lclnum -eq 4) {$loop=0}
    }
    cls
    $mch = $machine[$machinenum-1]
    $location = $lct[$lctnum-1]
    $department = $dpt[$dptnum-1]
    $cycle = $lcl[$lclnum-1]

    if ($lclnum -eq 1){$compname = "$mch$location$department$sn"}
    else{$compname = "$mch$location$department$cycle$sn"}
    $oldname = [system.net.dns]::gethostname()
    $check = Read-Host "You are about to change the name from | $oldname | to | $compname | Are you sure? (Y/N)"
    if ($check -eq "y") {Write-Output "Name changed"
    Rename-Computer -NewName $compname}
    elseif ($check -eq "Y") {Write-Output "Name changed"
    Rename-Computer -NewName $compname}
    elseif ($check -eq "yes") {Write-Output "Name changed"
    Rename-Computer -NewName $compname}
    elseif ($check -eq "YES") {Write-Output "Name changed"
    Rename-Computer -NewName $compname}
    elseif ($check -eq "n") {Write-Output "Name NOT changed"}
    elseif ($check -eq "N") {Write-Output "Name NOT changed"}
    elseif ($check -eq "No") {Write-Output "Name NOT changed"}
    elseif ($check -eq "NO") {Write-Output "Name NOT changed"}
    elseif ($check -eq "exit") {break}
    pause
   

}

#Custom name change
function f5v2(){
    cls
    $loop=1
    while ($loop=1){
        cls
        write-output "**********CUSTOM NAME CHANGE**********"
        $compname = read-host "Enter Custom Computer Name"
        if ($compname -eq "exit") {break}
        $compname2 = read-host "Confirm Custom Computer Name"
        if ($compname2 -eq "exit") {break}
        if ($compname -eq $compname2){
        $loop=0
        break
        write-output "Computer names matched"
        }
        elseif ($compname -ne $compname2){
        Write-Output "The computernames do not match"
        }
        pause
    }

    $oldname = [system.net.dns]::gethostname()
    $check = Read-Host "You are about to change the name from | $oldname | to | $compname | Are you sure?"
    if ($check -eq "y") {Write-Output "Name changed"
    Rename-Computer -NewName $compname
    }
    elseif ($check -eq "Y") {Write-Output "Name changed"
    Rename-Computer -NewName $compname
    }
    elseif ($check -eq "yes") {Write-Output "Name changed"
    Rename-Computer -NewName $compname
    }
    elseif ($check -eq "YES") {Write-Output "Name changed"
    Rename-Computer -NewName $compname
    }
    elseif ($check -eq "n") {Write-Output "Name NOT changed"}
    elseif ($check -eq "N") {Write-Output "Name NOT changed"}
    elseif ($check -eq "No") {Write-Output "Name NOT changed"}
    elseif ($check -eq "NO") {Write-Output "Name NOT changed"}
    elseif ($check -eq "exit") {break}

}

function f6(){

    try{
        Rename-LocalUser -Name "Administrator" -NewName "ladmin" -ErrorAction Stop
        net user ladmin /active:yes
        Write-Output "Administrator has been turned into Ladmin"
        $pw1 = Read-Host "Enter a password for Ladmin" -AsSecureString
        $account = Get-LocalUser -Name "ladmin"
        $account | Set-LocalUser -Password $pw1
        Write-Output "Password Saved"
        pause
        }
    catch{
        $loop=1
        while ($loop -eq 1){
            cls
            $pwchg = Read-Host "Ladmin Already exists. Would you like to change the password (Y/N)?`t"
            if ($pwchg.ToLower() -eq "y") {$pw = Read-Host "Enter a new password for Helpdesk" -AsSecureString
                $pw = Read-Host "Enter new Password`t"    
                $account = Get-LocalUser -Name "Ladmin"
                $account | Set-LocalUser -Password $pw
                $loop=0}
            elseif ($pwchg.ToLower() -eq "n") {$loop=0}
        }
    }
        
}

function f7(){

    try{
        New-Localuser -Name "Helpdesk" -ErrorAction Stop
        Write-Output "Account Created"
        pause}
    catch{
        $loop=1
        while ($loop -eq 1){
            cls
            $pwchg = Read-Host "Helpdesk Already exists. Would you like to change the password (Y/N)?`t"
            if ($pwchg.ToLower() -eq "y") {$pw = Read-Host "Enter a new password for Helpdesk" -AsSecureString
                $pw = Read-Host "Enter new Password`t"    
                $account = Get-LocalUser -Name "Helpdesk"
                $account | Set-LocalUser -Password $pw
                $loop=0}
            elseif ($pwchg.ToLower() -eq "n") {$loop=0}
        }
    }

    try{Add-LocalGroupMember -Group "Administrators" -Member "Helpdesk" -ErrorAction Stop
        Write-Output "Helpdesk has been elevated to an Administrator"}
    catch{Write-Output "Helpdesk is already an Administrator"}
    pause



   
}

function f8(){
    start powershell {
        Set-ExecutionPolicy Bypass
        ./"Windows10Debloater.ps1"
    }
}

function f9(){
    start powershell {
        Write-Output "STARTING DEFRAG"
        defrag C: /U}
    start powershell {cleanmgr}
    start powershell {
        echo "STARTING SCANNOW"
        sfc /scannow}
}

function f10(){
    add-computer -domainname esbnyc.local
}

function f11(){
    
}



function f12v1(){
    try{
        Remove-Item $env:PUBLIC\POWERPREP -Recurse
        Write-Output "folder deleted"
        }
    catch{
        Write-Output "The folder does not exist"
        }
}

function f12v2(){
    cls
    $loop=1
    while ($loop -eq 1){
        $ans = Read-Host "Are you sure you want to delete the script? This will terminate the session(Y/N)?`t"
        if ($ans.ToLower() -eq "y"){
            $loop=0
            ./Terminate.ps1
            Write-Output "Terminating"
            sleep 1
            exit
            }

        elseif ($ans.ToLower() -eq "n"){
            $loop=0
            Write-Output "Script not deleted"}
    }
    pause
}

function choice(){
    
    $loop = 1
    while ($loop -eq 1){
        prints
        $choice = Read-Host "Pick an option `t"
        if ($choice -eq 1) {f1}
        elseif ($choice -eq 2) {f2}
        elseif ($choice -eq 3) {f3}
        elseif ($choice -eq 4) {f4}
        elseif ($choice -eq 5) {f5}
        elseif ($choice -eq 6) {f6}
        elseif ($choice -eq 7) {f7}
        elseif ($choice -eq 8) {f8}
        elseif ($choice -eq 9) {f9}
        elseif ($choice -eq 10) {f10}
        elseif ($choice -eq 11) {f11}
        #elseif ($choice -eq 12) {f12v2}
        elseif ($choice -eq "exit") {$loop = 0}
    }
    

}

#This script will prompt the user for admin privileges/credentials
#When credentials are entered, it switch the current directory to the the admin users home directory
#Hense the purpose of changing directories to a folder found on every machine
cls
try{
    #$var = pwd
    cd $env:PUBLIC\"POWERPREP" -ErrorAction Stop
    #cd $var
    }
catch{
    cp ..\POWERPREP -Recurse -Destination $env:PUBLIC 
    }

#prompts the user for admin credentials if the script was not started as an administrator
If (!([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]'Administrator')) {
    Write-Host "You didn't run this script as an Administrator. This script will self elevate to run as an Administrator and continue."
    Start-Sleep 1
    Write-Host "                                               3" -ForegroundColor Red
    Start-Sleep 1
    Write-Host "                                               2" -ForegroundColor Yellow
    Start-Sleep 1
    Write-Host "                                               1" -ForegroundColor Green
    Start-Sleep 1
    Start-Process powershell.exe -ArgumentList ("-NoProfile -ExecutionPolicy Bypass -File `"{0}`"" -f $PSCommandPath) -Verb RunAs
    Exit
}

f0