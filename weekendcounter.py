from datetime import date, timedelta


def checkio(from_date, to_date):
    counter = 0
    days = timedelta(days=1)
    
    if to_date.isoweekday() == 6 or to_date.isoweekday() == 7:
        counter += 1
    
    while from_date < to_date:
        
        if from_date.isoweekday() >= 6:
            counter += 1
        from_date += days
    
    return counter