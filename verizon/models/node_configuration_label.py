# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class NodeConfigurationLabel(object):

    """Implementation of the 'NodeConfigurationLabel' model.

    TODO: type model description here.

    Attributes:
        placement (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "placement": 'placement'
    }

    _optionals = [
        'placement',
    ]

    def __init__(self,
                 placement=APIHelper.SKIP):
        """Constructor for the NodeConfigurationLabel class"""

        # Initialize members of the class
        if placement is not APIHelper.SKIP:
            self.placement = placement 

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

        placement = dictionary.get("placement") if dictionary.get("placement") else APIHelper.SKIP
        # Return an object of this model
        return cls(placement)
