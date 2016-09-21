#!/usr/bin/env python
import datetime
import re
from Filter import AbstractFilter
import pandas as pd
import sys

# see http://www.daveoncode.com/2014/10/07/abstract-classes-in-python-using-abc-module/


class FilterMax(AbstractFilter):
    """
    Calculates the average measured values in a MeasurementSet.
    """ """
    Class attributes:
        _properties: A dictionary with information about this filter, or this filter instance.
        _input: The source MeasurementList object(s) for this filter.
        _outputID: The string ID of the MeasurementList object to be constructed.
        _result: The resulting MeasurementList object.
    """

    def __init__(self, source=None, granularity=None, *others):
        """
        Initialise _properties of this filter, check input and output.
        Granularity should be given as _w_d_h_m_s (weeks, days, hours, minutes, seconds, missing values
        are acceptable. For example: 1h30m. If no granularity is given, default becomes 1h.
        :param out: The ID of the output MeasurementSet object.
        :type out: str
        :param source: MeasurementSet object that will serve as source
        :type source: MeasurementSet
        :param granularity: granularity of averages, ie. average over each span of this duration
        :type granularity: str
        """
        p_date = re.compile(
            "(\d*w)?(\d*d)?(\d*h)?(\d*m)?(\d*s)?$")  # pattern to extract details from granularity string

        self._properties["filter_name"] = "average"
        self._properties["parameter1"] = "f_gran"
        self._properties["parameter1_prompt"] = "filter granularity"
        self._properties["parameter1_tooltip"] = "Enter filter granularity in [w]eeks, [d]ays, " \
                                                 "[h]ours, [m]inutes and [s]econds, or any combination." \
                                                 " Example: 1h30m"
        self._input = source

        if granularity is None or granularity == "":
            print("No granularity given for max filter, defaulting to 1 hour.")
            self._granularity = datetime.timedelta(hours=1)
        else:
            try:
                res = list(p_date.match(granularity).groups())
                t = {"w": 0, "d": 0, "h": 0, "m": 0, "s": 0} # weeks, days, hours, minutes, seconds set to 0 by default
                for item in res:
                    if item is not None:
                        t[item[-1]] = int(item[:-1])
            except:
                print("Granularity format invalid. Using default.")
                t = {"w": 0, "d": 0, "h": 1, "m": 0, "s": 0}
            self._granularity = datetime.timedelta(weeks=t["w"], days=t["d"], hours=t["h"], minutes=t["m"],
                                                   seconds=t["s"])

    def apply(self):
        """
        Applies this filter to its input to produce the desired output.
        Returns the MeasurementSet object produced.
        """
        if self._input is None or self._input is "":
            raise ValueError("Input for filter " + self._properties["filter_name"] + " is empty.")
    
        measurements = self._input
        limit = measurements[0].timestamp + self._granularity
        max = []
        max_temp = []

        for measurement in measurements:
            if measurement.timestamp <= limit:
                max_temp.append((float(measurement.value), measurement.timestamp))
            else:
                df = pd.DataFrame(max_temp)
                measure = measurement
                measure.value = str(df.max().tolist()[0])
                measure.timestamp = df.max().tolist()[1].to_datetime()
                measure.id = None
                max.append(measure)
                max_temp = []
                limit = measurement.timestamp + self._granularity
            
        # just in case granularity is bigger than totime-fromtime
        if max ==[]:
            df = pd.DataFrame(max_temp)
            measure = measurement
            measure.value = str(df.max().tolist()[0])
            measure.timestamp = df.max().tolist()[1].to_datetime()
            measure.id = None
            max.append(measure)

        

        self._result = max

        return self._result