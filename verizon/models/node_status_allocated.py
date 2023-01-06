# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class NodeStatusAllocated(object):

    """Implementation of the 'NodeStatusAllocated' model.

    TODO: type model description here.

    Attributes:
        cpu_count (int): TODO: type description here.
        memory_kb (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cpu_count": 'cpuCount',
        "memory_kb": 'memoryKB'
    }

    _optionals = [
        'cpu_count',
        'memory_kb',
    ]

    def __init__(self,
                 cpu_count=APIHelper.SKIP,
                 memory_kb=APIHelper.SKIP):
        """Constructor for the NodeStatusAllocated class"""

        # Initialize members of the class
        if cpu_count is not APIHelper.SKIP:
            self.cpu_count = cpu_count 
        if memory_kb is not APIHelper.SKIP:
            self.memory_kb = memory_kb 

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

        cpu_count = dictionary.get("cpuCount") if dictionary.get("cpuCount") else APIHelper.SKIP
        memory_kb = dictionary.get("memoryKB") if dictionary.get("memoryKB") else APIHelper.SKIP
        # Return an object of this model
        return cls(cpu_count,
                   memory_kb)
