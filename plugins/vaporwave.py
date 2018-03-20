import pinhook.plugin as p

WIDE_MAP = dict((i, i + 0xFEE0) for i in range(0x21, 0x7F))
WIDE_MAP[0x20] = 0x3000

def widen(s):
    return s.translate(WIDE_MAP)

@p.register('!vapourwave')
@p.register('!vaporwave')
def wave(msg):
    return p.message(widen(msg.arg))
