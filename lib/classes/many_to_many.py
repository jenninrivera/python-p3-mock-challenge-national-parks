class NationalPark:

    def __init__(self, name):
        self.name = name
        self.trips_list = []
        self.visitor_list = []

        
    def trips(self):
        return self.trips_list
    
    def visitors(self):
        return self.visitor_list
    
    def total_visits(self):
        pass
    
    def best_visitor(self):
        pass

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not (hasattr(self, 'name')) and (type(name) == str) and (len(name) >= 3):
            self._name = name


class Trip:

    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date

        Trip.all.append(self)

        self.visitor.trips_list.append(self)

        if not (national_park in self.visitor.national_park_list):
            self.visitor.national_park_list.append(national_park)

        self.national_park.trips_list.append(self)

        if not (visitor in self.national_park.visitor_list):
            self.national_park.visitor_list.append(visitor)

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        if (type(start_date) == str) and (len(start_date) >= 7):
            self._start_date = start_date

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        if (type(end_date) == str) and (len(end_date) >= 7):
            self._end_date = end_date

    @property
    def visitor(self):
        return self._visitor

    @visitor.setter
    def visitor(self, visitor):
        if type(visitor) == Visitor:
            self._visitor = visitor

    @property
    def national_park(self):
        return self._national_park

    @national_park.setter
    def national_park(self, national_park):
        if type(national_park) == NationalPark:
            self._national_park = national_park

class Visitor:

    def __init__(self, name):
        self.name = name
        self.trips_list = []
        self.national_park_list = []
        
    def trips(self):
        return self.trips_list
    
    def national_parks(self):
        return self.national_park_list
    
    def total_visits_at_park(self, park):
        pass

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if (type(name) == str) and (1 <= len(name) <= 15):
            self._name = name