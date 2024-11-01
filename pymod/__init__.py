import importlib
import pymod.mqtt

def define_env(env):
    importlib.reload(pymod.mqtt)
    pymod.mqtt.define_env(env)
