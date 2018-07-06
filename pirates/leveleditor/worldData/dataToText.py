# uncompyle6 version 3.2.3
# Python bytecode 2.4 (62061)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: C:\Cygwin\home\piratepub\player_pirates_1_0_33QA\pirates\src\leveleditor\worldData\dataToText.py
import direct, sys
dataFileName = sys.argv[1]
textFileName = sys.argv[2]
dataModule = dataFileName.split('.py')[0]
print 'Parsing %s.py --> %s\n' % (dataModule, textFileName)
exec 'from pirates.leveleditor.worldData.%s import *' % dataModule
lines = []
for mainUid in objectStruct['Objects']:
    mainObj = objectStruct['Objects'][mainUid]
    lines.append('Name:\t%s\t%s\nType:\t%s\n\n' % (mainObj['Name'], mainUid, mainObj['Type']))
    for uid in mainObj['Objects']:
        object = mainObj['Objects'][uid]
        lines.append('%s\t%s\t%s\n' % (uid, object['Type'], `(object['Pos'])`))

    lines.append('\n')

textFile = file(textFileName, 'w')
textFile.writelines(lines)
textFile.close()