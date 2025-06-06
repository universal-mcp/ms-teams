from typing import Any, List, Optional
from .api_segment_base import APISegmentBase


class AppcatalogsApi(APISegmentBase):

    def __init__(self, main_app_client: Any):
        super().__init__(main_app_client)

    def app_catalogs_list_teams_apps(
        self,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        List teamsApp

        Args:
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            appCatalogs.teamsApp, important
        """
        url = f"{self.main_app_client.base_url}/appCatalogs/teamsApps"
        query_params = {
            k: v
            for k, v in [
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def app_catalogs_create_teams_apps(
        self,
        atodata_type: str,
        id: Optional[str] = None,
        displayName: Optional[str] = None,
        distributionMethod: Optional[Any] = None,
        externalId: Optional[str] = None,
        appDefinitions: Optional[List[Any]] = None,
    ) -> Any:
        """

        Publish teamsApp

        Args:
            atodata_type (string): @odata.type
            id (string): The unique identifier for an entity. Read-only.
            displayName (string): The name of the catalog app provided by the app developer in the Microsoft Teams zip app package.
            distributionMethod (string): The method of distribution for the app. Read-only.
            externalId (string): The ID of the catalog provided by the app developer in the Microsoft Teams zip app package.
            appDefinitions (array): The details for each version of the app.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            appCatalogs.teamsApp
        """
        request_body_data = None
        request_body_data = {
            "id": id,
            "@odata.type": atodata_type,
            "displayName": displayName,
            "distributionMethod": distributionMethod,
            "externalId": externalId,
            "appDefinitions": appDefinitions,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/appCatalogs/teamsApps"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def app_catalogs_get_teams_apps(
        self,
        teamsApp_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get teamsApps from appCatalogs

        Args:
            teamsApp_id (string): teamsApp-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            appCatalogs.teamsApp
        """
        if teamsApp_id is None:
            raise ValueError("Missing required parameter 'teamsApp-id'.")
        url = f"{self.main_app_client.base_url}/appCatalogs/teamsApps/{teamsApp_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def app_catalogs_update_teams_apps(
        self,
        teamsApp_id: str,
        atodata_type: str,
        id: Optional[str] = None,
        displayName: Optional[str] = None,
        distributionMethod: Optional[Any] = None,
        externalId: Optional[str] = None,
        appDefinitions: Optional[List[Any]] = None,
    ) -> Any:
        """

        Update the navigation property teamsApps in appCatalogs

        Args:
            teamsApp_id (string): teamsApp-id
            atodata_type (string): @odata.type
            id (string): The unique identifier for an entity. Read-only.
            displayName (string): The name of the catalog app provided by the app developer in the Microsoft Teams zip app package.
            distributionMethod (string): The method of distribution for the app. Read-only.
            externalId (string): The ID of the catalog provided by the app developer in the Microsoft Teams zip app package.
            appDefinitions (array): The details for each version of the app.

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            appCatalogs.teamsApp
        """
        if teamsApp_id is None:
            raise ValueError("Missing required parameter 'teamsApp-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "@odata.type": atodata_type,
            "displayName": displayName,
            "distributionMethod": distributionMethod,
            "externalId": externalId,
            "appDefinitions": appDefinitions,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/appCatalogs/teamsApps/{teamsApp_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def app_catalogs_delete_teams_apps(self, teamsApp_id: str) -> Any:
        """

        Delete teamsApp

        Args:
            teamsApp_id (string): teamsApp-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            appCatalogs.teamsApp
        """
        if teamsApp_id is None:
            raise ValueError("Missing required parameter 'teamsApp-id'.")
        url = f"{self.main_app_client.base_url}/appCatalogs/teamsApps/{teamsApp_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def get_app_definitions(
        self,
        teamsApp_id: str,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        orderby: Optional[List[str]] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> dict[str, Any]:
        """

        Get appDefinitions from appCatalogs

        Args:
            teamsApp_id (string): teamsApp-id
            top (integer): Show only the first n items Example: '50'.
            skip (integer): Skip the first n items
            search (string): Search items by search phrases
            filter (string): Filter items by property values
            count (boolean): Include count of items
            orderby (array): Order items by property values
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            dict[str, Any]: Retrieved collection

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            appCatalogs.teamsApp
        """
        if teamsApp_id is None:
            raise ValueError("Missing required parameter 'teamsApp-id'.")
        url = f"{self.main_app_client.base_url}/appCatalogs/teamsApps/{teamsApp_id}/appDefinitions"
        query_params = {
            k: v
            for k, v in [
                ("$top", top),
                ("$skip", skip),
                ("$search", search),
                ("$filter", filter),
                ("$count", count),
                ("$orderby", orderby),
                ("$select", select),
                ("$expand", expand),
            ]
            if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def create_teams_app_definition(
        self,
        teamsApp_id: str,
        atodata_type: str,
        id: Optional[str] = None,
        authorization: Optional[Any] = None,
        createdBy: Optional[Any] = None,
        description: Optional[str] = None,
        displayName: Optional[str] = None,
        lastModifiedDateTime: Optional[str] = None,
        publishingState: Optional[Any] = None,
        shortDescription: Optional[str] = None,
        teamsAppId: Optional[str] = None,
        version: Optional[str] = None,
        bot: Optional[Any] = None,
    ) -> Any:
        """

        Update teamsApp

        Args:
            teamsApp_id (string): teamsApp-id
            atodata_type (string): @odata.type
            id (string): The unique identifier for an entity. Read-only.
            authorization (string): Authorization requirements specified in the Teams app manifest.
            createdBy (string): createdBy
            description (string): Verbose description of the application.
            displayName (string): The name of the app provided by the app developer.
            lastModifiedDateTime (string): lastModifiedDateTime
            publishingState (string): The published status of a specific version of a Teams app. Possible values are:submitted—The specific version of the Teams app was submitted and is under review.published—The request to publish the specific version of the Teams app was approved by the admin and the app is published.rejected—The admin rejected the request to publish the specific version of the Teams app.
            shortDescription (string): Short description of the application.
            teamsAppId (string): The ID from the Teams app manifest.
            version (string): The version number of the application.
            bot (string): The details of the bot specified in the Teams app manifest.

        Returns:
            Any: Created navigation property.

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            appCatalogs.teamsApp
        """
        if teamsApp_id is None:
            raise ValueError("Missing required parameter 'teamsApp-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "@odata.type": atodata_type,
            "authorization": authorization,
            "createdBy": createdBy,
            "description": description,
            "displayName": displayName,
            "lastModifiedDateTime": lastModifiedDateTime,
            "publishingState": publishingState,
            "shortDescription": shortDescription,
            "teamsAppId": teamsAppId,
            "version": version,
            "bot": bot,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/appCatalogs/teamsApps/{teamsApp_id}/appDefinitions"
        query_params = {}
        response = self._post(
            url,
            data=request_body_data,
            params=query_params,
            content_type="application/json",
        )
        return self._handle_response(response)

    def get_app_definition_by_id(
        self,
        teamsApp_id: str,
        teamsAppDefinition_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get appDefinitions from appCatalogs

        Args:
            teamsApp_id (string): teamsApp-id
            teamsAppDefinition_id (string): teamsAppDefinition-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            appCatalogs.teamsApp
        """
        if teamsApp_id is None:
            raise ValueError("Missing required parameter 'teamsApp-id'.")
        if teamsAppDefinition_id is None:
            raise ValueError("Missing required parameter 'teamsAppDefinition-id'.")
        url = f"{self.main_app_client.base_url}/appCatalogs/teamsApps/{teamsApp_id}/appDefinitions/{teamsAppDefinition_id}"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def update_app_definition(
        self,
        teamsApp_id: str,
        teamsAppDefinition_id: str,
        atodata_type: str,
        id: Optional[str] = None,
        authorization: Optional[Any] = None,
        createdBy: Optional[Any] = None,
        description: Optional[str] = None,
        displayName: Optional[str] = None,
        lastModifiedDateTime: Optional[str] = None,
        publishingState: Optional[Any] = None,
        shortDescription: Optional[str] = None,
        teamsAppId: Optional[str] = None,
        version: Optional[str] = None,
        bot: Optional[Any] = None,
    ) -> Any:
        """

        Publish teamsApp

        Args:
            teamsApp_id (string): teamsApp-id
            teamsAppDefinition_id (string): teamsAppDefinition-id
            atodata_type (string): @odata.type
            id (string): The unique identifier for an entity. Read-only.
            authorization (string): Authorization requirements specified in the Teams app manifest.
            createdBy (string): createdBy
            description (string): Verbose description of the application.
            displayName (string): The name of the app provided by the app developer.
            lastModifiedDateTime (string): lastModifiedDateTime
            publishingState (string): The published status of a specific version of a Teams app. Possible values are:submitted—The specific version of the Teams app was submitted and is under review.published—The request to publish the specific version of the Teams app was approved by the admin and the app is published.rejected—The admin rejected the request to publish the specific version of the Teams app.
            shortDescription (string): Short description of the application.
            teamsAppId (string): The ID from the Teams app manifest.
            version (string): The version number of the application.
            bot (string): The details of the bot specified in the Teams app manifest.

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            appCatalogs.teamsApp
        """
        if teamsApp_id is None:
            raise ValueError("Missing required parameter 'teamsApp-id'.")
        if teamsAppDefinition_id is None:
            raise ValueError("Missing required parameter 'teamsAppDefinition-id'.")
        request_body_data = None
        request_body_data = {
            "id": id,
            "@odata.type": atodata_type,
            "authorization": authorization,
            "createdBy": createdBy,
            "description": description,
            "displayName": displayName,
            "lastModifiedDateTime": lastModifiedDateTime,
            "publishingState": publishingState,
            "shortDescription": shortDescription,
            "teamsAppId": teamsAppId,
            "version": version,
            "bot": bot,
        }
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/appCatalogs/teamsApps/{teamsApp_id}/appDefinitions/{teamsAppDefinition_id}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def delete_teams_app_definition(
        self, teamsApp_id: str, teamsAppDefinition_id: str
    ) -> Any:
        """

        Delete navigation property appDefinitions for appCatalogs

        Args:
            teamsApp_id (string): teamsApp-id
            teamsAppDefinition_id (string): teamsAppDefinition-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            appCatalogs.teamsApp
        """
        if teamsApp_id is None:
            raise ValueError("Missing required parameter 'teamsApp-id'.")
        if teamsAppDefinition_id is None:
            raise ValueError("Missing required parameter 'teamsAppDefinition-id'.")
        url = f"{self.main_app_client.base_url}/appCatalogs/teamsApps/{teamsApp_id}/appDefinitions/{teamsAppDefinition_id}"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def get_teams_app_bot(
        self,
        teamsApp_id: str,
        teamsAppDefinition_id: str,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
    ) -> Any:
        """

        Get teamworkBot

        Args:
            teamsApp_id (string): teamsApp-id
            teamsAppDefinition_id (string): teamsAppDefinition-id
            select (array): Select properties to be returned
            expand (array): Expand related entities

        Returns:
            Any: Retrieved navigation property

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            appCatalogs.teamsApp
        """
        if teamsApp_id is None:
            raise ValueError("Missing required parameter 'teamsApp-id'.")
        if teamsAppDefinition_id is None:
            raise ValueError("Missing required parameter 'teamsAppDefinition-id'.")
        url = f"{self.main_app_client.base_url}/appCatalogs/teamsApps/{teamsApp_id}/appDefinitions/{teamsAppDefinition_id}/bot"
        query_params = {
            k: v for k, v in [("$select", select), ("$expand", expand)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def update_bot_definition(
        self,
        teamsApp_id: str,
        teamsAppDefinition_id: str,
        atodata_type: str,
        id: Optional[str] = None,
    ) -> Any:
        """

        Update the navigation property bot in appCatalogs

        Args:
            teamsApp_id (string): teamsApp-id
            teamsAppDefinition_id (string): teamsAppDefinition-id
            atodata_type (string): @odata.type
            id (string): The unique identifier for an entity. Read-only.

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            appCatalogs.teamsApp
        """
        if teamsApp_id is None:
            raise ValueError("Missing required parameter 'teamsApp-id'.")
        if teamsAppDefinition_id is None:
            raise ValueError("Missing required parameter 'teamsAppDefinition-id'.")
        request_body_data = None
        request_body_data = {"id": id, "@odata.type": atodata_type}
        request_body_data = {
            k: v for k, v in request_body_data.items() if v is not None
        }
        url = f"{self.main_app_client.base_url}/appCatalogs/teamsApps/{teamsApp_id}/appDefinitions/{teamsAppDefinition_id}/bot"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        return self._handle_response(response)

    def delete_bot_definition(
        self, teamsApp_id: str, teamsAppDefinition_id: str
    ) -> Any:
        """

        Delete navigation property bot for appCatalogs

        Args:
            teamsApp_id (string): teamsApp-id
            teamsAppDefinition_id (string): teamsAppDefinition-id

        Returns:
            Any: Success

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            appCatalogs.teamsApp
        """
        if teamsApp_id is None:
            raise ValueError("Missing required parameter 'teamsApp-id'.")
        if teamsAppDefinition_id is None:
            raise ValueError("Missing required parameter 'teamsAppDefinition-id'.")
        url = f"{self.main_app_client.base_url}/appCatalogs/teamsApps/{teamsApp_id}/appDefinitions/{teamsAppDefinition_id}/bot"
        query_params = {}
        response = self._delete(url, params=query_params)
        return self._handle_response(response)

    def count_teams_app_definitions(
        self,
        teamsApp_id: str,
        search: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> Any:
        """

        Get the number of the resource

        Args:
            teamsApp_id (string): teamsApp-id
            search (string): Search items by search phrases
            filter (string): Filter items by property values

        Returns:
            Any: The count of the resource

        Raises:
            HTTPStatusError: Raised when the API request fails with detailed error information including status code and response body.

        Tags:
            appCatalogs.teamsApp
        """
        if teamsApp_id is None:
            raise ValueError("Missing required parameter 'teamsApp-id'.")
        url = f"{self.main_app_client.base_url}/appCatalogs/teamsApps/{teamsApp_id}/appDefinitions/$count"
        query_params = {
            k: v for k, v in [("$search", search), ("$filter", filter)] if v is not None
        }
        response = self._get(url, params=query_params)
        return self._handle_response(response)

    def list_tools(self):
        return [
            self.app_catalogs_list_teams_apps,
            self.app_catalogs_create_teams_apps,
            self.app_catalogs_get_teams_apps,
            self.app_catalogs_update_teams_apps,
            self.app_catalogs_delete_teams_apps,
            self.get_app_definitions,
            self.create_teams_app_definition,
            self.get_app_definition_by_id,
            self.update_app_definition,
            self.delete_teams_app_definition,
            self.get_teams_app_bot,
            self.update_bot_definition,
            self.delete_bot_definition,
            self.count_teams_app_definitions,
        ]
