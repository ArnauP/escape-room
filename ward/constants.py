from string import ascii_uppercase
from random import randint, choice
from datetime import datetime
from time import time


PATH_ICON = 'resources/icons/black-hole.png'
PATH_STYLE = 'resources/style/style.css'

TYPE_PROMPT_SERVER = 'server'
TYPE_PROMPT_WEAPONS = 'weapons'
TYPE_PROMPT_ENGINES = 'engines'

STATUS_WEAPONS = ['ONLINE', 'ONLINE', 'ONLINE', 'ONLINE', 'OFFLINE', 'OFFLINE', 'PENDING REPAIR']
STATUS_ENGINES = ['RUNNING', 'RUNNING', 'RUNNING', 'RUNNING', 'RUNNING', 'OFFLINE', 'PENDING REPAIR']
STATUS_SERVER = [200, 200, 200, 200, 200, 200, 404, 400, 503]

EXPECTED_PASSWORD = 'test'

COMMAND_SYSTEM_SHUTDOWN = 'system shutdown'
COMMAND_SYSTEM_STATUS = 'system status'
COMMAND_WEAPONS_ENABLE = 'weapons enable'
COMMAND_WEAPONS_DISABLE = 'weapons disable'
COMMAND_SERVER_STATUS = 'server status'
COMMAND_SERVER_KEY = 'server key'
COMMAND_ENGINES_START = 'engines start'
COMMAND_ENGINES_STOP = 'engines stop'
COMMAND_HELP = 'help'

MSG_HELP = '>> For command information use "{}".'.format(COMMAND_HELP)
MSG_HELP_RESPONSE = '\n>> Options and arguments available:\n' \
                    '       - Server commands:\n' \
                    '               {}\n' \
                    '               {}\n' \
                    '       - Weapons commands:\n' \
                    '               {}\n' \
                    '               {}\n' \
                    '       - Engine commands:\n' \
                    '               {}\n' \
                    '               {}\n' \
                    '       - System commands:\n' \
                    '               {}\n' \
                    '               {}\n'.format(COMMAND_SERVER_STATUS, COMMAND_SERVER_KEY, 
                    COMMAND_WEAPONS_ENABLE, COMMAND_WEAPONS_DISABLE, COMMAND_ENGINES_START, 
                    COMMAND_ENGINES_STOP, COMMAND_SYSTEM_STATUS, COMMAND_SYSTEM_SHUTDOWN)
MSG_AUTOMATIC_WEAPONS = [
    '>> [{}] - TURRET <{}{}> - {}',
    '>> [{}] - LASER CANON <{}{}> - {}',
    '>> [{}] - WHITE EAGLE <{}{}> - {}',
    '>> [{}] - IONIC BEAM <{}{}> - {}',
    '>> [{}] - PLASMA EMITTER <{}{}> - {}',
    '>> [{}] - PHOTON BLASTER <{}{}> - {}',
    '>> [{}] - ANTI-MATTER LAUNCHER <{}{}> - {}'
]

MSG_AUTOMATIC_SERVER = [
    '>> [{}] - /GET server_status\n     Return code: {}',
    '>> [{}] - /GET system_status\n     Return code: {}',
    '>> [{}] - /GET weapons_status\n     Return code: {}',
    '>> [{}] - /GET engines_status\n     Return code: {}',
    '>> [{}] - /POST weapon_query\n     Return code: {}',
    '>> [{}] - /POST engine_query\n     Return code: {}',
    '>> [{}] - /POST system_query\n     Return code: {}'
]

MSG_AUTOMATIC_ENGINES = [
    '>> [{}] - RS-2200 <{}> - {}',
    '>> [{}] - SIDE ROTOR <{}> - {}',
    '>> [{}] - HOVER PROPULSOR <{}> - {}',
    '>> [{}] - IGNITION TRIGGER <{}> - {}',
    '>> [{}] - SWIRL INJECTOR <{}> - {}',
    '>> [{}] - G-FORCE GENERATOR <{}> - {}',
    '>> [{}] - PLASMA BARRIER <{}> - {}'
]
