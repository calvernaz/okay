import argparse
import logging
import sys

import boto3
import jwt
from okay import __version__

__author__ = "Cesar Alvernaz"
__copyright__ = "Cesar Alvernaz"
__license__ = "MIT"

from okay.ssm import SecretsManagerSecret

_logger = logging.getLogger(__name__)
logging.getLogger('botocore').setLevel(logging.CRITICAL)
logging.getLogger('urllib3').setLevel(logging.CRITICAL)

_ssm = SecretsManagerSecret(boto3.client('secretsmanager'))

DEFAULT_ALG = 'HS256'


def decode(token: str, secret: str, verify_signature=False):
    """JWT token decode

    Args:
      token (str): string
      secret (str): string
      verify_signature(bool): boolean

    Returns:
      str: the token payload
    """
    assert token

    alg = DEFAULT_ALG
    header = jwt.get_unverified_header(token)
    if header:
        alg = header.get('alg', DEFAULT_ALG)

    return jwt.decode(token, secret,
        options={"verify_signature": verify_signature},
        algorithms=[alg])


def decode_ssm(token: str, secret_key: str, verify_signature=False):
    """JWT token decode using AWS Secrets Manager

    Args:
      token (str): string
      secret_key (str): string
      verify_signature(bool): boolean

    Returns:
      str: the token payload
    """
    secret = _ssm.get_value(key=secret_key)
    decode(token, secret, verify_signature)


def parse_args(args):
    """Parse command line parameters

    Args:
      args (List[str]): command line parameters as list of strings
          (for example  ``["--help"]``).

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(
        description="Okay to decode JWT tokens")
    parser.add_argument(
        "--version",
        action="version",
        version="okay {ver}".format(ver=__version__),
    )
    parser.add_argument(
        "-v",
        "--verbose",
        dest="loglevel",
        help="set loglevel to INFO",
        action="store_const",
        const=logging.DEBUG,
    )
    parser.add_argument(dest="token", help="the jwt token string", type=str,
        metavar="TOKEN")
    parser.add_argument(dest="secret", help="the token secret", type=str,
        metavar="SECRET")
    parser.add_argument('--verify', help="verify token signature",
        action='store_true')
    parser.add_argument('--aws', help="get the secret from aws secrets "
                                      "manager", action='store_true')
    return parser.parse_args(args)


def setup_logging(log_level):
    """Setup basic logging

    Args:
      log_level (int): minimum loglevel for emitting messages
    """
    log_format = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(
        level=log_level, stream=sys.stdout, format=log_format,
        datefmt="%Y-%m-%d %H:%M:%S"
    )


def main(args):
    args = parse_args(args)
    setup_logging(args.loglevel)

    if args.aws:
        return print(
            decode_ssm(args.token, args.secret, verify_signature=args.verify))
    else:
        return print(
            decode(args.token, args.secret, verify_signature=args.verify))


def run():
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
