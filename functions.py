def getBoxSize(box):
    return box.maxx - box.minx, box.maxy - box.miny, box.maxz - box.minz


def get_block(level, x, y, z):
    return level.blockAt(x, y, z)


def setBlock(level, x, y, z, block_id, data=0):
    level.setBlockAt(x, y, z, block_id)
    level.setBlockDataAt(x, y, z, data)
