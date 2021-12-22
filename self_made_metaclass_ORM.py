import datetime
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.name, self.column_type)

class StringField(Field):
    def __init__(self, name):
        return super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
    def __init__(self, name):
        return super(IntegerField, self).__init__(name, 'bigint')

class TimeField(Field):
    def __init__(self, name):
        return super(TimeField, self).__init__(name, 'CURRENT_TIMESTAMP')

class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = {}
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v.name))
                mappings[k] = v.name
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name

        return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)
    def __getattr__(self, k):
        try:
            return self[k]
        except Exception:
            raise AttributeError
        return self[k]
    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        parameters = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v)
            parameters.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(parameters))
        final_sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(map(repr, args)))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))
        print('Final SQL: %s' % final_sql)


class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')
    time = TimeField('date')

# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd', time=str(datetime.datetime.now()))
# 保存到数据库：
u.save()
