import pytest
from zerodb.crypto import AES, rand
from zerodb.crypto.exceptions import WrongKeyError
from zerodb.crypto import scrypt_hash

TEST_TEXT = "hello world"


def test_aes_rand():
    key = rand(32)

    cipher1 = AES(key=key)
    ciphertext = cipher1.encrypt(TEST_TEXT)

    cipher2 = AES(key=key)
    assert cipher2.decrypt(ciphertext) == TEST_TEXT


def test_aes_passphrase():
    passphrase = "the most secret passphrase ever"

    cipher1 = AES(passphrase=passphrase)
    ciphertext = cipher1.encrypt(TEST_TEXT)

    cipher2 = AES(passphrase=passphrase)
    assert cipher2.decrypt(ciphertext) == TEST_TEXT


def test_aes_exception():
    passphrase = "the most secret passphrase ever"

    cipher1 = AES(passphrase=passphrase)
    ciphertext = cipher1.encrypt(TEST_TEXT)

    cipher2 = AES(passphrase="wrong one")
    with pytest.raises(WrongKeyError):
        cipher2.decrypt(ciphertext)


def test_scrypt():
    password = "no one will guess this password"
    h = scrypt_hash.hash_password(password)
    assert scrypt_hash.verify_password(h, password)
    assert not scrypt_hash.verify_password(h, password + "oops")