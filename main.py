#!/usr/bin/env python
import subprocess
from datetime import datetime
from lib.ArkSession import ArkSession
from lib.Helper import Helper

def main():
    path = "config.ini"
    
    session = ArkSession(path)
    session.load()

    current_date = datetime.now()

    # Check if we should reset date before we do any maths.
    if Helper.to_bool(session.reset):
        start_date = datetime.strptime(session.startdate, '%Y-%m-%d %I:%M:%S')
        session.reset = "False"
        session.startdate = current_date.strftime('%Y-%m-%d %I:%M:%S')
        session.save()

    if Helper.to_bool(session.enabled):
        start_date = datetime.strptime(session.startdate, '%Y-%m-%d %I:%M:%S')
        duration = ((current_date - start_date).total_seconds() / 86400) #days
        difficulty = Helper.clamp((float(session.difficultystart) + (duration * float(session.timescalar) * float(session.difficultyperday))), 0.0, float(session.difficultymax))
        subprocess.run(["./launch.sh", str(session.map),  '"' + str(session.servertitle) + '"', '' + str(session.gameclientport) + '', '' + str(session.queryport) + '', '' + str(session.rconport) + '', '' + str(session.adminpass) + '', '' + str(session.password) + '', '' + str(session.playercount) + '', '' + str(session.difficulty) + '', '' + "{:.1f}".format(difficulty) + ''])    
    else:
        subprocess.run(["./launch.sh", str(session.map),  '"' + str(session.servertitle) + '"', '' + str(session.gameclientport) + '', '' + str(session.queryport) + '', '' + str(session.rconport) + '', '' + str(session.adminpass) + '', '' + str(session.password) + '', '' + str(session.playercount) + '', '' + str(session.difficulty) + '', '' + str(session.officialdifficulty) + ''])


if __name__ == '__main__':
    main()