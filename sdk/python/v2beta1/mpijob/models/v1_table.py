# coding: utf-8

"""
    mpijob

    Python SDK for MPI-Operator  # noqa: E501

    The version of the OpenAPI document: v2beta1
    Generated by: https://openapi-generator.tech
"""


import inspect
import pprint
import re  # noqa: F401
import six

from mpijob.configuration import Configuration


class V1Table(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'api_version': 'str',
        'column_definitions': 'list[V1TableColumnDefinition]',
        'kind': 'str',
        'metadata': 'V1ListMeta',
        'rows': 'list[V1TableRow]'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'column_definitions': 'columnDefinitions',
        'kind': 'kind',
        'metadata': 'metadata',
        'rows': 'rows'
    }

    def __init__(self, api_version=None, column_definitions=None, kind=None, metadata=None, rows=None, local_vars_configuration=None):  # noqa: E501
        """V1Table - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._api_version = None
        self._column_definitions = None
        self._kind = None
        self._metadata = None
        self._rows = None
        self.discriminator = None

        if api_version is not None:
            self.api_version = api_version
        self.column_definitions = column_definitions
        if kind is not None:
            self.kind = kind
        if metadata is not None:
            self.metadata = metadata
        self.rows = rows

    @property
    def api_version(self):
        """Gets the api_version of this V1Table.  # noqa: E501

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :return: The api_version of this V1Table.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this V1Table.

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :param api_version: The api_version of this V1Table.  # noqa: E501
        :type api_version: str
        """

        self._api_version = api_version

    @property
    def column_definitions(self):
        """Gets the column_definitions of this V1Table.  # noqa: E501

        columnDefinitions describes each column in the returned items array. The number of cells per row will always match the number of column definitions.  # noqa: E501

        :return: The column_definitions of this V1Table.  # noqa: E501
        :rtype: list[V1TableColumnDefinition]
        """
        return self._column_definitions

    @column_definitions.setter
    def column_definitions(self, column_definitions):
        """Sets the column_definitions of this V1Table.

        columnDefinitions describes each column in the returned items array. The number of cells per row will always match the number of column definitions.  # noqa: E501

        :param column_definitions: The column_definitions of this V1Table.  # noqa: E501
        :type column_definitions: list[V1TableColumnDefinition]
        """
        if self.local_vars_configuration.client_side_validation and column_definitions is None:  # noqa: E501
            raise ValueError("Invalid value for `column_definitions`, must not be `None`")  # noqa: E501

        self._column_definitions = column_definitions

    @property
    def kind(self):
        """Gets the kind of this V1Table.  # noqa: E501

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :return: The kind of this V1Table.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this V1Table.

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :param kind: The kind of this V1Table.  # noqa: E501
        :type kind: str
        """

        self._kind = kind

    @property
    def metadata(self):
        """Gets the metadata of this V1Table.  # noqa: E501


        :return: The metadata of this V1Table.  # noqa: E501
        :rtype: V1ListMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this V1Table.


        :param metadata: The metadata of this V1Table.  # noqa: E501
        :type metadata: V1ListMeta
        """

        self._metadata = metadata

    @property
    def rows(self):
        """Gets the rows of this V1Table.  # noqa: E501

        rows is the list of items in the table.  # noqa: E501

        :return: The rows of this V1Table.  # noqa: E501
        :rtype: list[V1TableRow]
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """Sets the rows of this V1Table.

        rows is the list of items in the table.  # noqa: E501

        :param rows: The rows of this V1Table.  # noqa: E501
        :type rows: list[V1TableRow]
        """
        if self.local_vars_configuration.client_side_validation and rows is None:  # noqa: E501
            raise ValueError("Invalid value for `rows`, must not be `None`")  # noqa: E501

        self._rows = rows

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = inspect.getargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1Table):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1Table):
            return True

        return self.to_dict() != other.to_dict()
