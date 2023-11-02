#!/usr/bin/python3
import types
import hidden_4

names = [name for name in dir(hidden_4) if not name.startswith("__")]
names.sort()

for name in names:
    attr = getattr(hidden_4, name)
    if isinstance(attr, types.ModuleType):
        print(name + " (module)")
    else:
        print(name)
