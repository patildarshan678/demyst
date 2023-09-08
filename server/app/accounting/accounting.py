from datetime import datetime, timedelta
class Accounting:
    def __init__(self) -> None:
        pass

    def fetch_balance_sheet(self):
        try:
            sheet = [
                {
                    "year": 2020,
                    "month": 12,
                    "profitOrLoss": 250000,
                    "assetsValue": 1234
                },
                {
                    "year": 2020,
                    "month": 11,
                    "profitOrLoss": 1150,
                    "assetsValue": 5789
                },
                {
                    "year": 2020,
                    "month": 10,
                    "profitOrLoss": 2500,
                    "assetsValue": 22345
                },
                {
                    "year": 2020,
                    "month": 9,
                    "profitOrLoss": -187000,
                    "assetsValue": 223452
                }
            ]
            return sheet
        except BaseException as err:
            msg = f'Exception occured in fetch_balance_sheet.{err}'
            print(msg)
            return False
        
    def summarise_outcome(self,sheet,requested_loan):
        try:
            preAssesment = 20
            current_date = datetime.today()
            last_12_months_date = current_date - timedelta(days=30*12)
            last_year = last_12_months_date.year
            last_month = last_12_months_date.month
            last_12_assest = 0
            for row in sheet:
                year,month,profitorloss,assetsValue = row.values()
                if profitorloss < 0:
                    loss = profitorloss
                else:
                    profit = profitorloss
                if year <= last_year and month <=last_month and profit:
                    preAssesment = 60
                    last_12_assest = last_12_assest + assetsValue
            asset_avg = last_12_assest / len(sheet)
            if asset_avg >requested_loan:
                preAssesment = 100
            approved_loan = (preAssesment * requested_loan) / 100
            return approved_loan, preAssesment
        except BaseException as err:
            msg = f" Exception occured in summarise_outcome.{err}"
            print(msg)
            return False