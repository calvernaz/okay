VALID_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.' \
              'eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6Ikpv' \
              'aG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.' \
              'XbPfbIHMI6arZ3Y922BhjWgQzWXcXNrz0ogtVhfEd2o'

VALID_RS256_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM' \
                    '0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWU' \
                    'sImlhdCI6MTUxNjIzOTAyMn0.POstGetfAytaZS82wHcjoTyoqhM' \
                    'yxXiWdR7Nn7A29DNSl0EiXLdwJ6xC6AfgZWF1bOsS_TuYI3OG85A' \
                    'miExREkrS6tDfTQ2B3WXlrr-wp5AokiRbz3_oB4OxG-W9KcEEbDR' \
                    'cZc0nH3L7LzYptiy1PtAylQGxHTWZXtGz4ht0bAecBgmpdgXMguEI' \
                    'coqPJ1n3pIWk_dUZegpqx0Lka21H6XxUTxiy8OcaarA8zdnPUnV6' \
                    'AmNP3ecFawIFYdvJB_cm-GvpCSbr8G8y_Mllj8f4x9nBH8pQux' \
                    '89_6gUY618iYv7tuPWBFfEbLxtF2pZS6YC1aSfLQxeNe8djT9YjpvRZA'

SECRET = 'secret'
INVALID_SECRET = 'invalid_secret'

EXPECTED_TOKEN_PAYLOAD = \
    {'iat': 1516239022, 'name': 'John Doe', 'sub': '1234567890'}

EXPECTED_TOKEN_RS256_PAYLOAD = \
    {'admin': True, 'iat': 1516239022, 'name': 'John Doe', 'sub': '1234567890'}
