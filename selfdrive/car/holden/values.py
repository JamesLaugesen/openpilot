# flake8: noqa

from cereal import car
from selfdrive.car import dbc_dict
Ecu = car.CarParams.Ecu

class CarControllerParams():
  def __init__(self):
    self.STEER_MAX = 300
    self.STEER_STEP = 2              # how often we update the steer cmd
    self.STEER_DELTA_UP = 7          # ~0.75s time to peak torque (255/50hz/0.75s)
    self.STEER_DELTA_DOWN = 17       # ~0.3s from peak torque to zero
    self.MIN_STEER_SPEED = 3.
    self.STEER_DRIVER_ALLOWANCE = 50   # allowed driver torque before start limiting
    self.STEER_DRIVER_MULTIPLIER = 4   # weight driver torque heavily
    self.STEER_DRIVER_FACTOR = 100     # from dbc
    self.NEAR_STOP_BRAKE_PHASE = 0.5  # m/s, more aggressive braking near full stop

    # Takes case of "Service Adaptive Cruise" and "Service Front Camera"
    # dashboard messages.
    self.ADAS_KEEPALIVE_STEP = 100
    self.CAMERA_KEEPALIVE_STEP = 100

    # pedal lookups, only for Volt
    MAX_GAS = 3072              # Only a safety limit
    ZERO_GAS = 2048
    MAX_BRAKE = 350             # Should be around 3.5m/s^2, including regen

    self.ACCEL_MAX = 2.0 # m/s^2

    # Allow small margin below -3.5 m/s^2 from ISO 15622:2018 since we
    # perform the closed loop control, and might need some
    # to apply some more braking if we're on a downhill slope.
    # Our controller should still keep the 2 second average above
    # -3.5 m/s^2 as per planner limits
    self.ACCEL_MIN = -4.0 # m/s^2

    self.MAX_ACC_REGEN = 1404  # ACC Regen braking is slightly less powerful than max regen paddle
    self.GAS_LOOKUP_BP = [-1.0, 0., self.ACCEL_MAX]
    self.GAS_LOOKUP_V = [self.MAX_ACC_REGEN, ZERO_GAS, MAX_GAS]
    self.BRAKE_LOOKUP_BP = [self.ACCEL_MIN, -1.0]
    self.BRAKE_LOOKUP_V = [MAX_BRAKE, 0]

class CAR:
  VOLT = "HOLDEN VOLT 2013"

class CruiseButtons:
  INIT = 0
  UNPRESS = 1
  RES_ACCEL = 2
  DECEL_SET = 3
  MAIN = 5
  CANCEL = 6

class AccState:
  OFF = 0
  ACTIVE = 1
  FAULTED = 3
  STANDSTILL = 4

class CanBus:
  POWERTRAIN = 0
  OBSTACLE = 1
  CHASSIS = 2
  SW_GMLAN = 3

FINGERPRINTS = {
  CAR.VOLT: [
  # Holden Volt 2013
  # As captured.
  #{
  #  150: 6, 151: 8, 152: 8, 170: 8, 185: 8, 186: 8, 187: 8, 188: 8, 189: 7, 193: 8, 197: 8, 199: 4, 201: 8, 209: 7, 211: 2, 241: 6, 288: 5, 289: 1, 290: 1, 298: 8, 304: 8, 309: 8, 311: 8, 313: 8, 320: 8, 328: 1, 352: 5, 381: 6, 386: 3, 389: 2, 390: 7, 417: 7, 419: 1, 451: 8, 452: 8, 453: 6, 454: 8, 479: 1, 481: 7, 485: 8, 489: 8, 491: 2, 493: 8, 495: 4, 497: 8, 499: 3, 500: 6, 501: 8, 512: 8, 514: 8, 516: 8, 518: 3, 532: 6, 546: 6, 548: 3, 550: 8, 552: 4, 554: 2, 560: 6, 562: 4, 565: 8, 566: 3, 568: 1, 647: 2, 707: 8, 711: 6, 753: 5, 761: 7, 810: 8, 840: 5, 842: 5, 866: 4, 901: 3, 961: 8, 969: 8, 971: 6, 977: 8, 988: 6, 989: 6, 995: 5, 1001: 8, 1005: 6, 1009: 8, 1017: 8, 1019: 2, 1020: 5, 1105: 6, 1217: 8, 1221: 3, 1223: 3, 1225: 4, 1227: 4, 1233: 8, 1239: 5, 1241: 3, 1249: 8, 1257: 6, 1265: 8, 1280: 4, 1300: 8, 1322: 6, 1328: 4, 1417: 7, 1904: 7, 1906: 8, 1907: 7, 1912: 7, 1917: 7, 1919: 7, 1927: 7
  #}],
  # Holden Volt 2013
  # Without flipping values(?); 304, 512, 560
  {
    150: 6, 151: 8, 152: 8, 170: 8, 185: 8, 186: 8, 187: 8, 188: 8, 189: 7, 193: 8, 197: 8, 199: 4, 201: 8, 209: 7, 211: 2, 241: 6, 288: 5, 289: 1, 290: 1, 298: 8, 309: 8, 311: 8, 313: 8, 320: 8, 328: 1, 352: 5, 381: 6, 386: 3, 389: 2, 390: 7, 417: 7, 419: 1, 451: 8, 452: 8, 453: 6, 454: 8, 479: 1, 481: 7, 485: 8, 489: 8, 491: 2, 493: 8, 495: 4, 497: 8, 499: 3, 500: 6, 501: 8, 514: 8, 516: 8, 518: 3, 532: 6, 546: 6, 548: 3, 550: 8, 552: 4, 554: 2, 562: 4, 565: 8, 566: 3, 568: 1, 647: 2, 707: 8, 711: 6, 753: 5, 761: 7, 810: 8, 840: 5, 842: 5, 866: 4, 901: 3, 961: 8, 969: 8, 971: 6, 977: 8, 988: 6, 989: 6, 995: 5, 1001: 8, 1005: 6, 1009: 8, 1017: 8, 1019: 2, 1020: 5, 1105: 6, 1217: 8, 1221: 3, 1223: 3, 1225: 4, 1227: 4, 1233: 8, 1239: 5, 1241: 3, 1249: 8, 1257: 6, 1265: 8, 1280: 4, 1300: 8, 1322: 6, 1328: 4, 1417: 7, 1904: 7, 1906: 8, 1907: 7, 1912: 7, 1917: 7, 1919: 7, 1927: 7
  }],
}

STEER_THRESHOLD = 1.0

DBC = {
  CAR.VOLT: dbc_dict('gm_global_a_powertrain', 'gm_global_a_object', chassis_dbc='gm_global_a_chassis'),
}
