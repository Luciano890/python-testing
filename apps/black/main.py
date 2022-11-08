def get_workflows_names(self) -> list[str]:
    """..."""
    return [
        workflow["name"]
        for workflow in self.__WORKFLOW_SERVICE.get_all_workflows(
            self._database_name, self._form_uuid
        )
        if workflow["status"] != StatusWorkflowTask.INACTIVE.value
        and workflow["form_uuid"] == self._form_uuid
    ]
