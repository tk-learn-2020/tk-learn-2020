
import numbers

class Field:
    # 公共类方便判断逻辑
    pass

class IntField(Field):

    def __init__(self, db_column=None, min_value=None, max_value=None):
        self._value = None
        self.min_value = min_value
        self.max_value = max_value
        if min_value is not None:
            if not isinstance(min_value, numbers.Integral):
                raise ValueError("min_value must be int")
            elif min_value < 0:
                raise ValueError("min_value must be positive int")

        if max_value is not None:
            if not isinstance(max_value, numbers.Integral):
                raise ValueError("max_value must be int")
            elif max_value < 0:
                raise ValueError("max_value must be positive int")
        if min_value is not None and max_value is not None:
            if min_value > max_value:
                raise ValueError("min_value must be smaller than max_value")

        self.db_column = db_column

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("int need")
        if value < self.min_value or value > self.max_value:
            raise ValueError("value must between min_value and max_value")
        self._value = value


class CharField(Field):

    def __init__(self,db_column=None, max_length=None, value=None):
        self._value = value
        if max_length is None:
            raise ValueError("you must specify max_length for charfield")
        self.max_length = max_length
        self.db_column = db_column

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("str need")
        if len(value) > self.max_length:
            raise ValueError("value len excess len of max_length")
        self._value = value


class ModelMetaClass(type):
    # def __new__(cls, *args, **kwargs):
    # caution: args传进来的东西, 与type创建类时接收的三个参数一致
    # 可以修改这样：
    def __new__(cls, name, bases, attrs, **kwargs):
        if name == "BaseModel":
            return super().__new__(cls, name, bases, attrs, **kwargs)
        fields = {}
        for key, value in attrs.items():
            if isinstance(value, Field):
                fields[key] = value
        attrs_meta = attrs.get("Meta")
        _meta = {}
        db_table = name.lower()
        if attrs_meta is not None:
            table = getattr(attrs_meta, "db_table", None)
            if table is not None:
                db_table = table
        _meta["db_table"] = db_table
        attrs["_meta"] = _meta
        attrs["fields"] = fields
        del attrs["Meta"]
        return super().__new__(cls, name, bases, attrs, **kwargs)


class BaseModel(metaclass=ModelMetaClass):

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        super().__init__()

    def save(self):
        fields = []
        values = []
        for key, value in self.fields.items():
            db_column = value.db_column
            if db_column is None:
                db_column = key.lower()
            fields.append(db_column)
            value = getattr(self, key)
            values.append(str(value))
        sql = "insert {} ({}) values ({})".format(self._meta['db_table'], ','.join(fields), ','.join(values))
        print(sql)


class User(BaseModel):
    name = CharField(db_column="name", max_length=100)
    age = IntField(db_column="age", min_value=0, max_value=100)

    class Meta:
        db_table = "user"

if __name__ == '__main__':
    user = User()
    user.name = "zzlion"
    user.age = 28
    user.save()

