# coding: utf-8

"""
    OpsGenie REST API

    OpsGenie API Description

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from pprint import pformat

from six import iteritems


class BaseAlert(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    def __init__(self, id=None, tiny_id=None, alias=None, message=None, status=None, acknowledged=None, is_seen=None,
                 tags=None, snoozed=None, snoozed_until=None, count=None, last_occurred_at=None, created_at=None,
                 updated_at=None, source=None, owner=None, priority=None, teams=None, integration=None, report=None):
        """
        BaseAlert - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'tiny_id': 'str',
            'alias': 'str',
            'message': 'str',
            'status': 'str',
            'acknowledged': 'bool',
            'is_seen': 'bool',
            'tags': 'list[str]',
            'snoozed': 'bool',
            'snoozed_until': 'datetime',
            'count': 'int',
            'last_occurred_at': 'datetime',
            'created_at': 'datetime',
            'updated_at': 'datetime',
            'source': 'str',
            'owner': 'str',
            'priority': 'str',
            'teams': 'list[TeamMeta]',
            'integration': 'AlertIntegration',
            'report': 'AlertReport'
        }

        self.attribute_map = {
            'id': 'id',
            'tiny_id': 'tinyId',
            'alias': 'alias',
            'message': 'message',
            'status': 'status',
            'acknowledged': 'acknowledged',
            'is_seen': 'isSeen',
            'tags': 'tags',
            'snoozed': 'snoozed',
            'snoozed_until': 'snoozedUntil',
            'count': 'count',
            'last_occurred_at': 'lastOccurredAt',
            'created_at': 'createdAt',
            'updated_at': 'updatedAt',
            'source': 'source',
            'owner': 'owner',
            'priority': 'priority',
            'teams': 'teams',
            'integration': 'integration',
            'report': 'report'
        }

        self._id = id
        self._tiny_id = tiny_id
        self._alias = alias
        self._message = message
        self._status = status
        self._acknowledged = acknowledged
        self._is_seen = is_seen
        self._tags = tags
        self._snoozed = snoozed
        self._snoozed_until = snoozed_until
        self._count = count
        self._last_occurred_at = last_occurred_at
        self._created_at = created_at
        self._updated_at = updated_at
        self._source = source
        self._owner = owner
        self._priority = priority
        self._teams = teams
        self._integration = integration
        self._report = report

    @property
    def id(self):
        """
        Gets the id of this BaseAlert.

        :return: The id of this BaseAlert.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BaseAlert.

        :param id: The id of this BaseAlert.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def tiny_id(self):
        """
        Gets the tiny_id of this BaseAlert.

        :return: The tiny_id of this BaseAlert.
        :rtype: str
        """
        return self._tiny_id

    @tiny_id.setter
    def tiny_id(self, tiny_id):
        """
        Sets the tiny_id of this BaseAlert.

        :param tiny_id: The tiny_id of this BaseAlert.
        :type: str
        """

        self._tiny_id = tiny_id

    @property
    def alias(self):
        """
        Gets the alias of this BaseAlert.

        :return: The alias of this BaseAlert.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """
        Sets the alias of this BaseAlert.

        :param alias: The alias of this BaseAlert.
        :type: str
        """

        self._alias = alias

    @property
    def message(self):
        """
        Gets the message of this BaseAlert.

        :return: The message of this BaseAlert.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this BaseAlert.

        :param message: The message of this BaseAlert.
        :type: str
        """

        self._message = message

    @property
    def status(self):
        """
        Gets the status of this BaseAlert.

        :return: The status of this BaseAlert.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this BaseAlert.

        :param status: The status of this BaseAlert.
        :type: str
        """

        self._status = status

    @property
    def acknowledged(self):
        """
        Gets the acknowledged of this BaseAlert.

        :return: The acknowledged of this BaseAlert.
        :rtype: bool
        """
        return self._acknowledged

    @acknowledged.setter
    def acknowledged(self, acknowledged):
        """
        Sets the acknowledged of this BaseAlert.

        :param acknowledged: The acknowledged of this BaseAlert.
        :type: bool
        """

        self._acknowledged = acknowledged

    @property
    def is_seen(self):
        """
        Gets the is_seen of this BaseAlert.

        :return: The is_seen of this BaseAlert.
        :rtype: bool
        """
        return self._is_seen

    @is_seen.setter
    def is_seen(self, is_seen):
        """
        Sets the is_seen of this BaseAlert.

        :param is_seen: The is_seen of this BaseAlert.
        :type: bool
        """

        self._is_seen = is_seen

    @property
    def tags(self):
        """
        Gets the tags of this BaseAlert.

        :return: The tags of this BaseAlert.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this BaseAlert.

        :param tags: The tags of this BaseAlert.
        :type: list[str]
        """

        self._tags = tags

    @property
    def snoozed(self):
        """
        Gets the snoozed of this BaseAlert.

        :return: The snoozed of this BaseAlert.
        :rtype: bool
        """
        return self._snoozed

    @snoozed.setter
    def snoozed(self, snoozed):
        """
        Sets the snoozed of this BaseAlert.

        :param snoozed: The snoozed of this BaseAlert.
        :type: bool
        """

        self._snoozed = snoozed

    @property
    def snoozed_until(self):
        """
        Gets the snoozed_until of this BaseAlert.

        :return: The snoozed_until of this BaseAlert.
        :rtype: datetime
        """
        return self._snoozed_until

    @snoozed_until.setter
    def snoozed_until(self, snoozed_until):
        """
        Sets the snoozed_until of this BaseAlert.

        :param snoozed_until: The snoozed_until of this BaseAlert.
        :type: datetime
        """

        self._snoozed_until = snoozed_until

    @property
    def count(self):
        """
        Gets the count of this BaseAlert.

        :return: The count of this BaseAlert.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this BaseAlert.

        :param count: The count of this BaseAlert.
        :type: int
        """

        self._count = count

    @property
    def last_occurred_at(self):
        """
        Gets the last_occurred_at of this BaseAlert.

        :return: The last_occurred_at of this BaseAlert.
        :rtype: datetime
        """
        return self._last_occurred_at

    @last_occurred_at.setter
    def last_occurred_at(self, last_occurred_at):
        """
        Sets the last_occurred_at of this BaseAlert.

        :param last_occurred_at: The last_occurred_at of this BaseAlert.
        :type: datetime
        """

        self._last_occurred_at = last_occurred_at

    @property
    def created_at(self):
        """
        Gets the created_at of this BaseAlert.

        :return: The created_at of this BaseAlert.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this BaseAlert.

        :param created_at: The created_at of this BaseAlert.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """
        Gets the updated_at of this BaseAlert.

        :return: The updated_at of this BaseAlert.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this BaseAlert.

        :param updated_at: The updated_at of this BaseAlert.
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def source(self):
        """
        Gets the source of this BaseAlert.

        :return: The source of this BaseAlert.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this BaseAlert.

        :param source: The source of this BaseAlert.
        :type: str
        """

        self._source = source

    @property
    def owner(self):
        """
        Gets the owner of this BaseAlert.

        :return: The owner of this BaseAlert.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this BaseAlert.

        :param owner: The owner of this BaseAlert.
        :type: str
        """

        self._owner = owner

    @property
    def priority(self):
        """
        Gets the priority of this BaseAlert.

        :return: The priority of this BaseAlert.
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """
        Sets the priority of this BaseAlert.

        :param priority: The priority of this BaseAlert.
        :type: str
        """

        self._priority = priority

    @property
    def teams(self):
        """
        Gets the teams of this BaseAlert.

        :return: The teams of this BaseAlert.
        :rtype: list[TeamMeta]
        """
        return self._teams

    @teams.setter
    def teams(self, teams):
        """
        Sets the teams of this BaseAlert.

        :param teams: The teams of this BaseAlert.
        :type: list[TeamMeta]
        """

        self._teams = teams

    @property
    def integration(self):
        """
        Gets the integration of this BaseAlert.

        :return: The integration of this BaseAlert.
        :rtype: AlertIntegration
        """
        return self._integration

    @integration.setter
    def integration(self, integration):
        """
        Sets the integration of this BaseAlert.

        :param integration: The integration of this BaseAlert.
        :type: AlertIntegration
        """

        self._integration = integration

    @property
    def report(self):
        """
        Gets the report of this BaseAlert.

        :return: The report of this BaseAlert.
        :rtype: AlertReport
        """
        return self._report

    @report.setter
    def report(self, report):
        """
        Sets the report of this BaseAlert.

        :param report: The report of this BaseAlert.
        :type: AlertReport
        """

        self._report = report

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, BaseAlert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
