# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class ConditionItem(object):

    """Implementation of the 'ConditionItem' model.

    TODO: type model description here.

    Attributes:
        mtype (string): TODO: type description here.
        status (string): TODO: type description here.
        last_updated (string): TODO: type description here.
        reason (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mtype": 'type',
        "status": 'status',
        "last_updated": 'lastUpdated',
        "reason": 'reason'
    }

    _optionals = [
        'mtype',
        'status',
        'last_updated',
        'reason',
    ]

    def __init__(self,
                 mtype=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 last_updated=APIHelper.SKIP,
                 reason=APIHelper.SKIP):
        """Constructor for the ConditionItem class"""

        # Initialize members of the class
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype 
        if status is not APIHelper.SKIP:
            self.status = status 
        if last_updated is not APIHelper.SKIP:
            self.last_updated = last_updated 
        if reason is not APIHelper.SKIP:
            self.reason = reason 

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

        mtype = dictionary.get("type") if dictionary.get("type") else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        last_updated = dictionary.get("lastUpdated") if dictionary.get("lastUpdated") else APIHelper.SKIP
        reason = dictionary.get("reason") if dictionary.get("reason") else APIHelper.SKIP
        # Return an object of this model
        return cls(mtype,
                   status,
                   last_updated,
                   reason)
