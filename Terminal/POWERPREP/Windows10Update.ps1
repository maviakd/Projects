$mf = wmic bios get manufacturer
    $mfr = $mf.Split()[4]
    if ($mfr -eq "HP"){
        wget https://hpia.hpcloud.hp.com/downloads/hpia/hp-hpia-5.1.5.exe -UseBasicParsing -OutFile "HP_Image_Assistant.exe"
        ./"HP_Image_assistant.exe"
    }
    elseif ($mfr -eq "LENOVO"){
        wget https://download.lenovo.com/pccbbs/thinkvantage_en/system_update_5.07.0136.exe -UseBasicParsing -OutFile "Lenovo_System_Update.exe"
        ./"Lenovo_System_Update.exe"}
    
    else {Write-Output "DOES NOT MATCH"
        pause
    }