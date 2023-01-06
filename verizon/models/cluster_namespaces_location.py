# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class ClusterNamespacesLocation(object):

    """Implementation of the 'ClusterNamespacesLocation' model.

    TODO: type model description here.

    Attributes:
        ern (string): Edge Resource Number
        city (string): TODO: type description here.
        latitude (string): TODO: type description here.
        longitude (string): TODO: type description here.
        csp (string): Cloud Service Provider

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ern": 'ern',
        "city": 'city',
        "latitude": 'latitude',
        "longitude": 'longitude',
        "csp": 'csp'
    }

    _optionals = [
        'ern',
        'city',
        'latitude',
        'longitude',
        'csp',
    ]

    def __init__(self,
                 ern=APIHelper.SKIP,
                 city=APIHelper.SKIP,
                 latitude=APIHelper.SKIP,
                 longitude=APIHelper.SKIP,
                 csp=APIHelper.SKIP):
        """Constructor for the ClusterNamespacesLocation class"""

        # Initialize members of the class
        if ern is not APIHelper.SKIP:
            self.ern = ern 
        if city is not APIHelper.SKIP:
            self.city = city 
        if latitude is not APIHelper.SKIP:
            self.latitude = latitude 
        if longitude is not APIHelper.SKIP:
            self.longitude = longitude 
        if csp is not APIHelper.SKIP:
            self.csp = csp 

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

        ern = dictionary.get("ern") if dictionary.get("ern") else APIHelper.SKIP
        city = dictionary.get("city") if dictionary.get("city") else APIHelper.SKIP
        latitude = dictionary.get("latitude") if dictionary.get("latitude") else APIHelper.SKIP
        longitude = dictionary.get("longitude") if dictionary.get("longitude") else APIHelper.SKIP
        csp = dictionary.get("csp") if dictionary.get("csp") else APIHelper.SKIP
        # Return an object of this model
        return cls(ern,
                   city,
                   latitude,
                   longitude,
                   csp)
