# uncompyle6 version 3.2.3
# Python bytecode 2.4 (62061)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: C:\Cygwin\home\piratepub\player_pirates_1_0_33QA\pirates\src\leveleditor\worldData\del_fuego_area_cave_c_1.py
from pandac.PandaModules import Point3, VBase3, Vec4
objectStruct = {'Objects': {'1164929110.98sdnaik': {'Type': 'Island Game Area', 'Name': 'del_fuego_area_cave_c_1', 'File': '', 'Instanced': True, 'Minimap': False, 'Objects': {'1164930102.27sdnaik': {'Type': 'Locator Node', 'Name': 'portal_interior_1', 'Hpr': VBase3(57.196, 0.0, 0.0), 'Pos': Point3(-148.822, -121.561, 26.647), 'Scale': VBase3(1.0, 1.0, 1.0)}, '1164930102.28sdnaik': {'Type': 'Locator Node', 'Name': 'portal_interior_2', 'Hpr': VBase3(178.366, 0.0, 0.0), 'Pos': Point3(162.003, -10.773, 2.083), 'Scale': VBase3(1.0, 1.0, 1.0)}, '1176238208.0dxschafe': {'Type': 'Spawn Node', 'Aggro Radius': '12.0000', 'AnimSet': 'gp_chant_a', 'Hpr': VBase3(137.437, 0.0, 0.0), 'Min Population': '1', 'Patrol Radius': '12.0000', 'Pause Chance': 100, 'Pause Duration': 30, 'Pos': Point3(24.46, 39.593, 0.069), 'PoseAnim': '', 'PoseFrame': '', 'Scale': VBase3(1.0, 1.0, 1.0), 'Spawnables': 'Skel T5', 'Start State': 'Patrol', 'StartFrame': '0', 'Team': 'default', 'TrailFX': 'None', 'VisSize': '', 'Visual': {'Color': (0, 0, 0.65, 1), 'Model': 'models/misc/smiley'}}, '1176238208.0dxschafe0': {'Type': 'Spawn Node', 'Aggro Radius': '12.0000', 'AnimSet': 'gp_chant_b', 'Hpr': VBase3(8.215, 0.0, 0.0), 'Min Population': '1', 'Patrol Radius': '12.0000', 'Pause Chance': 100, 'Pause Duration': 30, 'Pos': Point3(16.455, 18.41, 0.069), 'PoseAnim': '', 'PoseFrame': '', 'Scale': VBase3(1.0, 1.0, 1.0), 'Spawnables': 'Skel T5', 'Start State': 'Patrol', 'StartFrame': '0', 'Team': 'default', 'TrailFX': 'None', 'VisSize': '', 'Visual': {'Color': (0, 0, 0.65, 1), 'Model': 'models/misc/smiley'}}, '1176238208.0dxschafe1': {'Type': 'Player Spawn Node', 'Hpr': VBase3(85.413, 0.0, 0.0), 'Index': -1, 'Pos': Point3(69.237, 2.171, 0.069), 'Scale': VBase3(1.0, 1.0, 1.0), 'Spawnables': 'All', 'Visual': {'Color': (0.5, 0.5, 0.5, 1), 'Model': 'models/misc/smiley'}}, '1176239104.0dxschafe': {'Type': 'Spawn Node', 'Aggro Radius': '12.0000', 'AnimSet': 'gp_searching', 'Hpr': Point3(0.0, 0.0, 0.0), 'Min Population': '1', 'Patrol Radius': '7.7530', 'Pause Chance': '23', 'Pause Duration': '97', 'Pos': Point3(-111.72, -53.65, 24.74), 'PoseAnim': '', 'PoseFrame': '', 'Scale': VBase3(1.0, 1.0, 1.0), 'Spawnables': 'Dread Scorpion', 'Start State': 'Ambush', 'StartFrame': '0', 'Team': 'default', 'TrailFX': 'None', 'VisSize': '', 'Visual': {'Color': (0, 0, 0.65, 1), 'Model': 'models/misc/smiley'}}, '1188602752.0dxschafe': {'Type': 'Player Spawn Node', 'Hpr': VBase3(85.413, 0.0, 0.0), 'Index': -1, 'Pos': Point3(79.135, 58.949, 0.069), 'Scale': VBase3(1.0, 1.0, 1.0), 'Spawnables': 'All', 'VisSize': '', 'Visual': {'Color': (0.5, 0.5, 0.5, 1), 'Model': 'models/misc/smiley'}}, '1188602752.0dxschafe0': {'Type': 'Player Spawn Node', 'Hpr': VBase3(85.413, 0.0, 0.0), 'Index': -1, 'Pos': Point3(110.414, -27.524, 0.077), 'Scale': VBase3(1.0, 1.0, 1.0), 'Spawnables': 'All', 'Visual': {'Color': (0.5, 0.5, 0.5, 1), 'Model': 'models/misc/smiley'}}, '1189033600.0dchiappe': {'Type': 'Light - Dynamic', 'Attenuation': '0.005', 'ConeAngle': '60.0000', 'DropOff': '0.0000', 'FlickRate': '0.0964', 'Flickering': False, 'Hpr': VBase3(0.0, 1.968, 0.0), 'Intensity': '1.3735', 'LightType': 'POINT', 'Pos': Point3(-60.328, -27.47, 65.808), 'Scale': VBase3(1.0, 1.0, 1.0), 'Visual': {'Color': (1.0, 0.2, 0.0, 1.0), 'Model': 'models/props/light_tool_bulb'}}, '1189033600.0dchiappe0': {'Type': 'Light - Dynamic', 'Attenuation': '0.005', 'ConeAngle': '60.0000', 'DropOff': '0.0000', 'FlickRate': '0.5000', 'Flickering': False, 'Hpr': Point3(0.0, 0.0, 0.0), 'Intensity': '1.0120', 'LightType': 'POINT', 'Pos': Point3(107.938, 64.026, 31.319), 'Scale': VBase3(1.0, 1.0, 1.0), 'Visual': {'Color': (1.0, 0.36, 0.39, 1.0), 'Model': 'models/props/light_tool_bulb'}}, '1189033728.0dchiappe': {'Type': 'Effect Node', 'EffectName': 'bonfire_effect', 'Hpr': Point3(0.0, 0.0, 0.0), 'Pos': Point3(16.178, 31.787, 0.0), 'Scale': VBase3(0.641, 0.641, 0.641), 'Visual': {'Color': (0.0, 1.0, 0.0, 1.0), 'Model': 'models/misc/smiley'}}, '1189033856.0dchiappe': {'Type': 'Spawn Node', 'Aggro Radius': '12.0000', 'AnimSet': 'gp_summon', 'Hpr': VBase3(-96.39, 0.0, 0.0), 'Min Population': '1', 'Patrol Radius': '12.0000', 'Pause Chance': 100, 'Pause Duration': 30, 'Pos': Point3(5.546, 33.646, 0.069), 'PoseAnim': '', 'PoseFrame': '', 'Scale': VBase3(1.0, 1.0, 1.0), 'Spawnables': 'Skel T5', 'Start State': 'Patrol', 'StartFrame': '0', 'Team': 'default', 'TrailFX': 'None', 'VisSize': '', 'Visual': {'Color': (0, 0, 0.65, 1), 'Model': 'models/misc/smiley'}}, '1189637504.0dxschafe': {'Type': 'Movement Node', 'Hpr': Point3(0.0, 0.0, 0.0), 'Pause Chance': '10', 'Pause Duration': '5', 'Pos': Point3(-115.353, -4.892, 25.003), 'Scale': VBase3(1.0, 1.0, 1.0), 'Visual': {'Color': (0.65, 0, 0, 1), 'Model': 'models/misc/smiley'}}, '1189637504.0dxschafe0': {'Type': 'Movement Node', 'Hpr': Point3(0.0, 0.0, 0.0), 'Pause Chance': '19', 'Pause Duration': '5', 'Pos': Point3(-85.201, 22.347, 24.947), 'Scale': VBase3(1.0, 1.0, 1.0), 'Visual': {'Color': (0.65, 0, 0, 1), 'Model': 'models/misc/smiley'}}, '1189637504.0dxschafe1': {'Type': 'Movement Node', 'Hpr': Point3(0.0, 0.0, 0.0), 'Pause Chance': '74', 'Pause Duration': '5', 'Pos': Point3(-77.619, 64.292, 15.37), 'Scale': VBase3(1.0, 1.0, 1.0), 'Visual': {'Color': (0.65, 0, 0, 1), 'Model': 'models/misc/smiley'}}, '1245456238.69piwanow': {'Type': 'Spawn Node', 'AnimSet': 'default', 'Hpr': VBase3(-172.875, 0.0, 0.0), 'Min Population': '1', 'Patrol Radius': '12.0000', 'Pause Chance': 100, 'Pause Duration': 30, 'Pos': Point3(32.393, 86.825, 0.069), 'PoseAnim': '', 'PoseFrame': '', 'Scale': VBase3(1.0, 1.0, 1.0), 'Spawnables': 'Spanish Undead Bandido', 'Start State': 'Patrol', 'StartFrame': '0', 'Team': 'default', 'TrailFX': 'None', 'VisSize': '', 'Visual': {'Color': (0, 0, 0.65, 1), 'Model': 'models/misc/smiley'}}, '1245456279.94piwanow': {'Type': 'Spawn Node', 'AnimSet': 'default', 'Hpr': VBase3(159.444, 0.0, 0.0), 'Min Population': '1', 'Patrol Radius': '12.0000', 'Pause Chance': 100, 'Pause Duration': 30, 'Pos': Point3(59.63, 84.278, 0.069), 'PoseAnim': '', 'PoseFrame': '', 'Scale': VBase3(1.0, 1.0, 1.0), 'Spawnables': 'Spanish Undead Bandido', 'Start State': 'Patrol', 'StartFrame': '0', 'Team': 'default', 'TrailFX': 'None', 'VisSize': '', 'Visual': {'Color': (0, 0, 0.65, 1), 'Model': 'models/misc/smiley'}}, '1245456317.19piwanow': {'Type': 'Spawn Node', 'AnimSet': 'default', 'Hpr': VBase3(63.435, 0.0, 0.0), 'Min Population': '1', 'Patrol Radius': '12.0000', 'Pause Chance': 100, 'Pause Duration': 30, 'Pos': Point3(108.667, -80.491, 0.073), 'PoseAnim': '', 'PoseFrame': '', 'Scale': VBase3(1.0, 1.0, 1.0), 'Spawnables': 'Skel T6', 'Start State': 'Patrol', 'StartFrame': '0', 'Team': 'default', 'TrailFX': 'None', 'VisSize': '', 'Visual': {'Color': (0, 0, 0.65, 1), 'Model': 'models/misc/smiley'}}, '1245456422.86piwanow': {'Type': 'Spawn Node', 'AnimSet': 'default', 'Hpr': VBase3(-91.548, 0.0, 0.0), 'Min Population': '1', 'Patrol Radius': '12.0000', 'Pause Chance': 100, 'Pause Duration': 30, 'Pos': Point3(-111.266, 59.542, 16.376), 'PoseAnim': '', 'PoseFrame': '', 'Scale': VBase3(1.0, 1.0, 1.0), 'Spawnables': 'Dread Scorpion', 'Start State': 'Ambush', 'StartFrame': '0', 'Team': 'default', 'TrailFX': 'None', 'VisSize': '', 'Visual': {'Color': (0, 0, 0.65, 1), 'Model': 'models/misc/smiley'}}, '1245456456.48piwanow': {'Type': 'Spawn Node', 'AnimSet': 'default', 'Hpr': VBase3(72.582, 0.0, 0.0), 'Min Population': '1', 'Patrol Radius': '12.0000', 'Pause Chance': 100, 'Pause Duration': 30, 'Pos': Point3(135.843, 43.604, 0.071), 'PoseAnim': '', 'PoseFrame': '', 'Scale': VBase3(1.0, 1.0, 1.0), 'Spawnables': 'Dread Scorpion', 'Start State': 'Ambush', 'StartFrame': '0', 'Team': 'default', 'TrailFX': 'None', 'VisSize': '', 'Visual': {'Color': (0, 0, 0.65, 1), 'Model': 'models/misc/smiley'}}, '1245456481.61piwanow': {'Type': 'Spawn Node', 'AnimSet': 'default', 'Hpr': VBase3(165.964, 0.0, 0.0), 'Min Population': '1', 'Patrol Radius': '12.0000', 'Pause Chance': 100, 'Pause Duration': 30, 'Pos': Point3(108.856, 87.371, 0.069), 'PoseAnim': '', 'PoseFrame': '', 'Scale': VBase3(1.0, 1.0, 1.0), 'Spawnables': 'Spanish Undead Pirata', 'Start State': 'Patrol', 'StartFrame': '0', 'Team': 'default', 'TrailFX': 'None', 'VisSize': '', 'Visual': {'Color': (0, 0, 0.65, 1), 'Model': 'models/misc/smiley'}}, '1245456495.84piwanow': {'Type': 'Spawn Node', 'AnimSet': 'default', 'Hpr': VBase3(126.87, 0.0, 0.0), 'Min Population': '1', 'Patrol Radius': '12.0000', 'Pause Chance': 100, 'Pause Duration': 30, 'Pos': Point3(123.547, 76.181, 0.069), 'PoseAnim': '', 'PoseFrame': '', 'Scale': VBase3(1.0, 1.0, 1.0), 'Spawnables': 'Spanish Undead Pirata', 'Start State': 'Patrol', 'StartFrame': '0', 'Team': 'default', 'TrailFX': 'None', 'VisSize': '', 'Visual': {'Color': (0, 0, 0.65, 1), 'Model': 'models/misc/smiley'}}, '1245456520.91piwanow': {'Type': 'Spawn Node', 'AnimSet': 'default', 'Hpr': VBase3(26.565, 0.0, 0.0), 'Min Population': '1', 'Patrol Radius': '12.0000', 'Pause Chance': 100, 'Pause Duration': 30, 'Pos': Point3(105.192, -121.129, 0.069), 'PoseAnim': '', 'PoseFrame': '', 'Scale': VBase3(1.0, 1.0, 1.0), 'Spawnables': 'Skel T6', 'Start State': 'Ambush', 'StartFrame': '0', 'Team': 'default', 'TrailFX': 'None', 'VisSize': '', 'Visual': {'Color': (0, 0, 0.65, 1), 'Model': 'models/misc/smiley'}}, '1245456614.55piwanow': {'Type': 'Spawn Node', 'AnimSet': 'default', 'Hpr': VBase3(-48.857, 0.0, 0.0), 'Min Population': '1', 'Patrol Radius': '7.0663', 'Pause Chance': 100, 'Pause Duration': 30, 'Pos': Point3(-24.892, -76.399, 0.069), 'PoseAnim': '', 'PoseFrame': '', 'Scale': VBase3(1.0, 1.0, 1.0), 'Spawnables': 'Spanish Undead Bandido', 'Start State': 'Patrol', 'StartFrame': '0', 'Team': 'default', 'TrailFX': 'None', 'VisSize': '', 'Visual': {'Color': (0, 0, 0.65, 1), 'Model': 'models/misc/smiley'}}, '1245456628.66piwanow': {'Type': 'Spawn Node', 'AnimSet': 'default', 'Hpr': VBase3(-92.862, 0.0, 0.0), 'Min Population': '1', 'Patrol Radius': '6.7229', 'Pause Chance': 100, 'Pause Duration': 30, 'Pos': Point3(-30.091, -59.001, 0.069), 'PoseAnim': '', 'PoseFrame': '', 'Scale': VBase3(1.0, 1.0, 1.0), 'Spawnables': 'Spanish Undead Pirata', 'Start State': 'Patrol', 'StartFrame': '0', 'Team': 'default', 'TrailFX': 'None', 'VisSize': '', 'Visual': {'Color': (0, 0, 0.65, 1), 'Model': 'models/misc/smiley'}}, '1245456780.69piwanow': {'Type': 'Spawn Node', 'AnimSet': 'default', 'Hpr': VBase3(332.008, 0.0, 0.0), 'Min Population': '1', 'Patrol Radius': '12.0000', 'Pause Chance': 100, 'Pause Duration': 30, 'Pos': Point3(57.006, -70.842, 0.076), 'PoseAnim': '', 'PoseFrame': '', 'Scale': VBase3(1.0, 1.0, 1.0), 'Spawnables': 'Skel T6', 'Start State': 'Patrol', 'StartFrame': '0', 'Team': 'default', 'TrailFX': 'None', 'VisSize': '', 'Visual': {'Color': (0, 0, 0.65, 1), 'Model': 'models/misc/smiley'}}, '1245457393.06piwanow': {'Type': 'Spawn Node', 'AnimSet': 'default', 'Hpr': VBase3(-69.057, 0.0, 0.0), 'Min Population': '1', 'Patrol Radius': '8.4398', 'Pause Chance': 100, 'Pause Duration': 30, 'Pos': Point3(-34.254, -6.97, 0.069), 'PoseAnim': '', 'PoseFrame': '', 'Scale': VBase3(1.0, 1.0, 1.0), 'Spawnables': 'Skel T5', 'Start State': 'Patrol', 'StartFrame': '0', 'Team': 'default', 'TrailFX': 'None', 'VisSize': '', 'Visual': {'Color': (0, 0, 0.65, 1), 'Model': 'models/misc/smiley'}}}, 'Visibility': 'Grid', 'Visual': {'Model': 'models/caves/cave_c_zero'}}}, 'TodSettings': {'AmbientColors': {0: Vec4(0.45, 0.53, 0.65, 1), 2: Vec4(1, 1, 1, 1), 4: Vec4(0.4, 0.45, 0.5, 1), 6: Vec4(0.44, 0.45, 0.56, 1), 8: Vec4(0.39, 0.42, 0.54, 1), 12: Vec4(0.34, 0.28, 0.41, 1), 13: Vec4(0.34, 0.28, 0.41, 1), 16: Vec4(0.25, 0.25, 0.25, 1)}, 'DirectionalColors': {0: Vec4(0.55, 0.46, 0.35, 1), 2: Vec4(1, 1, 1, 1), 4: Vec4(0.6, 0.34, 0.1, 1), 6: Vec4(0.46, 0.48, 0.45, 1), 8: Vec4(0.42, 0.42, 0.4, 1), 12: Vec4(0.66, 0.76, 0.05, 1), 13: Vec4(0.66, 0.76, 0.05, 1), 16: Vec4(0, 0, 0, 1)}, 'FogColors': {0: Vec4(0.3, 0.2, 0.15, 0), 2: Vec4(0.6, 0.694118, 0.894118, 1), 4: Vec4(0.3, 0.18, 0.15, 0), 6: Vec4(0.15, 0.2, 0.35, 0), 8: Vec4(0.05, 0.06, 0.17, 0), 12: Vec4(0.1, 0.12, 0.03, 0), 13: Vec4(0.1, 0.12, 0.03, 0), 16: Vec4(0.25, 0.25, 0.25, 1)}, 'FogRanges': {0: 0.0001, 2: 9.999999747378752e-05, 4: 0.0001, 6: 0.0001, 8: 0.0002, 12: 0.00025, 13: 0.00025, 16: 0.0001}, 'LinearFogRanges': {0: (0.0, 100.0), 2: (0.0, 100.0), 4: (0.0, 100.0), 6: (0.0, 100.0), 8: (0.0, 100.0), 12: (0.0, 100.0), 13: (0.0, 100.0), 16: (0.0, 100.0)}}, 'Node Links': [['1189637504.0dxschafe', '1176239104.0dxschafe', 'Bi-directional'], ['1189637504.0dxschafe0', '1189637504.0dxschafe', 'Bi-directional'], ['1189637504.0dxschafe0', '1189637504.0dxschafe1', 'Bi-directional']], 'Layers': {}, 'ObjectIds': {'1164929110.98sdnaik': '["Objects"]["1164929110.98sdnaik"]', '1164930102.27sdnaik': '["Objects"]["1164929110.98sdnaik"]["Objects"]["1164930102.27sdnaik"]', '1164930102.28sdnaik': '["Objects"]["1164929110.98sdnaik"]["Objects"]["1164930102.28sdnaik"]', '1176238208.0dxschafe': '["Objects"]["1164929110.98sdnaik"]["Objects"]["1176238208.0dxschafe"]', '1176238208.0dxschafe0': '["Objects"]["1164929110.98sdnaik"]["Objects"]["1176238208.0dxschafe0"]', '1176238208.0dxschafe1': '["Objects"]["1164929110.98sdnaik"]["Objects"]["1176238208.0dxschafe1"]', '1176239104.0dxschafe': '["Objects"]["1164929110.98sdnaik"]["Objects"]["1176239104.0dxschafe"]', '1188602752.0dxschafe': '["Objects"]["1164929110.98sdnaik"]["Objects"]["1188602752.0dxschafe"]', '1188602752.0dxschafe0': '["Objects"]["1164929110.98sdnaik"]["Objects"]["1188602752.0dxschafe0"]', '1189033600.0dchiappe': '["Objects"]["1164929110.98sdnaik"]["Objects"]["1189033600.0dchiappe"]', '1189033600.0dchiappe0': '["Objects"]["1164929110.98sdnaik"]["Objects"]["1189033600.0dchiappe0"]', '1189033728.0dchiappe': '["Objects"]["1164929110.98sdnaik"]["Objects"]["1189033728.0dchiappe"]', '1189033856.0dchiappe': '["Objects"]["1164929110.98sdnaik"]["Objects"]["1189033856.0dchiappe"]', '1189637504.0dxschafe': '["Objects"]["1164929110.98sdnaik"]["Objects"]["1189637504.0dxschafe"]', '1189637504.0dxschafe0': '["Objects"]["1164929110.98sdnaik"]["Objects"]["1189637504.0dxschafe0"]', '1189637504.0dxschafe1': '["Objects"]["1164929110.98sdnaik"]["Objects"]["1189637504.0dxschafe1"]', '1245456238.69piwanow': '["Objects"]["1164929110.98sdnaik"]["Objects"]["1245456238.69piwanow"]', '1245456279.94piwanow': '["Objects"]["1164929110.98sdnaik"]["Objects"]["1245456279.94piwanow"]', '1245456317.19piwanow': '["Objects"]["1164929110.98sdnaik"]["Objects"]["1245456317.19piwanow"]', '1245456422.86piwanow': '["Objects"]["1164929110.98sdnaik"]["Objects"]["1245456422.86piwanow"]', '1245456456.48piwanow': '["Objects"]["1164929110.98sdnaik"]["Objects"]["1245456456.48piwanow"]', '1245456481.61piwanow': '["Objects"]["1164929110.98sdnaik"]["Objects"]["1245456481.61piwanow"]', '1245456495.84piwanow': '["Objects"]["1164929110.98sdnaik"]["Objects"]["1245456495.84piwanow"]', '1245456520.91piwanow': '["Objects"]["1164929110.98sdnaik"]["Objects"]["1245456520.91piwanow"]', '1245456614.55piwanow': '["Objects"]["1164929110.98sdnaik"]["Objects"]["1245456614.55piwanow"]', '1245456628.66piwanow': '["Objects"]["1164929110.98sdnaik"]["Objects"]["1245456628.66piwanow"]', '1245456780.69piwanow': '["Objects"]["1164929110.98sdnaik"]["Objects"]["1245456780.69piwanow"]', '1245457393.06piwanow': '["Objects"]["1164929110.98sdnaik"]["Objects"]["1245457393.06piwanow"]'}}
extraInfo = {'camPos': Point3(619.568, 288.857, 661.517), 'camHpr': VBase3(116.607, -43.8887, 0), 'focalLength': 1.39999997616, 'skyState': 2, 'fog': 0}