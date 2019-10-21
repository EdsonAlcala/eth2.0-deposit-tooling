from Crypto.Hash import (
    SHA256 as _sha256,
    SHA512 as _sha512,
)
from Crypto.Protocol.KDF import (
    scrypt as _scrypt,
    HKDF as _HKDF,
    PBKDF2 as _PBKDF2,
)


def SHA256(x):
    return _sha256.new(x).digest()


def scrypt(*, password: str, salt: str, n: int, r: int, p: int, dklen: int) -> bytes:
    res = _scrypt(password=password, salt=salt, key_len=dklen, N=n, r=r, p=p)
    return res if isinstance(res, bytes) else res[0]  # PyCryptodome can return Tuple[bytes]


def PBKDF2(*, password: str, salt: bytes, dklen: int, count: int) -> bytes:
    res = _PBKDF2(password=password, salt=salt, dkLen=dklen, count=count, hmac_hash_module=_sha512)
    return res if isinstance(res, bytes) else res[0]  # PyCryptodome can return Tuple[bytes]


def HKDF(*, salt: bytes, IKM: bytes, L: int) -> bytes:
    res = _HKDF(master=IKM, key_len=L, salt=salt, hashmod=_sha256)
    return res if isinstance(res, bytes) else res[0]  # PyCryptodome can return Tuple[bytes]