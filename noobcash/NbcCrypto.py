
from cryptography.exceptions                   import InvalidSignature
from cryptography.hazmat.backends              import default_backend
from cryptography.hazmat.primitives            import hashes
from cryptography.hazmat.primitives            import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding, utils

import Constants

def keyFromPEM(pemBytes):
    # https://cryptography.io/en/latest/hazmat/primitives/asymmetric/serialization/#pem
    return serialization.load_pem_private_key(
        data     = pemBytes,
        password = None,
        backend  = default_backend()
    )

def keyToPEM(key):
    # https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/#key-serialization
    return key.private_bytes(
        encoding             = serialization.Encoding.PEM,
        format               = serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm = serialization.NoEncryption()
    )

def generateKey():
    # https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/#generation
    return rsa.generate_private_key(
        public_exponent = Constants.RSA_EXPONENT,
        key_size        = Constants.KEY_SIZE,
        backend         = default_backend()
    )

def getAddress(key):
    # https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/#numbers
    pubkey  = key.public_key()
    pubnums = pubkey.public_numbers()
    return pubnums.n.to_bytes(Constants.KEY_SIZE // 8, 'little')

def pubkeyFromAddress(address):
    # https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/#numbers
    return rsa.RSAPublicNumbers(
        e = Constants.RSA_EXPONENT,
        n = int.from_bytes(address, 'little')
    ).public_key(default_backend())

def sign(key, data):
    # https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/#signing
    # `data` may be to large to be hashed by `sign()`,
    # so we hash it in advance, and pass the hash instead
    alg = hashes.SHA256()
    h   = hashes.Hash(alg, default_backend())
    h.update(data)
    digest = h.finalize()
    return key.sign(
        data      = digest,
        padding   = padding.PSS(
            mgf         = padding.MGF1(alg),
            salt_length = padding.PSS.MAX_LENGTH
        ),
        algorithm = utils.Prehashed(alg)
    )

def verify(pubkey, signature, data):
    # https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/#verification
    # `data` may be to large to be hashed by `verify()`,
    # so we hash it in advance, and pass the hash instead
    alg = hashes.SHA256()
    h   = hashes.Hash(alg, default_backend())
    h.update(data)
    digest = h.finalize()
    try:
        pubkey.verify(
            signature = signature,
            data      = digest,
            padding   = padding.PSS(
                mgf         = padding.MGF1(alg),
                salt_length = padding.PSS.MAX_LENGTH
            ),
            algorithm = utils.Prehashed(alg)
        )
        return True
    except (InvalidSignature, ValueError):
        return False

def verifyByAddress(address, signature, data):
    pubkey = pubkeyFromAddress(address)
    return verify(pubkey, signature, data)

