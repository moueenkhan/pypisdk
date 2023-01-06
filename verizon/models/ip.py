# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class IP(object):

    """Implementation of the 'IP' model.

    TODO: type model description here.

    Attributes:
        private_ip (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "private_ip": 'privateIP'
    }

    _optionals = [
        'private_ip',
    ]

    def __init__(self,
                 private_ip=APIHelper.SKIP):
        """Constructor for the IP class"""

        # Initialize members of the class
        if private_ip is not APIHelper.SKIP:
            self.private_ip = private_ip 

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

        private_ip = dictionary.get("privateIP") if dictionary.get("privateIP") else APIHelper.SKIP
        # Return an object of this model
        return cls(private_ip)
