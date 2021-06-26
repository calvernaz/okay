import jwt.exceptions
import pytest
from okay.jwt import main, decode

__author__ = "Cesar Alvernaz"
__copyright__ = "Cesar Alvernaz"
__license__ = "MIT"

from fixtures.jwt_fixtures import VALID_TOKEN, SECRET, \
    EXPECTED_TOKEN_PAYLOAD, INVALID_SECRET, VALID_RS256_TOKEN, \
    EXPECTED_TOKEN_RS256_PAYLOAD


def test_decode_without_signature_verification():
    assert decode(VALID_TOKEN, SECRET) == EXPECTED_TOKEN_PAYLOAD


def test_decode_with_signature_verification():
    assert decode(VALID_TOKEN, SECRET, verify_signature=True) == \
           EXPECTED_TOKEN_PAYLOAD


def test_decode_with_invalid_secret():
    with pytest.raises(jwt.exceptions.InvalidSignatureError):
        decode(VALID_TOKEN, INVALID_SECRET, verify_signature=True)


def test_decode_with_invalid_secret_no_validation():
    assert decode(VALID_TOKEN, INVALID_SECRET, verify_signature=False) == \
           EXPECTED_TOKEN_PAYLOAD


def test_decode_with_invalid_token_type_with_validation():
    with pytest.raises(jwt.exceptions.InvalidAlgorithmError):
        decode(VALID_RS256_TOKEN, SECRET, verify_signature=True)


def test_decode_with_invalid_token_type_with_no_validation():
    assert decode(VALID_RS256_TOKEN, SECRET, verify_signature=False) == \
           EXPECTED_TOKEN_RS256_PAYLOAD


# def test_main(capsys):
#     """CLI Tests"""
#     # capsys is a pytest fixture that allows asserts agains stdout/stderr
#     # https://docs.pytest.org/en/stable/capture.html
#     main(["7"])
#     captured = capsys.readouterr()
#     assert "The 7-th Fibonacci number is 13" in captured.out
