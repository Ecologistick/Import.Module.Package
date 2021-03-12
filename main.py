from datetime import *
from application.salary import calculate_salary
from application.people import get_employees


if __name__ == '__main__':
  calculate_salary(2,5)
  get_employees("Виктор")
  today = datetime.today()
  print("{}".format(today.strftime("%Y/%m/%d %H:%M")))
  