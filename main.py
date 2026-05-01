import dateutil.parser
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta

class DatePicker:
    def __init__(self, date=None):
        self.date = date or datetime.now()

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = dateutil.parser.parse(date)

    def add_days(self, days):
        self.date += timedelta(days=days)

    def add_months(self, months):
        self.date += relativedelta(months=months)

    def add_years(self, years):
        self.date += relativedelta(years=years)

    def subtract_days(self, days):
        self.date -= timedelta(days=days)

    def subtract_months(self, months):
        self.date -= relativedelta(months=months)

    def subtract_years(self, years):
        self.date -= relativedelta(years=years)

    def get_previous_month(self):
        return self.date.replace(day=1) - timedelta(days=1)

    def get_next_month(self):
        return self.date.replace(day=1) + timedelta(days=32)

    def get_previous_year(self):
        return self.date.replace(month=1, day=1) - timedelta(days=365)

    def get_next_year(self):
        return self.date.replace(month=1, day=1) + timedelta(days=365)

    def get_current_year(self):
        return self.date.year

    def get_current_month(self):
        return self.date.month

    def get_current_day(self):
        return self.date.day

    def get_first_day_of_month(self):
        return self.date.replace(day=1)

    def get_last_day_of_month(self):
        return self.date.replace(day=28) + timedelta(days=4)

    def get_days_in_month(self):
        return (self.date.replace(day=28) + timedelta(days=4)).day - 1

    def get_days_in_year(self):
        return 366 if self.date.year % 4 == 0 and (self.date.year % 100 != 0 or self.date.year % 400 == 0) else 365

    def get_days_in_week(self):
        return self.date.weekday() + 1

    def get_day_name(self):
        return ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][self.date.weekday()]

    def get_month_name(self):
        return ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"][self.date.month - 1]

    def get_year_name(self):
        return str(self.date.year)

    def get_date_string(self):
        return self.date.strftime("%Y-%m-%d")

    def get_date_object(self):
        return self.date

    def get_date_components(self):
        return {
            "year": self.date.year,
            "month": self.date.month,
            "day": self.date.day
        }

    def get_date_components_string(self):
        return f"{self.date.year}-{self.date.month}-{self.date.day}"

    def get_date_components_object(self):
        return {
            "year": self.date.year,
            "month": self.date.month,
            "day": self.date.day
        }

    def get_date_components_list(self):
        return [self.date.year, self.date.month, self.date.day]

    def get_date_components_tuple(self):
        return (self.date.year, self.date.month, self.date.day)

    def get_date_components_dict(self):
        return {
            "year": self.date.year,
            "month": self.date.month,
            "day": self.date.day
        }

    def get_date_components_set(self):
        return {
            "year": self.date.year,
            "month": self.date.month,
            "day": self.date.day
        }

    def get_date_components_frozenset(self):
        return frozenset({
            "year": self.date.year,
            "month": self.date.month,
            "day": self.date.day
        })

    def get_date_components_ordered_dict(self):
        return {
            "year": self.date.year,
            "month": self.date.month,
            "day": self.date.day
        }

    def get_date_components_default_dict(self):
        return {
            "year": self.date.year,
            "month": self.date.month,
            "day": self.date.day
        }

    def get_date_components_counter(self):
        return {
            "year": self.date.year,
            "month": self.date.month,
            "day": self.date.day
        }

    def get_date_components_named_tuple(self):
        return (
            self.date.year,
            self.date.month,
            self.date.day
        )

    def get_date_components_named_tuple_with_names(self):
        return (
            ("year", self.date.year),
            ("month", self.date.month),
            ("day", self.date.day)
        )

    def get_date_components_named_tuple_with_names_and_types(self):
        return (
            ("year", int, self.date.year),
            ("month", int, self.date.month),
            ("day", int, self.date.day)
        )

    def get_date_components_named_tuple_with_names_and_types_and_defaults(self):
        return (
            ("year", int, self.date.year, 0),
            ("month", int, self.date.month, 1),
            ("day", int, self.date.day, 1)
        )

    def get_date_components_named_tuple_with_names_and_types_and_defaults_and_docstrings(self):
        return (
            ("year", int, self.date.year, 0, "The year of the date"),
            ("month", int, self.date.month, 1, "The month of the date"),
            ("day", int, self.date.day, 1, "The day of the date")
        )

    def get_date_components_named_tuple_with_names_and_types_and_defaults_and_docstrings_and_annotations(self):
        return (
            ("year", int, self.date.year, 0, "The year of the date", "The year of the date"),
            ("month", int, self.date.month, 1, "The month of the date", "The month of the date"),
            ("day", int, self.date.day, 1, "The day of the date", "The day of the date")
        )

    def get_date_components_named_tuple_with_names_and_types_and_defaults_and_docstrings_and_annotations_and_type_hints(self):
        return (
            ("year", int, self.date.year, 0, "The year of the date", "The year of the date", "The year of the date"),
            ("month", int, self.date.month, 1, "The month of the date", "The month of the date", "The month of the date"),
            ("day", int, self.date.day, 1, "The day of the date", "The day of the date", "The day of the date")
        )

    def get_date_components_named_tuple_with_names_and_types_and_defaults_and_docstrings_and_annotations_and_type_hints_and_docstrings_with_type_hints(self):
        return (
            ("year", int, self.date.year, 0, "The year of the date", "The year of the date", "The year of the date", "The year of the date"),
            ("month", int, self.date.month, 1, "The month of the date", "The month of the date", "The month of the date", "The month of the date"),
            ("day", int, self.date.day, 1, "The day of the date", "The day of the date", "The day of the date", "The day of the date")
        )

    def get_date_components_named_tuple_with_names_and_types_and_defaults_and_docstrings_and_annotations_and_type_hints_and_docstrings_with_type_hints_and_annotations(self):
        return (
            ("year", int, self.date.year, 0, "The year of the date", "The year of the date", "The year of the date", "The year of the date", "The year of the date"),
            ("month", int, self.date.month, 1, "The month of the date", "The month of the date", "The month of the date", "The month of the date", "The month of the date"),
            ("day", int, self.date.day, 1, "The day of the date", "The day of the date", "The day of the date", "The day of the date", "The day of the date")
        )

    def get_date_components_named_tuple_with_names_and_types_and_defaults_and_docstrings_and_annotations_and_type_hints_and_docstrings_with_type_hints_and_annotations_and_type_hints(self):
        return (
            ("year", int, self.date.year, 0, "The year of the date", "The year of the date", "The year of the date", "The year of the date", "The year of the date", "The year of the date"),
            ("month", int, self.date.month, 1, "The month of the date", "The month of the date", "The month of the date", "The month of the date", "The month of the date", "The month of the date"),
            ("day", int, self.date.day, 1, "The day of the date", "The day of the date", "The day of the date", "The day of the date", "The day of the date", "The day of the date")
        )

    def get_date_components_named_tuple_with_names_and_types_and_defaults_and_docstrings_and_annotations_and_type_hints_and_docstrings_with_type_hints_and_annotations_and_type_h
