# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.mec_performance_query_result import MECPerformanceQueryResult


class MECPerformanceMetrics(object):

    """Implementation of the 'MECPerformanceMetrics' model.

    Response to query the most recent data for Key Performance Indicators
    (KPIs) like network availability, MEC hostnames and more.

    Attributes:
        query_status (string): Success or Failed
        start (string): Timestamp of the query's start,
            format:mm/dd/yyyy,hr:min:sec
        end (string): Timestamp of the query's end , format:mm/dd/yyyy,
            hr:min:sec
        query_result (list of MECPerformanceQueryResult): Result of the query
            to fetch the most recent data for Key Performance Indicators
            (KPIs) like network availability, MEC hostnames and more.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "query_status": 'QueryStatus',
        "start": 'Start',
        "end": 'End',
        "query_result": 'QueryResult'
    }

    _optionals = [
        'query_status',
        'start',
        'end',
        'query_result',
    ]

    def __init__(self,
                 query_status=APIHelper.SKIP,
                 start=APIHelper.SKIP,
                 end=APIHelper.SKIP,
                 query_result=APIHelper.SKIP):
        """Constructor for the MECPerformanceMetrics class"""

        # Initialize members of the class
        if query_status is not APIHelper.SKIP:
            self.query_status = query_status 
        if start is not APIHelper.SKIP:
            self.start = start 
        if end is not APIHelper.SKIP:
            self.end = end 
        if query_result is not APIHelper.SKIP:
            self.query_result = query_result 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary

        query_status = dictionary.get("QueryStatus") if dictionary.get("QueryStatus") else APIHelper.SKIP
        start = dictionary.get("Start") if dictionary.get("Start") else APIHelper.SKIP
        end = dictionary.get("End") if dictionary.get("End") else APIHelper.SKIP
        query_result = None
        if dictionary.get('QueryResult') is not None:
            query_result = [MECPerformanceQueryResult.from_dictionary(x) for x in dictionary.get('QueryResult')]
        else:
            query_result = APIHelper.SKIP
        # Return an object of this model
        return cls(query_status,
                   start,
                   end,
                   query_result)
