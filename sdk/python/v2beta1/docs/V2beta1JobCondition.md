# V2beta1JobCondition

JobCondition describes the state of the job at a certain point.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_transition_time** | **datetime** | Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers. | [optional] 
**last_update_time** | **datetime** | Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers. | [optional] 
**message** | **str** | A human-readable message indicating details about the transition. | [optional] 
**reason** | **str** | The reason for the condition&#39;s last transition. | [optional] 
**status** | **str** | status of the condition, one of True, False, Unknown. | [default to '']
**type** | **str** | type of job condition. | [default to '']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


