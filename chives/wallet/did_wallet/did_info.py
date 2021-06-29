from dataclasses import dataclass
from typing import List, Optional, Tuple

from chives.types.blockchain_format.sized_bytes import bytes32
from chives.util.ints import uint64
from chives.util.streamable import streamable, Streamable
from chives.wallet.cc_wallet.ccparent import CCParent
from chives.types.blockchain_format.program import Program
from chives.types.blockchain_format.coin import Coin


@dataclass(frozen=True)
@streamable
class DIDInfo(Streamable):
    origin_coin: Optional[Coin]  # puzzlehash of this coin is our DID
    backup_ids: List[bytes]
    num_of_backup_ids_needed: uint64
    parent_info: List[Tuple[bytes32, Optional[CCParent]]]  # {coin.name(): CCParent}
    current_inner: Optional[Program]  # represents a Program as bytes
    temp_coin: Optional[Coin]  # partially recovered wallet uses these to hold info
    temp_puzhash: Optional[bytes32]
    temp_pubkey: Optional[bytes]
