# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.device_id import DeviceId


class DeviceConnectionListRequest(object):

    """Implementation of the 'DeviceConnectionListRequest' model.

    Request to list of network connection events for a device during a
    specified time period.

    Attributes:
        device_id (DeviceId): An identifier for a single device.
        earliest (string): The earliest date and time for which you want
            connection events.
        latest (string): The last date and time for which you want connection
            events.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "device_id": 'deviceId',
        "earliest": 'earliest',
        "latest": 'latest'
    }

    _optionals = [
        'device_id',
        'earliest',
        'latest',
    ]

    def __init__(self,
                 device_id=APIHelper.SKIP,
                 earliest=APIHelper.SKIP,
                 latest=APIHelper.SKIP):
        """Constructor for the DeviceConnectionListRequest class"""

        # Initialize members of the class
        if device_id is not APIHelper.SKIP:
            self.device_id = device_id 
        if earliest is not APIHelper.SKIP:
            self.earliest = earliest 
        if latest is not APIHelper.SKIP:
            self.latest = latest 

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

        device_id = DeviceId.from_dictionary(dictionary.get('deviceId')) if 'deviceId' in dictionary.keys() else APIHelper.SKIP
        earliest = dictionary.get("earliest") if dictionary.get("earliest") else APIHelper.SKIP
        latest = dictionary.get("latest") if dictionary.get("latest") else APIHelper.SKIP
        # Return an object of this model
        return cls(device_id,
                   earliest,
                   latest)
