# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.edge_service_repository import EdgeServiceRepository
from verizon.models.service_launch_helm_git_branch import ServiceLaunchHelmGitBranch
from verizon.models.service_launch_helm_git_tag import ServiceLaunchHelmGitTag
from verizon.models.service_launch_helm_repo import ServiceLaunchHelmRepo
from verizon.models.service_launch_helm_yaml_git_tag import ServiceLaunchHelmYamlGitTag
from verizon.models.service_launch_terraform_git_branch import ServiceLaunchTerraformGitBranch
from verizon.models.service_launch_terraform_git_tag import ServiceLaunchTerraformGitTag
from verizon.models.service_launch_yaml_git_branch import ServiceLaunchYamlGitBranch


class EdgeServiceWorkload(object):

    """Implementation of the 'EdgeServiceWorkload' model.

    TODO: type model description here.

    Attributes:
        id (string): TODO: type description here.
        name (string): Name of the workload needs to be deployed
        description (string): TODO: type description here.
        package_type (PackageTypeEnum): deployment package type
        upload_type (WorkloadUploadTypeEnum): TODO: type description here.
        repository_type (RepositoryTypeEnum): TODO: type description here.
        repository_id (string): TODO: type description here.
        repository (EdgeServiceRepository): TODO: type description here.
        files (list of string): TODO: type description here.
        revision_type (RevisionTypeEnum): TODO: type description here.
        helm_git_branch (ServiceLaunchHelmGitBranch): TODO: type description
            here.
        helm_git_tag (ServiceLaunchHelmGitTag): TODO: type description here.
        helm_yaml_git_tag (ServiceLaunchHelmYamlGitTag): TODO: type
            description here.
        helm_repo (ServiceLaunchHelmRepo): TODO: type description here.
        yaml_git_branch (ServiceLaunchYamlGitBranch): TODO: type description
            here.
        terraform_git_branch (ServiceLaunchTerraformGitBranch): TODO: type
            description here.
        terraform_git_tag (ServiceLaunchTerraformGitTag): TODO: type
            description here.
        created_date (datetime): TODO: type description here.
        last_modified_dte (datetime): TODO: type description here.
        created_by (string): TODO: type description here.
        updated_by (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "id": 'id',
        "description": 'description',
        "package_type": 'packageType',
        "upload_type": 'uploadType',
        "repository_type": 'repositoryType',
        "repository_id": 'repositoryId',
        "repository": 'repository',
        "files": 'files',
        "revision_type": 'revisionType',
        "helm_git_branch": 'helmGitBranch',
        "helm_git_tag": 'helmGitTag',
        "helm_yaml_git_tag": 'helmYamlGitTag',
        "helm_repo": 'helmRepo',
        "yaml_git_branch": 'yamlGitBranch',
        "terraform_git_branch": 'terraformGitBranch',
        "terraform_git_tag": 'terraformGitTag',
        "created_date": 'createdDate',
        "last_modified_dte": 'lastModifiedDte',
        "created_by": 'createdBy',
        "updated_by": 'updatedBy'
    }

    _optionals = [
        'id',
        'description',
        'package_type',
        'upload_type',
        'repository_type',
        'repository_id',
        'repository',
        'files',
        'revision_type',
        'helm_git_branch',
        'helm_git_tag',
        'helm_yaml_git_tag',
        'helm_repo',
        'yaml_git_branch',
        'terraform_git_branch',
        'terraform_git_tag',
        'created_date',
        'last_modified_dte',
        'created_by',
        'updated_by',
    ]

    _nullables = [
        'description',
        'package_type',
        'upload_type',
        'repository_type',
        'repository_id',
        'revision_type',
    ]

    def __init__(self,
                 name=None,
                 id=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 package_type=APIHelper.SKIP,
                 upload_type=APIHelper.SKIP,
                 repository_type=APIHelper.SKIP,
                 repository_id=APIHelper.SKIP,
                 repository=APIHelper.SKIP,
                 files=APIHelper.SKIP,
                 revision_type=APIHelper.SKIP,
                 helm_git_branch=APIHelper.SKIP,
                 helm_git_tag=APIHelper.SKIP,
                 helm_yaml_git_tag=APIHelper.SKIP,
                 helm_repo=APIHelper.SKIP,
                 yaml_git_branch=APIHelper.SKIP,
                 terraform_git_branch=APIHelper.SKIP,
                 terraform_git_tag=APIHelper.SKIP,
                 created_date=APIHelper.SKIP,
                 last_modified_dte=APIHelper.SKIP,
                 created_by=APIHelper.SKIP,
                 updated_by=APIHelper.SKIP):
        """Constructor for the EdgeServiceWorkload class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        self.name = name 
        if description is not APIHelper.SKIP:
            self.description = description 
        if package_type is not APIHelper.SKIP:
            self.package_type = package_type 
        if upload_type is not APIHelper.SKIP:
            self.upload_type = upload_type 
        if repository_type is not APIHelper.SKIP:
            self.repository_type = repository_type 
        if repository_id is not APIHelper.SKIP:
            self.repository_id = repository_id 
        if repository is not APIHelper.SKIP:
            self.repository = repository 
        if files is not APIHelper.SKIP:
            self.files = files 
        if revision_type is not APIHelper.SKIP:
            self.revision_type = revision_type 
        if helm_git_branch is not APIHelper.SKIP:
            self.helm_git_branch = helm_git_branch 
        if helm_git_tag is not APIHelper.SKIP:
            self.helm_git_tag = helm_git_tag 
        if helm_yaml_git_tag is not APIHelper.SKIP:
            self.helm_yaml_git_tag = helm_yaml_git_tag 
        if helm_repo is not APIHelper.SKIP:
            self.helm_repo = helm_repo 
        if yaml_git_branch is not APIHelper.SKIP:
            self.yaml_git_branch = yaml_git_branch 
        if terraform_git_branch is not APIHelper.SKIP:
            self.terraform_git_branch = terraform_git_branch 
        if terraform_git_tag is not APIHelper.SKIP:
            self.terraform_git_tag = terraform_git_tag 
        if created_date is not APIHelper.SKIP:
            self.created_date = APIHelper.RFC3339DateTime(created_date) if created_date else None 
        if last_modified_dte is not APIHelper.SKIP:
            self.last_modified_dte = APIHelper.RFC3339DateTime(last_modified_dte) if last_modified_dte else None 
        if created_by is not APIHelper.SKIP:
            self.created_by = created_by 
        if updated_by is not APIHelper.SKIP:
            self.updated_by = updated_by 

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

        name = dictionary.get("name") if dictionary.get("name") else None
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        description = dictionary.get("description") if "description" in dictionary.keys() else APIHelper.SKIP
        package_type = dictionary.get("packageType") if "packageType" in dictionary.keys() else APIHelper.SKIP
        upload_type = dictionary.get("uploadType") if "uploadType" in dictionary.keys() else APIHelper.SKIP
        repository_type = dictionary.get("repositoryType") if "repositoryType" in dictionary.keys() else APIHelper.SKIP
        repository_id = dictionary.get("repositoryId") if "repositoryId" in dictionary.keys() else APIHelper.SKIP
        repository = EdgeServiceRepository.from_dictionary(dictionary.get('repository')) if 'repository' in dictionary.keys() else APIHelper.SKIP
        files = dictionary.get("files") if dictionary.get("files") else APIHelper.SKIP
        revision_type = dictionary.get("revisionType") if "revisionType" in dictionary.keys() else APIHelper.SKIP
        helm_git_branch = ServiceLaunchHelmGitBranch.from_dictionary(dictionary.get('helmGitBranch')) if 'helmGitBranch' in dictionary.keys() else APIHelper.SKIP
        helm_git_tag = ServiceLaunchHelmGitTag.from_dictionary(dictionary.get('helmGitTag')) if 'helmGitTag' in dictionary.keys() else APIHelper.SKIP
        helm_yaml_git_tag = ServiceLaunchHelmYamlGitTag.from_dictionary(dictionary.get('helmYamlGitTag')) if 'helmYamlGitTag' in dictionary.keys() else APIHelper.SKIP
        helm_repo = ServiceLaunchHelmRepo.from_dictionary(dictionary.get('helmRepo')) if 'helmRepo' in dictionary.keys() else APIHelper.SKIP
        yaml_git_branch = ServiceLaunchYamlGitBranch.from_dictionary(dictionary.get('yamlGitBranch')) if 'yamlGitBranch' in dictionary.keys() else APIHelper.SKIP
        terraform_git_branch = ServiceLaunchTerraformGitBranch.from_dictionary(dictionary.get('terraformGitBranch')) if 'terraformGitBranch' in dictionary.keys() else APIHelper.SKIP
        terraform_git_tag = ServiceLaunchTerraformGitTag.from_dictionary(dictionary.get('terraformGitTag')) if 'terraformGitTag' in dictionary.keys() else APIHelper.SKIP
        created_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("createdDate")).datetime if dictionary.get("createdDate") else APIHelper.SKIP
        last_modified_dte = APIHelper.RFC3339DateTime.from_value(dictionary.get("lastModifiedDte")).datetime if dictionary.get("lastModifiedDte") else APIHelper.SKIP
        created_by = dictionary.get("createdBy") if dictionary.get("createdBy") else APIHelper.SKIP
        updated_by = dictionary.get("updatedBy") if dictionary.get("updatedBy") else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   id,
                   description,
                   package_type,
                   upload_type,
                   repository_type,
                   repository_id,
                   repository,
                   files,
                   revision_type,
                   helm_git_branch,
                   helm_git_tag,
                   helm_yaml_git_tag,
                   helm_repo,
                   yaml_git_branch,
                   terraform_git_branch,
                   terraform_git_tag,
                   created_date,
                   last_modified_dte,
                   created_by,
                   updated_by)
