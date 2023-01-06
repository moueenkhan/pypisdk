# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.access_intents import AccessIntents
from verizon.models.deployment_location import DeploymentLocation
from verizon.models.linked_service_instance import LinkedServiceInstance
from verizon.models.placement_intents import PlacementIntents


class CreateServiceProfileRequest(object):

    """Implementation of the 'CreateServiceProfileRequest' model.

    TODO: type model description here.

    Attributes:
        name (string): Provide name for Service Profile
        service_name (string): Service being deployed.
        service_version (string): Service version being deployed.
        customer_id (string): Id of particular customer.
        linked_service_instances (list of LinkedServiceInstance): TODO: type
            description here.
        access_intents (AccessIntents): TODO: type description here.
        placement_intents (PlacementIntents): TODO: type description here.
        deployment_locations (list of DeploymentLocation): TODO: type
            description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "service_name": 'serviceName',
        "service_version": 'serviceVersion',
        "customer_id": 'customerID',
        "linked_service_instances": 'linkedServiceInstances',
        "access_intents": 'accessIntents',
        "placement_intents": 'placementIntents',
        "deployment_locations": 'deploymentLocations'
    }

    _optionals = [
        'name',
        'service_name',
        'service_version',
        'customer_id',
        'linked_service_instances',
        'access_intents',
        'placement_intents',
        'deployment_locations',
    ]

    def __init__(self,
                 name=APIHelper.SKIP,
                 service_name=APIHelper.SKIP,
                 service_version=APIHelper.SKIP,
                 customer_id=APIHelper.SKIP,
                 linked_service_instances=APIHelper.SKIP,
                 access_intents=APIHelper.SKIP,
                 placement_intents=APIHelper.SKIP,
                 deployment_locations=APIHelper.SKIP):
        """Constructor for the CreateServiceProfileRequest class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name 
        if service_name is not APIHelper.SKIP:
            self.service_name = service_name 
        if service_version is not APIHelper.SKIP:
            self.service_version = service_version 
        if customer_id is not APIHelper.SKIP:
            self.customer_id = customer_id 
        if linked_service_instances is not APIHelper.SKIP:
            self.linked_service_instances = linked_service_instances 
        if access_intents is not APIHelper.SKIP:
            self.access_intents = access_intents 
        if placement_intents is not APIHelper.SKIP:
            self.placement_intents = placement_intents 
        if deployment_locations is not APIHelper.SKIP:
            self.deployment_locations = deployment_locations 

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

        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        service_name = dictionary.get("serviceName") if dictionary.get("serviceName") else APIHelper.SKIP
        service_version = dictionary.get("serviceVersion") if dictionary.get("serviceVersion") else APIHelper.SKIP
        customer_id = dictionary.get("customerID") if dictionary.get("customerID") else APIHelper.SKIP
        linked_service_instances = None
        if dictionary.get('linkedServiceInstances') is not None:
            linked_service_instances = [LinkedServiceInstance.from_dictionary(x) for x in dictionary.get('linkedServiceInstances')]
        else:
            linked_service_instances = APIHelper.SKIP
        access_intents = AccessIntents.from_dictionary(dictionary.get('accessIntents')) if 'accessIntents' in dictionary.keys() else APIHelper.SKIP
        placement_intents = PlacementIntents.from_dictionary(dictionary.get('placementIntents')) if 'placementIntents' in dictionary.keys() else APIHelper.SKIP
        deployment_locations = None
        if dictionary.get('deploymentLocations') is not None:
            deployment_locations = [DeploymentLocation.from_dictionary(x) for x in dictionary.get('deploymentLocations')]
        else:
            deployment_locations = APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   service_name,
                   service_version,
                   customer_id,
                   linked_service_instances,
                   access_intents,
                   placement_intents,
                   deployment_locations)
