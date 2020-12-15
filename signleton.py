"""
用__new__实现单例模式
https://amos-x.com/index.php/amos/archives/python-singleton/
"""

class A:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
