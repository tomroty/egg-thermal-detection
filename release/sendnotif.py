from exponent_server_sdk import (
    DeviceNotRegisteredError,
    PushClient,
    PushMessage,
    PushServerError,
)

def sendNotification(token: str, title: str, body: str, extra: dict = None, sound: str = 'default', ttl: int = 0):
    try:
        response = PushClient().publish(
            PushMessage(
                to=token,
                title=title,
                body=body,
                data=extra,
                sound=sound,
                ttl=ttl,
                
            )
        )
    except PushServerError as err:
        print(err)
        return False

    try:
        response.validate_response()
    except DeviceNotRegisteredError:
        print('Device not regfistered')
        return False
    return True


        

