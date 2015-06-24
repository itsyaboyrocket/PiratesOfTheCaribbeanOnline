loadPrcFile('config/general.prc')

class game:
    name = 'pirates'
    process = 'server'
__builtins__.game = game

from pirates.ai.PiratesAIRepository import PiratesAIRepository
simbase.air = PiratesAIRepository(401000000, 4002, 'Ocean')
simbase.air.connect('127.0.0.1', 7100)

run()