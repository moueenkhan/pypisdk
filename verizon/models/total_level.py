# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.aggregate_usage_error import AggregateUsageError
from verizon.models.aggregate_usage_item import AggregateUsageItem


class TotalLevel(object):

    """Implementation of the 'TotalLevel' model.

    Session and usage details for up to 10 devices.

    Attributes:
        txid (string): A unique string that associates the request with the
            location report information that is sent in asynchronous callback
            message.ThingSpace will send a separate callback message for each
            device that was in the request. All of the callback messages will
            have the same txid.
        usage (list of AggregateUsageItem): Contains usage per device
        errors (list of AggregateUsageError): An object containing any errors
            reported by the device.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "txid": 'txid',
        "usage": 'usage',
        "errors": 'errors'
    }

    _optionals = [
        'usage',
        'errors',
    ]

    def __init__(self,
                 txid=None,
                 usage=APIHelper.SKIP,
                 errors=APIHelper.SKIP):
        """Constructor for the TotalLevel class"""

        # Initialize members of the class
        self.txid = txid 
        if usage is not APIHelper.SKIP:
            self.usage = usage 
        if errors is not APIHelper.SKIP:
            self.errors = errors 

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

        txid = dictionary.get("txid") if dictionary.get("txid") else None
        usage = None
        if dictionary.get('usage') is not None:
            usage = [AggregateUsageItem.from_dictionary(x) for x in dictionary.get('usage')]
        else:
            usage = APIHelper.SKIP
        errors = None
        if dictionary.get('errors') is not None:
            errors = [AggregateUsageError.from_dictionary(x) for x in dictionary.get('errors')]
        else:
            errors = APIHelper.SKIP
        # Return an object of this model
        return cls(txid,
                   usage,
                   errors)
