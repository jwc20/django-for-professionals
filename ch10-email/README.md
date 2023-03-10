# Chapter 10: Email

## About

- In this chapter we will fully configure email and add password change and password reset functionality.

## Instructions

```
mkdir templates/account/email
vi templates/account/email/email_confirmation_subject.txt
vi templates/account/email/email_confirmation_message.txt
```

- Modify email_confirmation_subject.
- Modify email_confirmation_message.
- Update sites domain name in admin panel sites.
- Update DEFAULT_FROM_EMAIL in settings.

```
docker-compose logs
```

- Check logs to see if email confirmation is working and click on the link.

```
vi templates/account/email/email_confirmation.html
```

- Create email_confirmation template

- (optional) Update EMAIL_BACKEND in settings to use smtp.
