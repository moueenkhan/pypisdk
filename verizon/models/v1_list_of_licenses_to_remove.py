# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class V1ListOfLicensesToRemove(object):

    """Implementation of the 'V1ListOfLicensesToRemove' model.

    List of cancellation candidate devices

    Attributes:
        count (int): The total number of devices on the list.
        has_more_data (bool): True if there are more devices to retrieve.
        update_time (datetime): The date and time that the list was last
            updated.
        device_list (list of string): The IMEIs of the devices.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "count": 'count',
        "has_more_data": 'hasMoreData',
        "update_time": 'updateTime',
        "device_list": 'deviceList'
    }

    _optionals = [
        'count',
        'has_more_data',
        'update_time',
        'device_list',
    ]

    def __init__(self,
                 count=APIHelper.SKIP,
                 has_more_data=APIHelper.SKIP,
                 update_time=APIHelper.SKIP,
                 device_list=APIHelper.SKIP):
        """Constructor for the V1ListOfLicensesToRemove class"""

        # Initialize members of the class
        if count is not APIHelper.SKIP:
            self.count = count 
        if has_more_data is not APIHelper.SKIP:
            self.has_more_data = has_more_data 
        if update_time is not APIHelper.SKIP:
            self.update_time = APIHelper.RFC3339DateTime(update_time) if update_time else None 
        if device_list is not APIHelper.SKIP:
            self.device_list = device_list 

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

        count = dictionary.get("count") if dictionary.get("count") else APIHelper.SKIP
        has_more_data = dictionary.get("hasMoreData") if "hasMoreData" in dictionary.keys() else APIHelper.SKIP
        update_time = APIHelper.RFC3339DateTime.from_value(dictionary.get("updateTime")).datetime if dictionary.get("updateTime") else APIHelper.SKIP
        device_list = dictionary.get("deviceList") if dictionary.get("deviceList") else APIHelper.SKIP
        # Return an object of this model
        return cls(count,
                   has_more_data,
                   update_time,
                   device_list)
