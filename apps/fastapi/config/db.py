""" db mongo connection  """
# pylint: disable=import-error
import motor.motor_tornado

client = motor.motor_tornado.MotorClient('mongodb://root:example@mongo:27017/')
