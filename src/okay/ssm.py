import logging

from botocore.exceptions import ClientError

_logger = logging.getLogger(__name__)


class SecretsManagerSecret:
    """Encapsulates Secrets Manager functions."""

    def __init__(self, secretsmanager_client):
        self._ssm_client = secretsmanager_client

    def get_value(self, key: str, stage=None):
        """
        Gets the value of a secret.

        :param key: the secret key
        :param stage: The stage of the secret to retrieve. If this is None, the
                      current stage is retrieved.
        :return: The value of the secret. When the secret is a string,
        the value is
                 contained in the `SecretString` field. When the secret is
                 bytes,
                 it is contained in the `SecretBinary` field.
        """
        if key is None:
            raise ValueError

        try:
            kwargs = {'SecretId': key}
            if stage is not None:
                kwargs['VersionStage'] = stage
            response = self._ssm_client.get_secret_value(**kwargs)
            _logger.info("Got value for secret %s.", key)
        except ClientError:
            _logger.exception("Couldn't get value for secret %s.", key)
            raise
        else:
            return response['SecretString']
