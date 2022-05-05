from twilio.rest import Client

accountSid = 'AC557dd792ec59de3d312fd9c8526ba03f'
authToken = '740c4217207cef2b3f9297e268c3eb34'

clien = Client(accountSid,authToken)
message = clien.messages.create(
    from_ = '+16203203024',
    to = '+86 156 5654 7075',
    body = '我就是进行测试的号码'
)