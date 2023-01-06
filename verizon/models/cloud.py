# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.advance_configuration import AdvanceConfiguration
from verizon.models.cluster_configuration import ClusterConfiguration
from verizon.models.common_configuration import CommonConfiguration
from verizon.models.node_configuration import NodeConfiguration


class Cloud(object):

    """Implementation of the 'Cloud' model.

    TODO: type model description here.

    Attributes:
        provider (CloudProviderEnum): Cloud provider where you plan to
            provision and operate your Kubernetes cluster
        distribution (CloudDestributionEnum): Supported Kubernetes
            distribution for the selected cloud provider
        common_config (CommonConfiguration): TODO: type description here.
        cluster_config (ClusterConfiguration): TODO: type description here.
        node_config (NodeConfiguration): TODO: type description here.
        node_configs (list of NodeConfiguration): TODO: type description
            here.
        advance_config (AdvanceConfiguration): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "provider": 'provider',
        "distribution": 'distribution',
        "common_config": 'commonConfig',
        "cluster_config": 'clusterConfig',
        "node_config": 'nodeConfig',
        "node_configs": 'nodeConfigs',
        "advance_config": 'advanceConfig'
    }

    _optionals = [
        'provider',
        'distribution',
        'common_config',
        'cluster_config',
        'node_config',
        'node_configs',
        'advance_config',
    ]

    def __init__(self,
                 provider=APIHelper.SKIP,
                 distribution=APIHelper.SKIP,
                 common_config=APIHelper.SKIP,
                 cluster_config=APIHelper.SKIP,
                 node_config=APIHelper.SKIP,
                 node_configs=APIHelper.SKIP,
                 advance_config=APIHelper.SKIP):
        """Constructor for the Cloud class"""

        # Initialize members of the class
        if provider is not APIHelper.SKIP:
            self.provider = provider 
        if distribution is not APIHelper.SKIP:
            self.distribution = distribution 
        if common_config is not APIHelper.SKIP:
            self.common_config = common_config 
        if cluster_config is not APIHelper.SKIP:
            self.cluster_config = cluster_config 
        if node_config is not APIHelper.SKIP:
            self.node_config = node_config 
        if node_configs is not APIHelper.SKIP:
            self.node_configs = node_configs 
        if advance_config is not APIHelper.SKIP:
            self.advance_config = advance_config 

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

        provider = dictionary.get("provider") if dictionary.get("provider") else APIHelper.SKIP
        distribution = dictionary.get("distribution") if dictionary.get("distribution") else APIHelper.SKIP
        common_config = CommonConfiguration.from_dictionary(dictionary.get('commonConfig')) if 'commonConfig' in dictionary.keys() else APIHelper.SKIP
        cluster_config = ClusterConfiguration.from_dictionary(dictionary.get('clusterConfig')) if 'clusterConfig' in dictionary.keys() else APIHelper.SKIP
        node_config = NodeConfiguration.from_dictionary(dictionary.get('nodeConfig')) if 'nodeConfig' in dictionary.keys() else APIHelper.SKIP
        node_configs = None
        if dictionary.get('nodeConfigs') is not None:
            node_configs = [NodeConfiguration.from_dictionary(x) for x in dictionary.get('nodeConfigs')]
        else:
            node_configs = APIHelper.SKIP
        advance_config = AdvanceConfiguration.from_dictionary(dictionary.get('advanceConfig')) if 'advanceConfig' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(provider,
                   distribution,
                   common_config,
                   cluster_config,
                   node_config,
                   node_configs,
                   advance_config)
