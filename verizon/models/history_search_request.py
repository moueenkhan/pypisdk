# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.history_search_filter import HistorySearchFilter
from verizon.models.history_search_limit_time import HistorySearchLimitTime


class HistorySearchRequest(object):

    """Implementation of the 'HistorySearchRequest' model.

    Used to filter data by time period or number of devices.

    Attributes:
        filter (HistorySearchFilter): The selected device and attributes for
            which a request should retrieve data.
        limit_number (int): The maximum number of historical attributes to
            include in the response. If the request matches more than this
            number of attributes, the response will contain an X-Next value in
            the header that can be used as the page value in the next request
            to retrieve the next page of events.
        limit_time (HistorySearchLimitTime): The time period for which a
            request should retrieve data, beginning with the limitTime.startOn
            and proceeding with the limitTime.duration.
        page (string): Page number for pagination purposes.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "filter": '$filter',
        "limit_number": '$limitNumber',
        "limit_time": '$limitTime',
        "page": '$page'
    }

    _optionals = [
        'limit_number',
        'limit_time',
        'page',
    ]

    def __init__(self,
                 filter=None,
                 limit_number=APIHelper.SKIP,
                 limit_time=APIHelper.SKIP,
                 page=APIHelper.SKIP):
        """Constructor for the HistorySearchRequest class"""

        # Initialize members of the class
        self.filter = filter 
        if limit_number is not APIHelper.SKIP:
            self.limit_number = limit_number 
        if limit_time is not APIHelper.SKIP:
            self.limit_time = limit_time 
        if page is not APIHelper.SKIP:
            self.page = page 

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

        filter = HistorySearchFilter.from_dictionary(dictionary.get('$filter')) if dictionary.get('$filter') else None
        limit_number = dictionary.get("$limitNumber") if dictionary.get("$limitNumber") else APIHelper.SKIP
        limit_time = HistorySearchLimitTime.from_dictionary(dictionary.get('$limitTime')) if '$limitTime' in dictionary.keys() else APIHelper.SKIP
        page = dictionary.get("$page") if dictionary.get("$page") else APIHelper.SKIP
        # Return an object of this model
        return cls(filter,
                   limit_number,
                   limit_time,
                   page)
