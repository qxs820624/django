from django.core.mail import EmailMultiAlternatives

def send_signup_mail(name,url,to):
    """user sign up mail send"""
    html_content = """<h3>Hi: %s </h3><p>Please confirm your account by clicking on the following link:
        <a href='%s'>Confirm My Account</a><br><p><b>,the confirm email will expired in 15 minutes.
        If you did not sign up for this account, you can disregard this email and the account will not be created.
        </b></p><br>
        Regards,<br>
        The Development Team""" %(name,url)
    print(html_content)
    msg = EmailMultiAlternatives('Account registration confirmation', html_content, 'admin@www.com', [to])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
