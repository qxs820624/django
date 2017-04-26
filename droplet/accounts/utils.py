from django.core import signing
from django.core.urlresolvers import reverse


def get_signer(salt='register_email_confirm'):
    """ get the timestamp sign
    :param salt:
    :return timestampsign object
    """
    return signing.TimestampSigner(salt=salt)


def get_confirmation_url(email,request,username=None):
    """
        Return confirmation url
        :param email
        :return: string of url
    """
    singer = get_signer()
    code_list = [email,'']
    if username:
        code_list[1] = username
    code = singer.sign(':'.join(code_list))
    url = request.build_absolute_uri(reverse('accounts:email_confirmation',kwargs={'code':code}))
    return url


class InvalidCode(Exception):
    """Problems occurred during decoding the registration link"""
    pass


def decode(code,max_age=15*60*60):
    """"""
    try:
        data=get_signer().unsign(code,max_age=max_age)
    except signing.SignatureExpired:
        raise InvalidCode("The link is expired. Please request another registration link.")
    except signing.BadSignature:
        raise InvalidCode(
            'Unable to verify the signature. Please request a new'
            ' registration link.')
    parts = data.rsplit(':',2)
    if len(parts) != 2:
        raise InvalidCode("Something went wrong while decoding the"
            " registration request. Please try again.")
    email,user = parts
    return email,user

