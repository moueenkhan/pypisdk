# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.cloud import Cloud
from verizon.models.cluster_ingress_ip import ClusterIngressIP
from verizon.models.data_center import DataCenter
from verizon.models.edge_service_launch_params import EdgeServiceLaunchParams


class ClusterMetadata(object):

    """Implementation of the 'ClusterMetadata' model.

    TODO: type model description here.

    Attributes:
        name (string): name of the cluster to be used
        description (string): Description of the cluster
        cluster_type (ClusterTypeEnum): TODO: type description here.
        cloud (Cloud): TODO: type description here.
        data_center (DataCenter): TODO: type description here.
        labels (list of EdgeServiceLaunchParams): TODO: type description
            here.
        ingress_ips (ClusterIngressIP): TODO: type description here.
        upgrade_protection (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "description": 'description',
        "cluster_type": 'clusterType',
        "cloud": 'cloud',
        "data_center": 'dataCenter',
        "labels": 'labels',
        "ingress_ips": 'ingressIps',
        "upgrade_protection": 'upgradeProtection'
    }

    _optionals = [
        'name',
        'description',
        'cluster_type',
        'cloud',
        'data_center',
        'labels',
        'ingress_ips',
        'upgrade_protection',
    ]

    def __init__(self,
                 name=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 cluster_type=APIHelper.SKIP,
                 cloud=APIHelper.SKIP,
                 data_center=APIHelper.SKIP,
                 labels=APIHelper.SKIP,
                 ingress_ips=APIHelper.SKIP,
                 upgrade_protection=APIHelper.SKIP):
        """Constructor for the ClusterMetadata class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name 
        if description is not APIHelper.SKIP:
            self.description = description 
        if cluster_type is not APIHelper.SKIP:
            self.cluster_type = cluster_type 
        if cloud is not APIHelper.SKIP:
            self.cloud = cloud 
        if data_center is not APIHelper.SKIP:
            self.data_center = data_center 
        if labels is not APIHelper.SKIP:
            self.labels = labels 
        if ingress_ips is not APIHelper.SKIP:
            self.ingress_ips = ingress_ips 
        if upgrade_protection is not APIHelper.SKIP:
            self.upgrade_protection = upgrade_protection 

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
        description = dictionary.get("description") if dictionary.get("description") else APIHelper.SKIP
        cluster_type = dictionary.get("clusterType") if dictionary.get("clusterType") else APIHelper.SKIP
        cloud = Cloud.from_dictionary(dictionary.get('cloud')) if 'cloud' in dictionary.keys() else APIHelper.SKIP
        data_center = DataCenter.from_dictionary(dictionary.get('dataCenter')) if 'dataCenter' in dictionary.keys() else APIHelper.SKIP
        labels = None
        if dictionary.get('labels') is not None:
            labels = [EdgeServiceLaunchParams.from_dictionary(x) for x in dictionary.get('labels')]
        else:
            labels = APIHelper.SKIP
        ingress_ips = ClusterIngressIP.from_dictionary(dictionary.get('ingressIps')) if 'ingressIps' in dictionary.keys() else APIHelper.SKIP
        upgrade_protection = dictionary.get("upgradeProtection") if "upgradeProtection" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   description,
                   cluster_type,
                   cloud,
                   data_center,
                   labels,
                   ingress_ips,
                   upgrade_protection)
