#!/bin/bash -x

map=${1}
seshname=${2}
port=${3}
query=${4}
rcon=${5}
adminpass=${6}
pass=${7}
playercount=${8}
difficulty=${9}
officialdifficulty=${10}

steamcmd +force_install_dir ./ark +login anonymous +app_update 376030 +quit

screen -dmS ark ~/util/arkserverdirectory/ShooterGame/Binaries/Linux/ShooterGameServer ${map}?listen?Multihome=0.0.0.0?SessionName=${seshname}?MaxPlayers=${playercount}?QueryPort=${query}?RCONPort=${rcon}?Port=${port}?ServerAdminPassword=${adminpass}?ServerPassword=${pass}?DifficultyOffset=${difficulty}?OverrideOfficialDifficulty=${officialdifficulty} -server -log -noantispeedhack -automanagedmods -ForceRespawnDinos
