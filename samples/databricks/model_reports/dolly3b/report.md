
MLflow Model: _models:/dolly3b/1_
=================================

Contents
========

* [Model Overview](#model-overview)
* [MLflow Model](#mlflow-model)
	* [Details](#details)
	* [Signature](#signature)
	* [Saved input example info](#saved-input-example-info)
* [Registered Model](#registered-model)
	* [Details](#details)
	* [Tags](#tags)
	* [Permissions](#permissions)
* [Registered Model Version](#registered-model-version)
	* [Details](#details)
	* [Tags](#tags)
* [Run](#run)
	* [Info](#info)
	* [Params](#params)
	* [Metrics](#metrics)
	* [Inputs](#inputs)
	* [Tags](#tags)
* [Experiment](#experiment)
	* [Details](#details)
	* [Tags](#tags)
	* [Permissions](#permissions)

# Model Overview
  
<b><font size="+1">MLflow Model</font></b>  

|Name|Value|
| :--- | :--- |
|model_uri|models:/dolly3b/1|
|flavor|mlflow.transformers|
|flavor_version|4.28.1|
|mlflow_version|2.3.1|
|size_bytes|11,239,015,445|
|databricks_runtime|13.1.x-cpu-ml-scala2.12|
|time_created|2023-06-13 06:53:44|
|report_time|2023-07-06 05:11:21|
  
<b><font size="+1">MLflow Model URIs</font></b>  

|URI type|URI|
| :--- | :--- |
|model_uri|models:/dolly3b/1|
|run_uri|runs:/abbe441c4d9f4b69a9943e4beb71ce89/dolly3b|
|reg_model_download_uri|dbfs:/databricks/mlflow-registry/d672ee3b99134b6f8bc8a59b915d2950/models/dolly3b|
|run_model_download_uri|dbfs:/databricks/mlflow-tracking/3336498746257830/abbe441c4d9f4b69a9943e4beb71ce89/artifacts/dolly3b|

# MLflow Model

## Details
  

|Name|Value|
| :--- | :--- |
|artifact_path|dolly3b|
|databricks_runtime|13.1.x-cpu-ml-scala2.12|
|mlflow_version|2.3.1|
|model_uuid|c47df0c7b78341f8b631374c6ef49946|
|run_id|abbe441c4d9f4b69a9943e4beb71ce89|
|utc_time_created|2023-06-13 06:53:44.178099|

### Flavors

#### Flavor 'python_function'
  

|Name|Value|
| :--- | :--- |
|env|{'conda': 'conda.yaml', 'virtualenv': 'python_env.yaml'}|
|loader_module|mlflow.transformers|
|pipeline|pipeline|
|python_version|3.10.6|

#### Flavor 'transformers'
  

|Name|Value|
| :--- | :--- |
|code|None|
|components|['tokenizer']|
|instance_type|InstructionTextGenerationPipeline|
|pipeline|pipeline|
|pipeline_model_type|GPTNeoXForCausalLM|
|source_model_name|databricks/dolly-v2-3b|
|task|text-generation|
|tokenizer_type|GPTNeoXTokenizerFast|
|transformers_version|4.28.1|

## Signature

### Inputs
  

|Column|Type|
| :--- | :--- |
|None|string|

### Outputs
  

|Type name|Type value|
| :--- | :--- |
|string|None|

## Saved input example info
  

|Name|Value|
| :--- | :--- |
|artifact_path|input_example.json|
|pandas_orient|split|
|type|dataframe|

# Registered Model

## Details
  

|Name|Value|
| :--- | :--- |
|name|dolly3b|
|creation_timestamp|1686639590162|
|last_updated_timestamp|1687328546253|
|user_id|andre@mycompany.com|
|description|Registered model<br/>Databricks' dolly-v2-3b<br/>https://huggingface.co/databricks/dolly-v2-3b|
|id|ce7fcc248bfd446ea1c644985d1fb14c|
|permission_level|CAN_MANAGE|
|_creation_timestamp|2023-06-13 06:59:50|
|_last_updated_timestamp|2023-06-21 06:22:26|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com#mlflow/models/dolly3b|
|_api_link|https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/registered-models/get?name=dolly3b|

## Tags
  

|Name|Value|
| :--- | :--- |
|info|Databricks' dolly-v2-3b|

## Permissions
  
```
{
  "permission_levels": [
    {
      "permission_level": "CAN_READ",
      "description": "Can view the details of the registered model and its model versions, and use the model versions."
    },
    {
      "permission_level": "CAN_EDIT",
      "description": "Can view and edit the details of a registered model and its model versions (except stage changes), and add new model versions."
    },
    {
      "permission_level": "CAN_MANAGE_STAGING_VERSIONS",
      "description": "Can view and edit the details of a registered model and its model versions, add new model versions, and manage stage transitions between non-Production stages."
    },
    {
      "permission_level": "CAN_MANAGE_PRODUCTION_VERSIONS",
      "description": "Can view and edit the details of a registered model and its model versions, add new model versions, and manage stage transitions between any stages."
    },
    {
      "permission_level": "CAN_MANAGE",
      "description": "Can manage permissions on, view all details of, and perform all actions on the registered model and its model versions."
    }
  ],
  "permissions": {
    "object_id": "/registered-models/ce7fcc248bfd446ea1c644985d1fb14c",
    "object_type": "registered-model",
    "access_control_list": [
      {
        "user_name": "andre@mycompany.com",
        "display_name": "Andre",
        "all_permissions": [
          {
            "permission_level": "CAN_MANAGE",
            "inherited": false
          }
        ]
      },
      {
        "group_name": "admins",
        "all_permissions": [
          {
            "permission_level": "CAN_MANAGE",
            "inherited": true,
            "inherited_from_object": [
              "/registered-models/"
            ]
          }
        ]
      },
      {
        "group_name": "users",
        "all_permissions": [
          {
            "permission_level": "CAN_MANAGE",
            "inherited": true,
            "inherited_from_object": [
              "/registered-models/"
            ]
          }
        ]
      },
      {
        "service_principal_name": "038455d4-e5ec-4544-b6cf-64d55b91fee1",
        "display_name": "service-principal-e2-demo-west-ws-do-not-delete",
        "all_permissions": [
          {
            "permission_level": "CAN_MANAGE",
            "inherited": true,
            "inherited_from_object": [
              "/registered-models/"
            ]
          }
        ]
      }
    ]
  }
}

```
# Registered Model Version

## Details
  

|Name|Value|
| :--- | :--- |
|name|dolly3b|
|version|1|
|creation_timestamp|1686639590462|
|last_updated_timestamp|1687328578841|
|user_id|andre@mycompany.com|
|current_stage|Production|
|description|Production model version of dolly-v2-3b|
|source|dbfs:/databricks/mlflow-tracking/3336498746257830/abbe441c4d9f4b69a9943e4beb71ce89/artifacts/dolly3b|
|run_id|abbe441c4d9f4b69a9943e4beb71ce89|
|status|READY|
|_creation_timestamp|2023-06-13 06:59:50|
|_last_updated_timestamp|2023-06-21 06:22:59|
|_reg_model_download_uri|dbfs:/databricks/mlflow-registry/d672ee3b99134b6f8bc8a59b915d2950/models/dolly3b|
|_run_model_download_uri|dbfs:/databricks/mlflow-tracking/3336498746257830/abbe441c4d9f4b69a9943e4beb71ce89/artifacts/dolly3b|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com#mlflow/models/dolly3b/versions/1|
|_api_link|https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/model-versions/get?name=dolly3b&version=1|

## Tags
  
**_<font color="red" size="+1">None found</font>_**
# Run

## Info
  

|Name|Value|
| :--- | :--- |
|run_id|abbe441c4d9f4b69a9943e4beb71ce89|
|run_uuid|abbe441c4d9f4b69a9943e4beb71ce89|
|experiment_id|3336498746257830|
|run_name|capable-trout-571|
|status|FINISHED|
|start_time|1686639222719|
|end_time|1686639377116|
|artifact_uri|dbfs:/databricks/mlflow-tracking/3336498746257830/abbe441c4d9f4b69a9943e4beb71ce89/artifacts|
|lifecycle_stage|active|
|_start_time|2023-06-13 06:53:43|
|_end_time|2023-06-13 06:56:17|
|_duration|154.397|
|_experiment_name|/Users/andre@mycompany.com/mlflow/LLM/Dolly3b|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com#mlflow/experiments/3336498746257830/runs/abbe441c4d9f4b69a9943e4beb71ce89|
|_api_link|https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/runs/get?run_id=abbe441c4d9f4b69a9943e4beb71ce89|

## Params
  
**_<font color="red" size="+1">None found</font>_**
## Metrics
  
**_<font color="red" size="+1">None found</font>_**
## Inputs

## Tags

### Notebook Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.databricks.notebook.commandID|1775581375891600188_5296467027241741679_75720ce3640c47569c358233713ddf46|
|mlflow.databricks.notebookID|3336498746257830|
|mlflow.databricks.notebookPath|/Users/andre@mycompany.com/mlflow/transformers/scratch_dolly|
|mlflow.databricks.notebookRevisionID|1686639377589|

### Cluster Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.databricks.cluster.id|0730-173239-dawn193|
|mlflow.databricks.cluster.info|{'cluster_name': 'Shared Autoscaling EMEA', 'spark_version': '13.1.x-cpu-ml-scala2.12', 'node_type_id': 'i3.4xlarge', 'driver_node_type_id': 'm5.4xlarge', 'autotermination_minutes': 120, 'disk_spec': {'disk_type': {'ebs_volume_type': 'GENERAL_PURPOSE_SSD'}, 'disk_count': 1, 'disk_size': 100}, 'autoscale': {'min_workers': 0, 'max_workers': 6, 'target_workers': 0}}|
|mlflow.databricks.cluster.libraries|{'installable': [], 'redacted': []}|

### Workspace Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.databricks.webappURL|https://oregon.cloud.databricks.com|
|mlflow.databricks.workspaceID|2556758628403379|
|mlflow.databricks.workspaceURL|e2-demo-west.cloud.databricks.com|

### Source Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.source.name|/Users/andre@mycompany.com/mlflow/transformers/scratch_dolly|
|mlflow.source.type|NOTEBOOK|

### Other System Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.log-model.history|[{'artifact_path': 'dolly3b', 'saved_input_example_info': {'artifact_path': 'input_example.json', 'type': 'dataframe', 'pandas_orient': 'split'}, 'signature': {'inputs': [{'type': 'string'}], 'outputs': [{'type': 'string'}]}, 'flavors': {'python_function': {'pipeline': 'pipeline', 'loader_module': 'mlflow.transformers', 'python_version': '3.10.6', 'env': {'conda': 'conda.yaml', 'virtualenv': 'python_env.yaml'}}, 'transformers': {'task': 'text-generation', 'source_model_name': 'databricks/dolly-v2-3b', 'components': ['tokenizer'], 'pipeline': 'pipeline', 'code': None, 'tokenizer_type': 'GPTNeoXTokenizerFast', 'pipeline_model_type': 'GPTNeoXForCausalLM', 'instance_type': 'InstructionTextGenerationPipeline', 'transformers_version': '4.28.1'}}, 'run_id': 'abbe441c4d9f4b69a9943e4beb71ce89', 'model_uuid': 'c47df0c7b78341f8b631374c6ef49946', 'utc_time_created': '2023-06-13 06:53:44.178099', 'mlflow_version': '2.3.1', 'databricks_runtime': '13.1.x-cpu-ml-scala2.12'}]|
|mlflow.note.content|Databricks' dolly-v2-3b, an instruction-following large language model trained on the Databricks machine learning platform that is licensed for commercial use|
|mlflow.runName|capable-trout-571|
|mlflow.user|andre@mycompany.com|

### User Tags
  

|Key|Value|
| :--- | :--- |
|info|dolly-v2-3b run|

### Exploded Tags

#### Spark Datasources
  
**_<font color="red" size="+1">None found</font>_**
#### Cluster Info
  

|Key|Value|
| :--- | :--- |
|cluster_id|0730-173239-dawn193|
|cluster_name|Shared Autoscaling EMEA|
|spark_version|13.1.x-cpu-ml-scala2.12|
|node_type_id|i3.4xlarge|
|driver_node_type_id|m5.4xlarge|
|autotermination_minutes|120|
|disk_spec|{'disk_type': {'ebs_volume_type': 'GENERAL_PURPOSE_SSD'}, 'disk_count': 1, 'disk_size': 100}|
|autoscale|{'min_workers': 0, 'max_workers': 6, 'target_workers': 0}|

#### Cluster Libraries

# Experiment

## Details
  

|Name|Value|
| :--- | :--- |
|experiment_id|3336498746257830|
|name|/Users/andre@mycompany.com/mlflow/LLM/Dolly3b|
|artifact_location|dbfs:/databricks/mlflow-tracking/3336498746257830|
|lifecycle_stage|active|
|last_update_time|1686639223103|
|creation_time|1686639223103|
|_creation_time|2023-06-13 06:53:43|
|_last_update_time|2023-06-13 06:53:43|
|_tracking_uri|databricks://e2_demo|
|_web_ui_link|https://e2-demo-west.cloud.databricks.com#mlflow/experiments/3336498746257830|
|_api_link|https://e2-demo-west.cloud.databricks.com/api/2.0/mlflow/experiments/get?experiment_id=3336498746257830|

## Tags

### MLflow System Tags
  

|Key|Value|
| :--- | :--- |
|mlflow.note.content|Experiment for Databricks' dolly-v2-3b, an instruction-following large language model trained on the Databricks machine learning platform that is licensed for commercial use|
|mlflow.ownerId|4566812440727830|
|mlflow.experiment.sourceName|/Users/andre@mycompany.com/mlflow/LLM/Dolly3b|
|mlflow.ownerEmail|andre@mycompany.com|
|mlflow.experimentType|NOTEBOOK|

### User Tags
  
**_<font color="red" size="+1">None found</font>_**
## Permissions
  
```
{
  "permission_levels": [
    {
      "permission_level": "CAN_READ",
      "description": "Can view the experiment"
    },
    {
      "permission_level": "CAN_EDIT",
      "description": "Can view, log runs, and edit the experiment"
    },
    {
      "permission_level": "CAN_MANAGE",
      "description": "Can view, log runs, edit, delete, and change permissions of the experiment"
    }
  ],
  "permissions": {
    "error": "HTTP status code: 400. Reason: Bad Request URL: https://e2-demo-west.cloud.databricks.com/api/2.0/permissions/experiments/3336498746257830. Params: None. Text: {\"error_code\":\"INVALID_PARAMETER_VALUE\",\"message\":\"Object 3336498746257830 not a experiment.\"}"
  }
}

```