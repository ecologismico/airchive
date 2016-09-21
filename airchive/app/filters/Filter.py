#!/usr/bin/env python
from abc import ABCMeta, abstractmethod, abstractproperty

# see http://www.daveoncode.com/2014/10/07/abstract-classes-in-python-using-abc-module/


class AbstractFilter(object):
    __metaclass__ = ABCMeta

    _properties = {"filter_name": "abstract_filter",
                   "parameter1" : "not used", "parameter1_prompt": "disabled", "parameter1_tooltip": "",
                   "parameter2" : "not used", "parameter2_prompt": "disabled", "parameter2_tooltip": ""}

    @abstractmethod
    def __init__(self, inputs):

        self._result = None
        if not inputs:  # list is empty
            raise RuntimeError("Inputs list for filter " + self._properties["filter_name"] + " is empty.")
        else:

            self._inputs = inputs

    @abstractmethod
    def apply(self):
        """
        Applies this filter to its inputs to produce the desired output.
        Returns the MeasurementSet object produced.
        :return: MeasurementSet
        """
        pass

    def getResult(self):
        """
        Returns the MeasurementSet result object.
        :return: MeasurementSet
        """
        return self._result

