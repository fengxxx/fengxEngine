import wx

class Vector3(object):
	def __init__(self):
		self._x=0


	thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
	@property
	def x(self):
	    return self._x
	@x.setter
	def x(self, value):
	    self._x = value
		


a=Vector3()

print a
print str(a.x)
class Singleton(object):
	_singletons = {}
	def __new__(cls, *args, **kwds):
		if not cls._singletons.has_key(cls):           
		 cls._singletons[cls] = object.__new__(cls)  
		return cls._singletons[cls]    


c=Singleton
b=c