# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T13:43:12+00:00

from __future__ import annotations

from enum import Enum
from typing import Any, List, Optional

from pydantic import BaseModel, Field, RootModel, conint


class BadRequestException(RootModel[Any]):
    root: Any


class Capability(Enum):
    CAPABILITY_IAM = 'CAPABILITY_IAM'
    CAPABILITY_NAMED_IAM = 'CAPABILITY_NAMED_IAM'
    CAPABILITY_AUTO_EXPAND = 'CAPABILITY_AUTO_EXPAND'
    CAPABILITY_RESOURCE_POLICY = 'CAPABILITY_RESOURCE_POLICY'


class ConflictException(RootModel[Any]):
    root: Any


class DeleteApplicationRequest(BaseModel):
    pass


class ForbiddenException(RootModel[Any]):
    root: Any


class GetApplicationPolicyRequest(BaseModel):
    pass


class GetApplicationRequest(BaseModel):
    pass


class GetCloudFormationTemplateRequest(BaseModel):
    pass


class InternalServerErrorException(RootModel[Any]):
    root: Any


class ListApplicationDependenciesRequest(BaseModel):
    pass


class ListApplicationVersionsRequest(BaseModel):
    pass


class ListApplicationsRequest(BaseModel):
    pass


class MaxItems(RootModel[conint(ge=1, le=100)]):
    root: conint(ge=1, le=100)


class NotFoundException(RootModel[Any]):
    root: Any


class Status(Enum):
    PREPARING = 'PREPARING'
    ACTIVE = 'ACTIVE'
    EXPIRED = 'EXPIRED'


class TooManyRequestsException(RootModel[Any]):
    root: Any


class FieldBoolean(RootModel[bool]):
    root: bool


class FieldInteger(RootModel[int]):
    root: int


class FieldListOfCapability(RootModel[List[Capability]]):
    root: List[Capability]


class FieldString(RootModel[str]):
    root: str


class ApplicationsPostRequest(BaseModel):
    author: str = Field(
        ...,
        description='<p>The name of the author publishing the app.</p><p>Minimum length=1. Maximum length=127.</p><p>Pattern "^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$";</p>',
    )
    description: str = Field(
        ...,
        description='<p>The description of the application.</p><p>Minimum length=1. Maximum length=256</p>',
    )
    homePageUrl: Optional[str] = Field(
        None,
        description='A URL with more information about the application, for example the location of your GitHub repository for the application.',
    )
    labels: Optional[List[FieldString]] = Field(
        None,
        description='<p>Labels to improve discovery of apps in search results.</p><p>Minimum length=1. Maximum length=127. Maximum number of labels: 10</p><p>Pattern: "^[a-zA-Z0-9+\\\\-_:\\\\/@]+$";</p>',
    )
    licenseBody: Optional[str] = Field(
        None,
        description='<p>A local text file that contains the license of the app that matches the spdxLicenseID value of your application.\n The file has the format file://&lt;path>/&lt;filename>.</p><p>Maximum size 5 MB</p><p>You can specify only one of licenseBody and licenseUrl; otherwise, an error results.</p>',
    )
    licenseUrl: Optional[str] = Field(
        None,
        description='<p>A link to the S3 object that contains the license of the app that matches the spdxLicenseID value of your application.</p><p>Maximum size 5 MB</p><p>You can specify only one of licenseBody and licenseUrl; otherwise, an error results.</p>',
    )
    name: str = Field(
        ...,
        description='<p>The name of the application that you want to publish.</p><p>Minimum length=1. Maximum length=140</p><p>Pattern: "[a-zA-Z0-9\\\\-]+";</p>',
    )
    readmeBody: Optional[str] = Field(
        None,
        description='<p>A local text readme file in Markdown language that contains a more detailed description of the application and how it works.\n The file has the format file://&lt;path>/&lt;filename>.</p><p>Maximum size 5 MB</p><p>You can specify only one of readmeBody and readmeUrl; otherwise, an error results.</p>',
    )
    readmeUrl: Optional[str] = Field(
        None,
        description='<p>A link to the S3 object in Markdown language that contains a more detailed description of the application and how it works.</p><p>Maximum size 5 MB</p><p>You can specify only one of readmeBody and readmeUrl; otherwise, an error results.</p>',
    )
    semanticVersion: Optional[str] = Field(
        None,
        description='<p>The semantic version of the application:</p><p>\n <a href="https://semver.org/">https://semver.org/</a>\n </p>',
    )
    sourceCodeArchiveUrl: Optional[str] = Field(
        None,
        description='<p>A link to the S3 object that contains the ZIP archive of the source code for this version of your application.</p><p>Maximum size 50 MB</p>',
    )
    sourceCodeUrl: Optional[str] = Field(
        None,
        description='A link to a public repository for the source code of your application, for example the URL of a specific GitHub commit.',
    )
    spdxLicenseId: Optional[str] = Field(
        None,
        description='A valid identifier from <a href="https://spdx.org/licenses/">https://spdx.org/licenses/</a>.',
    )
    templateBody: Optional[str] = Field(
        None,
        description='<p>The local raw packaged AWS SAM template file of your application.\n The file has the format file://&lt;path>/&lt;filename>.</p><p>You can specify only one of templateBody and templateUrl; otherwise an error results.</p>',
    )
    templateUrl: Optional[str] = Field(
        None,
        description='<p>A link to the S3 object containing the packaged AWS SAM template of your application.</p><p>You can specify only one of templateBody and templateUrl; otherwise an error results.</p>',
    )


class ApplicationsApplicationIdPatchRequest(BaseModel):
    author: Optional[str] = Field(
        None,
        description='<p>The name of the author publishing the app.</p><p>Minimum length=1. Maximum length=127.</p><p>Pattern "^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$";</p>',
    )
    description: Optional[str] = Field(
        None,
        description='<p>The description of the application.</p><p>Minimum length=1. Maximum length=256</p>',
    )
    homePageUrl: Optional[str] = Field(
        None,
        description='A URL with more information about the application, for example the location of your GitHub repository for the application.',
    )
    labels: Optional[List[FieldString]] = Field(
        None,
        description='<p>Labels to improve discovery of apps in search results.</p><p>Minimum length=1. Maximum length=127. Maximum number of labels: 10</p><p>Pattern: "^[a-zA-Z0-9+\\\\-_:\\\\/@]+$";</p>',
    )
    readmeBody: Optional[str] = Field(
        None,
        description='<p>A text readme file in Markdown language that contains a more detailed description of the application and how it works.</p><p>Maximum size 5 MB</p>',
    )
    readmeUrl: Optional[str] = Field(
        None,
        description='<p>A link to the readme file in Markdown language that contains a more detailed description of the application and how it works.</p><p>Maximum size 5 MB</p>',
    )


class ApplicationsApplicationIdTemplatesPostRequest(BaseModel):
    semanticVersion: Optional[str] = Field(
        None,
        description='<p>The semantic version of the application:</p><p>\n <a href="https://semver.org/">https://semver.org/</a>\n </p>',
    )


class ApplicationsApplicationIdUnsharePostRequest(BaseModel):
    organizationId: str = Field(
        ..., description='The AWS Organization ID to unshare the application from.'
    )


class ApplicationsApplicationIdVersionsSemanticVersionPutRequest(BaseModel):
    sourceCodeArchiveUrl: Optional[str] = Field(
        None,
        description='<p>A link to the S3 object that contains the ZIP archive of the source code for this version of your application.</p><p>Maximum size 50 MB</p>',
    )
    sourceCodeUrl: Optional[str] = Field(
        None,
        description='A link to a public repository for the source code of your application, for example the URL of a specific GitHub commit.',
    )
    templateBody: Optional[str] = Field(
        None, description='The raw packaged AWS SAM template of your application.'
    )
    templateUrl: Optional[str] = Field(
        None, description='A link to the packaged AWS SAM template of your application.'
    )


class ApplicationDependencySummary(BaseModel):
    ApplicationId: FieldString
    SemanticVersion: FieldString


class CreateApplicationVersionRequest(BaseModel):
    SourceCodeArchiveUrl: Optional[FieldString] = None
    SourceCodeUrl: Optional[FieldString] = None
    TemplateBody: Optional[FieldString] = None
    TemplateUrl: Optional[FieldString] = None


class CreateCloudFormationChangeSetResponse(BaseModel):
    ApplicationId: Optional[FieldString] = None
    ChangeSetId: Optional[FieldString] = None
    SemanticVersion: Optional[FieldString] = None
    StackId: Optional[FieldString] = None


class CreateCloudFormationTemplateRequest(BaseModel):
    SemanticVersion: Optional[FieldString] = None


class CreateCloudFormationTemplateResponse(BaseModel):
    ApplicationId: Optional[FieldString] = None
    CreationTime: Optional[FieldString] = None
    ExpirationTime: Optional[FieldString] = None
    SemanticVersion: Optional[FieldString] = None
    Status_1: Optional[Status] = Field(None, alias='Status')
    TemplateId: Optional[FieldString] = None
    TemplateUrl: Optional[FieldString] = None


class GetCloudFormationTemplateResponse(BaseModel):
    ApplicationId: Optional[FieldString] = None
    CreationTime: Optional[FieldString] = None
    ExpirationTime: Optional[FieldString] = None
    SemanticVersion: Optional[FieldString] = None
    Status_1: Optional[Status] = Field(None, alias='Status')
    TemplateId: Optional[FieldString] = None
    TemplateUrl: Optional[FieldString] = None


class ParameterValue(BaseModel):
    Name: FieldString
    Value: FieldString


class RollbackTrigger(BaseModel):
    Arn: FieldString
    Type: FieldString


class Tag(BaseModel):
    Key: FieldString
    Value: FieldString


class UnshareApplicationRequest(BaseModel):
    OrganizationId: FieldString


class VersionSummary(BaseModel):
    ApplicationId: FieldString
    CreationTime: FieldString
    SemanticVersion: FieldString
    SourceCodeUrl: Optional[FieldString] = None


class FieldListOfApplicationDependencySummary(
    RootModel[List[ApplicationDependencySummary]]
):
    root: List[ApplicationDependencySummary]


class FieldListOfParameterValue(RootModel[List[ParameterValue]]):
    root: List[ParameterValue]


class FieldListOfRollbackTrigger(RootModel[List[RollbackTrigger]]):
    root: List[RollbackTrigger]


class FieldListOfTag(RootModel[List[Tag]]):
    root: List[Tag]


class FieldListOfVersionSummary(RootModel[List[VersionSummary]]):
    root: List[VersionSummary]


class FieldListOfString(RootModel[List[FieldString]]):
    root: List[FieldString]


class RollbackConfiguration(BaseModel):
    MonitoringTimeInMinutes: Optional[FieldInteger] = None
    RollbackTriggers: Optional[FieldListOfRollbackTrigger] = None


class ApplicationsApplicationIdChangesetsPostRequest(BaseModel):
    capabilities: Optional[List[FieldString]] = Field(
        None,
        description='<p>A list of values that you must specify before you can deploy certain applications.\n Some applications might include resources that can affect permissions in your AWS\n account, for example, by creating new AWS Identity and Access Management (IAM) users.\n For those applications, you must explicitly acknowledge their capabilities by\n specifying this parameter.</p><p>The only valid values are CAPABILITY_IAM, CAPABILITY_NAMED_IAM,\n CAPABILITY_RESOURCE_POLICY, and CAPABILITY_AUTO_EXPAND.</p><p>The following resources require you to specify CAPABILITY_IAM or\n CAPABILITY_NAMED_IAM:\n <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html">AWS::IAM::Group</a>,\n <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html">AWS::IAM::InstanceProfile</a>,\n <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html">AWS::IAM::Policy</a>, and\n <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html">AWS::IAM::Role</a>.\n If the application contains IAM resources, you can specify either CAPABILITY_IAM\n or CAPABILITY_NAMED_IAM. If the application contains IAM resources\n with custom names, you must specify CAPABILITY_NAMED_IAM.</p><p>The following resources require you to specify CAPABILITY_RESOURCE_POLICY:\n <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html">AWS::Lambda::Permission</a>,\n <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html">AWS::IAM:Policy</a>,\n <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html">AWS::ApplicationAutoScaling::ScalingPolicy</a>,\n <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-policy.html">AWS::S3::BucketPolicy</a>,\n <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sqs-policy.html">AWS::SQS::QueuePolicy</a>, and\n <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-policy.html">AWS::SNS:TopicPolicy</a>.</p><p>Applications that contain one or more nested applications require you to specify\n CAPABILITY_AUTO_EXPAND.</p><p>If your application template contains any of the above resources, we recommend that you review\n all permissions associated with the application before deploying. If you don\'t specify\n this parameter for an application that requires capabilities, the call will fail.</p>',
    )
    changeSetName: Optional[str] = Field(
        None,
        description='This property corresponds to the parameter of the same name for the <i>AWS CloudFormation <a href="https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet">CreateChangeSet</a>\n </i> API.',
    )
    clientToken: Optional[str] = Field(
        None,
        description='This property corresponds to the parameter of the same name for the <i>AWS CloudFormation <a href="https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet">CreateChangeSet</a>\n </i> API.',
    )
    description: Optional[str] = Field(
        None,
        description='This property corresponds to the parameter of the same name for the <i>AWS CloudFormation <a href="https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet">CreateChangeSet</a>\n </i> API.',
    )
    notificationArns: Optional[List[FieldString]] = Field(
        None,
        description='This property corresponds to the parameter of the same name for the <i>AWS CloudFormation <a href="https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet">CreateChangeSet</a>\n </i> API.',
    )
    parameterOverrides: Optional[List[ParameterValue]] = Field(
        None,
        description='A list of parameter values for the parameters of the application.',
    )
    resourceTypes: Optional[List[FieldString]] = Field(
        None,
        description='This property corresponds to the parameter of the same name for the <i>AWS CloudFormation <a href="https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet">CreateChangeSet</a>\n </i> API.',
    )
    rollbackConfiguration: Optional[RollbackConfiguration] = Field(
        None,
        description='This property corresponds to the <i>AWS CloudFormation <a href="https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/RollbackConfiguration">RollbackConfiguration</a>\n </i> Data Type.',
    )
    semanticVersion: Optional[str] = Field(
        None,
        description='<p>The semantic version of the application:</p><p>\n <a href="https://semver.org/">https://semver.org/</a>\n </p>',
    )
    stackName: str = Field(
        ...,
        description='This property corresponds to the parameter of the same name for the <i>AWS CloudFormation <a href="https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet">CreateChangeSet</a>\n </i> API.',
    )
    tags: Optional[List[Tag]] = Field(
        None,
        description='This property corresponds to the parameter of the same name for the <i>AWS CloudFormation <a href="https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet">CreateChangeSet</a>\n </i> API.',
    )
    templateId: Optional[str] = Field(
        None,
        description='<p>The UUID returned by CreateCloudFormationTemplate.</p><p>Pattern: [0-9a-fA-F]{8}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{12}</p>',
    )


class ApplicationPolicyStatement(BaseModel):
    Actions: FieldListOfString
    PrincipalOrgIDs: Optional[FieldListOfString] = None
    Principals: FieldListOfString
    StatementId: Optional[FieldString] = None


class ApplicationSummary(BaseModel):
    ApplicationId: FieldString
    Author: FieldString
    CreationTime: Optional[FieldString] = None
    Description: FieldString
    HomePageUrl: Optional[FieldString] = None
    Labels: Optional[FieldListOfString] = None
    Name: FieldString
    SpdxLicenseId: Optional[FieldString] = None


class CreateApplicationRequest(BaseModel):
    Author: FieldString
    Description: FieldString
    HomePageUrl: Optional[FieldString] = None
    Labels: Optional[FieldListOfString] = None
    LicenseBody: Optional[FieldString] = None
    LicenseUrl: Optional[FieldString] = None
    Name: FieldString
    ReadmeBody: Optional[FieldString] = None
    ReadmeUrl: Optional[FieldString] = None
    SemanticVersion: Optional[FieldString] = None
    SourceCodeArchiveUrl: Optional[FieldString] = None
    SourceCodeUrl: Optional[FieldString] = None
    SpdxLicenseId: Optional[FieldString] = None
    TemplateBody: Optional[FieldString] = None
    TemplateUrl: Optional[FieldString] = None


class ListApplicationDependenciesResponse(BaseModel):
    Dependencies: Optional[FieldListOfApplicationDependencySummary] = None
    NextToken: Optional[FieldString] = None


class ListApplicationVersionsResponse(BaseModel):
    NextToken: Optional[FieldString] = None
    Versions: Optional[FieldListOfVersionSummary] = None


class ParameterDefinition(BaseModel):
    AllowedPattern: Optional[FieldString] = None
    AllowedValues: Optional[FieldListOfString] = None
    ConstraintDescription: Optional[FieldString] = None
    DefaultValue: Optional[FieldString] = None
    Description: Optional[FieldString] = None
    MaxLength: Optional[FieldInteger] = None
    MaxValue: Optional[FieldInteger] = None
    MinLength: Optional[FieldInteger] = None
    MinValue: Optional[FieldInteger] = None
    Name: FieldString
    NoEcho: Optional[FieldBoolean] = None
    ReferencedByResources: FieldListOfString
    Type: Optional[FieldString] = None


class UpdateApplicationRequest(BaseModel):
    Author: Optional[FieldString] = None
    Description: Optional[FieldString] = None
    HomePageUrl: Optional[FieldString] = None
    Labels: Optional[FieldListOfString] = None
    ReadmeBody: Optional[FieldString] = None
    ReadmeUrl: Optional[FieldString] = None


class FieldListOfApplicationPolicyStatement(
    RootModel[List[ApplicationPolicyStatement]]
):
    root: List[ApplicationPolicyStatement]


class FieldListOfApplicationSummary(RootModel[List[ApplicationSummary]]):
    root: List[ApplicationSummary]


class FieldListOfParameterDefinition(RootModel[List[ParameterDefinition]]):
    root: List[ParameterDefinition]


class ApplicationsApplicationIdPolicyPutRequest(BaseModel):
    statements: List[ApplicationPolicyStatement] = Field(
        ..., description='An array of policy statements applied to the application.'
    )


class CreateApplicationVersionResponse(BaseModel):
    ApplicationId: Optional[FieldString] = None
    CreationTime: Optional[FieldString] = None
    ParameterDefinitions: Optional[FieldListOfParameterDefinition] = None
    RequiredCapabilities: Optional[FieldListOfCapability] = None
    ResourcesSupported: Optional[FieldBoolean] = None
    SemanticVersion: Optional[FieldString] = None
    SourceCodeArchiveUrl: Optional[FieldString] = None
    SourceCodeUrl: Optional[FieldString] = None
    TemplateUrl: Optional[FieldString] = None


class CreateCloudFormationChangeSetRequest(BaseModel):
    Capabilities: Optional[FieldListOfString] = None
    ChangeSetName: Optional[FieldString] = None
    ClientToken: Optional[FieldString] = None
    Description: Optional[FieldString] = None
    NotificationArns: Optional[FieldListOfString] = None
    ParameterOverrides: Optional[FieldListOfParameterValue] = None
    ResourceTypes: Optional[FieldListOfString] = None
    RollbackConfiguration_1: Optional[RollbackConfiguration] = Field(
        None, alias='RollbackConfiguration'
    )
    SemanticVersion: Optional[FieldString] = None
    StackName: FieldString
    Tags: Optional[FieldListOfTag] = None
    TemplateId: Optional[FieldString] = None


class GetApplicationPolicyResponse(BaseModel):
    Statements: Optional[FieldListOfApplicationPolicyStatement] = None


class ListApplicationsResponse(BaseModel):
    Applications: Optional[FieldListOfApplicationSummary] = None
    NextToken: Optional[FieldString] = None


class PutApplicationPolicyRequest(BaseModel):
    Statements: FieldListOfApplicationPolicyStatement


class PutApplicationPolicyResponse(BaseModel):
    Statements: Optional[FieldListOfApplicationPolicyStatement] = None


class Version(BaseModel):
    ApplicationId: FieldString
    CreationTime: FieldString
    ParameterDefinitions: FieldListOfParameterDefinition
    RequiredCapabilities: FieldListOfCapability
    ResourcesSupported: FieldBoolean
    SemanticVersion: FieldString
    SourceCodeArchiveUrl: Optional[FieldString] = None
    SourceCodeUrl: Optional[FieldString] = None
    TemplateUrl: FieldString


class CreateApplicationResponse(BaseModel):
    ApplicationId: Optional[FieldString] = None
    Author: Optional[FieldString] = None
    CreationTime: Optional[FieldString] = None
    Description: Optional[FieldString] = None
    HomePageUrl: Optional[FieldString] = None
    IsVerifiedAuthor: Optional[FieldBoolean] = None
    Labels: Optional[FieldListOfString] = None
    LicenseUrl: Optional[FieldString] = None
    Name: Optional[FieldString] = None
    ReadmeUrl: Optional[FieldString] = None
    SpdxLicenseId: Optional[FieldString] = None
    VerifiedAuthorUrl: Optional[FieldString] = None
    Version_1: Optional[Version] = Field(None, alias='Version')


class GetApplicationResponse(BaseModel):
    ApplicationId: Optional[FieldString] = None
    Author: Optional[FieldString] = None
    CreationTime: Optional[FieldString] = None
    Description: Optional[FieldString] = None
    HomePageUrl: Optional[FieldString] = None
    IsVerifiedAuthor: Optional[FieldBoolean] = None
    Labels: Optional[FieldListOfString] = None
    LicenseUrl: Optional[FieldString] = None
    Name: Optional[FieldString] = None
    ReadmeUrl: Optional[FieldString] = None
    SpdxLicenseId: Optional[FieldString] = None
    VerifiedAuthorUrl: Optional[FieldString] = None
    Version_1: Optional[Version] = Field(None, alias='Version')


class UpdateApplicationResponse(BaseModel):
    ApplicationId: Optional[FieldString] = None
    Author: Optional[FieldString] = None
    CreationTime: Optional[FieldString] = None
    Description: Optional[FieldString] = None
    HomePageUrl: Optional[FieldString] = None
    IsVerifiedAuthor: Optional[FieldBoolean] = None
    Labels: Optional[FieldListOfString] = None
    LicenseUrl: Optional[FieldString] = None
    Name: Optional[FieldString] = None
    ReadmeUrl: Optional[FieldString] = None
    SpdxLicenseId: Optional[FieldString] = None
    VerifiedAuthorUrl: Optional[FieldString] = None
    Version_1: Optional[Version] = Field(None, alias='Version')
