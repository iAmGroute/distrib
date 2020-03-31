
import Constants

from Block import Block

def make_dummy_block():
    return Block.fromJson([
        0,
        "0123456789ABCDEF",
        "0000000000000000000000000000000000000000000000000000000030313233",
        "0000000000000000000000000000000000000000000000000000000030313233",
        "0123456789ABCDEF",
        []
    ])

def test_header_size():
    b = make_dummy_block()
    assert len(b.getHeaderBytes()) == Constants.BLOCK_HEADER_SIZE

