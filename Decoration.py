def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            # 因為要返回now()的return value, 若要在執行後操作, 可先將return value 儲存 再return
            print("Call %s(), %s" % (func.__name__, text))
            ret = func(*args, **kw)
            print('exit function.')
            return ret
        return wrapper
    return decorator

@log('execute')
def now():
    print('2021')
    return False


def log(text):
    def decorate(func):
        def wrapper(*args, **kwargs):
            print('Call %s, %s' % (func.__name__, text))
            return func(*args, **kwargs)
        return wrapper

    def wrapper(*args, **kwargs):
        print('Call %s, %s' % (text.__name__, text))
        return text(*args, **kwargs)

        return wrapper
    return decorate if isinstance(text, str) else wrapper
@log
def now():
    pass
# log(now)
now()


@log('a')
def now():
    pass
# log('a')(now)
now()



