from utils.DateFormat import DateFormat
class Employed():
    def __init__(self, id, name=None, charge=None, salary=None, startdate=None):
        self.id=id
        self.name=name
        self.charge=charge
        self.salary=salary
        self.startdate=startdate

    def to_JSON(self):
        return {
            'id':self.id, 'name':self.name, 'charge':self.charge, 'salary':self.salary, 'startdate': DateFormat.convert_date(self.startdate)
        }