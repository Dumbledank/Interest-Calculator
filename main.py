import matplotlib.pyplot as plt
import matplotlib.dates as mdates
# import numpy as np
import datetime


class Savings:

    def __init__(self, amount=0, time_start=(2020, 1, 1)):
        self.amount = amount
        self.amount_added = 0
        self.interest_rate = .015
        self.days_in_year = 365
        self.time_start = datetime.date(*time_start)  # in form datetime.date(year, month, day)

    def balance(self, time_end=(datetime.date.today().year, datetime.date.today().month,
                                datetime.date.today().day)):
        x = mdates.drange(self.time_start, datetime.date(*time_end), datetime.timedelta(days=.1))
        y = self.amount * (1 + self.interest_rate) ** ((x - mdates.date2num(self.time_start)) / self.days_in_year)
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=50))
        plt.gcf().autofmt_xdate()
        plt.plot(x, y)
        self.amount = self.amount * (1 + self.interest_rate) ** (
                (mdates.date2num(datetime.date(*time_end)) - mdates.date2num(self.time_start)) / self.days_in_year)
        self.time_start = datetime.date(*time_end)

    def add_or_remove_funds(self, quantity, time=(datetime.date.today().year, datetime.date.today().month,
                                                  datetime.date.today().day)):  # +ve quantity if you want to add
        # funds and -ve quantity if you want to remove funds
        self.balance(time)
        if self.amount < -quantity:
            print("Insufficient funds. Request to withdraw has been void.")
            return
        else:
            amount_updated = self.amount + quantity
            plt.vlines(x=mdates.date2num(self.time_start), ymin=self.amount, ymax=amount_updated, color='red')
            self.amount = amount_updated
            self.amount_added += quantity


new = Savings(0, (2020, 1, 20))  # opening position

new.add_or_remove_funds(20000, (2020, 1, 20))

new.add_or_remove_funds(10000, (2020, 2, 12))

new.add_or_remove_funds(1334.55, (2020, 6, 30))

new.add_or_remove_funds(5000, (2020, 8, 16))

new.balance()  # closing position

print(new.amount - new.amount_added)
print(new.amount)
plt.show()
