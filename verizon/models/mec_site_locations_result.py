# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.mec_site_location import MECSiteLocation


class MECSiteLocationsResult(object):

    """Implementation of the 'MECSiteLocationsResult' model.

    TODO: type model description here.

    Attributes:
        mecsites (list of MECSiteLocation): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mecsites": 'mecsites'
    }

    _optionals = [
        'mecsites',
    ]

    def __init__(self,
                 mecsites=APIHelper.SKIP):
        """Constructor for the MECSiteLocationsResult class"""

        # Initialize members of the class
        if mecsites is not APIHelper.SKIP:
            self.mecsites = mecsites 

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

        mecsites = None
        if dictionary.get('mecsites') is not None:
            mecsites = [MECSiteLocation.from_dictionary(x) for x in dictionary.get('mecsites')]
        else:
            mecsites = APIHelper.SKIP
        # Return an object of this model
        return cls(mecsites)
