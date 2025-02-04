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


class V2beta1RunPolicy(object):
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
        'active_deadline_seconds': 'int',
        'backoff_limit': 'int',
        'clean_pod_policy': 'str',
        'managed_by': 'str',
        'scheduling_policy': 'V2beta1SchedulingPolicy',
        'suspend': 'bool',
        'ttl_seconds_after_finished': 'int'
    }

    attribute_map = {
        'active_deadline_seconds': 'activeDeadlineSeconds',
        'backoff_limit': 'backoffLimit',
        'clean_pod_policy': 'cleanPodPolicy',
        'managed_by': 'managedBy',
        'scheduling_policy': 'schedulingPolicy',
        'suspend': 'suspend',
        'ttl_seconds_after_finished': 'ttlSecondsAfterFinished'
    }

    def __init__(self, active_deadline_seconds=None, backoff_limit=None, clean_pod_policy=None, managed_by=None, scheduling_policy=None, suspend=None, ttl_seconds_after_finished=None, local_vars_configuration=None):  # noqa: E501
        """V2beta1RunPolicy - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._active_deadline_seconds = None
        self._backoff_limit = None
        self._clean_pod_policy = None
        self._managed_by = None
        self._scheduling_policy = None
        self._suspend = None
        self._ttl_seconds_after_finished = None
        self.discriminator = None

        if active_deadline_seconds is not None:
            self.active_deadline_seconds = active_deadline_seconds
        if backoff_limit is not None:
            self.backoff_limit = backoff_limit
        if clean_pod_policy is not None:
            self.clean_pod_policy = clean_pod_policy
        if managed_by is not None:
            self.managed_by = managed_by
        if scheduling_policy is not None:
            self.scheduling_policy = scheduling_policy
        if suspend is not None:
            self.suspend = suspend
        if ttl_seconds_after_finished is not None:
            self.ttl_seconds_after_finished = ttl_seconds_after_finished

    @property
    def active_deadline_seconds(self):
        """Gets the active_deadline_seconds of this V2beta1RunPolicy.  # noqa: E501

        Specifies the duration in seconds relative to the startTime that the job may be active before the system tries to terminate it; value must be positive integer.  # noqa: E501

        :return: The active_deadline_seconds of this V2beta1RunPolicy.  # noqa: E501
        :rtype: int
        """
        return self._active_deadline_seconds

    @active_deadline_seconds.setter
    def active_deadline_seconds(self, active_deadline_seconds):
        """Sets the active_deadline_seconds of this V2beta1RunPolicy.

        Specifies the duration in seconds relative to the startTime that the job may be active before the system tries to terminate it; value must be positive integer.  # noqa: E501

        :param active_deadline_seconds: The active_deadline_seconds of this V2beta1RunPolicy.  # noqa: E501
        :type active_deadline_seconds: int
        """

        self._active_deadline_seconds = active_deadline_seconds

    @property
    def backoff_limit(self):
        """Gets the backoff_limit of this V2beta1RunPolicy.  # noqa: E501

        Optional number of retries before marking this job failed.  # noqa: E501

        :return: The backoff_limit of this V2beta1RunPolicy.  # noqa: E501
        :rtype: int
        """
        return self._backoff_limit

    @backoff_limit.setter
    def backoff_limit(self, backoff_limit):
        """Sets the backoff_limit of this V2beta1RunPolicy.

        Optional number of retries before marking this job failed.  # noqa: E501

        :param backoff_limit: The backoff_limit of this V2beta1RunPolicy.  # noqa: E501
        :type backoff_limit: int
        """

        self._backoff_limit = backoff_limit

    @property
    def clean_pod_policy(self):
        """Gets the clean_pod_policy of this V2beta1RunPolicy.  # noqa: E501

        CleanPodPolicy defines the policy to kill pods after the job completes. Default to Running.  # noqa: E501

        :return: The clean_pod_policy of this V2beta1RunPolicy.  # noqa: E501
        :rtype: str
        """
        return self._clean_pod_policy

    @clean_pod_policy.setter
    def clean_pod_policy(self, clean_pod_policy):
        """Sets the clean_pod_policy of this V2beta1RunPolicy.

        CleanPodPolicy defines the policy to kill pods after the job completes. Default to Running.  # noqa: E501

        :param clean_pod_policy: The clean_pod_policy of this V2beta1RunPolicy.  # noqa: E501
        :type clean_pod_policy: str
        """

        self._clean_pod_policy = clean_pod_policy

    @property
    def managed_by(self):
        """Gets the managed_by of this V2beta1RunPolicy.  # noqa: E501

        ManagedBy is used to indicate the controller or entity that manages a MPIJob. The value must be either empty, 'kubeflow.org/mpi-operator' or 'kueue.x-k8s.io/multikueue'. The mpi-operator reconciles a MPIJob which doesn't have this field at all or the field value is the reserved string 'kubeflow.org/mpi-operator', but delegates reconciling the MPIJob with 'kueue.x-k8s.io/multikueue' to the Kueue. The field is immutable.  # noqa: E501

        :return: The managed_by of this V2beta1RunPolicy.  # noqa: E501
        :rtype: str
        """
        return self._managed_by

    @managed_by.setter
    def managed_by(self, managed_by):
        """Sets the managed_by of this V2beta1RunPolicy.

        ManagedBy is used to indicate the controller or entity that manages a MPIJob. The value must be either empty, 'kubeflow.org/mpi-operator' or 'kueue.x-k8s.io/multikueue'. The mpi-operator reconciles a MPIJob which doesn't have this field at all or the field value is the reserved string 'kubeflow.org/mpi-operator', but delegates reconciling the MPIJob with 'kueue.x-k8s.io/multikueue' to the Kueue. The field is immutable.  # noqa: E501

        :param managed_by: The managed_by of this V2beta1RunPolicy.  # noqa: E501
        :type managed_by: str
        """

        self._managed_by = managed_by

    @property
    def scheduling_policy(self):
        """Gets the scheduling_policy of this V2beta1RunPolicy.  # noqa: E501


        :return: The scheduling_policy of this V2beta1RunPolicy.  # noqa: E501
        :rtype: V2beta1SchedulingPolicy
        """
        return self._scheduling_policy

    @scheduling_policy.setter
    def scheduling_policy(self, scheduling_policy):
        """Sets the scheduling_policy of this V2beta1RunPolicy.


        :param scheduling_policy: The scheduling_policy of this V2beta1RunPolicy.  # noqa: E501
        :type scheduling_policy: V2beta1SchedulingPolicy
        """

        self._scheduling_policy = scheduling_policy

    @property
    def suspend(self):
        """Gets the suspend of this V2beta1RunPolicy.  # noqa: E501

        suspend specifies whether the MPIJob controller should create Pods or not. If a MPIJob is created with suspend set to true, no Pods are created by the MPIJob controller. If a MPIJob is suspended after creation (i.e. the flag goes from false to true), the MPIJob controller will delete all active Pods and PodGroups associated with this MPIJob. Also, it will suspend the Launcher Job. Users must design their workload to gracefully handle this. Suspending a Job will reset the StartTime field of the MPIJob.  Defaults to false.  # noqa: E501

        :return: The suspend of this V2beta1RunPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._suspend

    @suspend.setter
    def suspend(self, suspend):
        """Sets the suspend of this V2beta1RunPolicy.

        suspend specifies whether the MPIJob controller should create Pods or not. If a MPIJob is created with suspend set to true, no Pods are created by the MPIJob controller. If a MPIJob is suspended after creation (i.e. the flag goes from false to true), the MPIJob controller will delete all active Pods and PodGroups associated with this MPIJob. Also, it will suspend the Launcher Job. Users must design their workload to gracefully handle this. Suspending a Job will reset the StartTime field of the MPIJob.  Defaults to false.  # noqa: E501

        :param suspend: The suspend of this V2beta1RunPolicy.  # noqa: E501
        :type suspend: bool
        """

        self._suspend = suspend

    @property
    def ttl_seconds_after_finished(self):
        """Gets the ttl_seconds_after_finished of this V2beta1RunPolicy.  # noqa: E501

        TTLSecondsAfterFinished is the TTL to clean up jobs. It may take extra ReconcilePeriod seconds for the cleanup, since reconcile gets called periodically. Default to infinite.  # noqa: E501

        :return: The ttl_seconds_after_finished of this V2beta1RunPolicy.  # noqa: E501
        :rtype: int
        """
        return self._ttl_seconds_after_finished

    @ttl_seconds_after_finished.setter
    def ttl_seconds_after_finished(self, ttl_seconds_after_finished):
        """Sets the ttl_seconds_after_finished of this V2beta1RunPolicy.

        TTLSecondsAfterFinished is the TTL to clean up jobs. It may take extra ReconcilePeriod seconds for the cleanup, since reconcile gets called periodically. Default to infinite.  # noqa: E501

        :param ttl_seconds_after_finished: The ttl_seconds_after_finished of this V2beta1RunPolicy.  # noqa: E501
        :type ttl_seconds_after_finished: int
        """

        self._ttl_seconds_after_finished = ttl_seconds_after_finished

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
        if not isinstance(other, V2beta1RunPolicy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V2beta1RunPolicy):
            return True

        return self.to_dict() != other.to_dict()
