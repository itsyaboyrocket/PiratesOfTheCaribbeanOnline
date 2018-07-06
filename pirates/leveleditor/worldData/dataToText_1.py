# uncompyle6 version 3.2.3
# Python bytecode 2.4 (62061)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: C:\Cygwin\home\piratepub\player_pirates_1_0_33QA\pirates\src\leveleditor\worldData\dataToText_1.py
import direct, sys
dataFileName = sys.argv[1]
dataModule = dataFileName.split('.py')[0]
textFileName = dataModule + '.txt'
print 'Parsing %s.py --> %s\n' % (dataModule, textFileName)
exec 'from pirates.leveleditor.worldData.%s import *' % dataModule
lines = []
for mainUid in objectStruct['Objects']:
    mainObj = objectStruct['Objects'][mainUid]
    lines.append('Name:\t%s\t%s\nType:\t%s\n\n' % (mainObj['Name'], mainUid, mainObj['Type']))

def printObjects(obj):
    for uid in obj['Objects']:
        object = obj['Objects'][uid]
        line = ''
        if object['Type'] == 'Player Spawn Node':
            pass
        else:
            if object['Type'] == 'Spawn Node':
                line = '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (dataModule, obj['Type'], uid, object['Type'], object['Spawnables'], object['Team'], object['Min Population'], `(object['Pos'])`)
            else:
                if object['Type'] == 'Object Spawn Node':
                    line = '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (dataModule, obj['Type'], uid, object['Type'], object['Spawnables'], object['SpawnDelay'], object['startingDepth'], `(object['Pos'])`)
                else:
                    if object['Type'] == 'Searchable Container':
                        line = '%s\t%s\t%s\t%s\t%s\t%s\t\t%s\n' % (dataModule, obj['Type'], uid, object['Type'], object['type'], object['searchTime'], `(object['Pos'])`)
                    else:
                        if object['Type'] == 'Townsperson':
                            line = '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (dataModule, obj['Type'], uid, object['Type'], object['Category'], object['Start State'], object['Team'], `(object['Pos'])`)
                        else:
                            if 'Objects' in object:
                                printObjects(object)
        lines.append(line)


lines.append('\n')
for mainUid in objectStruct['Objects']:
    mainObj = objectStruct['Objects'][mainUid]
    printObjects(mainObj)

textFile = file(textFileName, 'w')
textFile.writelines(lines)
textFile.close()