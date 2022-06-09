;= @echo off
;= rem Call DOSKEY and use this file as the macrofile
;= %SystemRoot%\system32\doskey /listsize=1000 /macrofile=%0%
;= rem In batch mode, jump to the end of the file
;= goto:eof
;= Add aliases below here
cd~=cd /d %userprofile%
cdkivy=cd /d D:\Documents\kivyenv
e.=explorer .
gl=git log --oneline --all --graph --decorate  $*
ls=ls --show-control-chars -F --color $*
ll=ls -al
pwd=cd
history=cat -n "%CMDER_ROOT%\config\.history"
unalias=alias /d $1
; user_profile.cmd
; set vim = %programfiles%...
cmderr=cd /d "%CMDER_ROOT%"
