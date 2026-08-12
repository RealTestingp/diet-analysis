import azure.functions as func
import json
<<<<<<< HEAD

from azure.cosmos.exceptions import CosmosResourceNotFoundError

from cosmos_client import get_container
=======
import io
import os

from azure.storage.blob import BlobServiceClient

from data_analysis import analyze_diets
>>>>>>> fcbc2b33dc511076dfb360994472731e94bf15d8


def main(req: func.HttpRequest) -> func.HttpResponse:

    try:

<<<<<<< HEAD
        container = get_container()

        try:
            result = container.read_item(
                item="latest",
                partition_key="latest"
            )
        except CosmosResourceNotFoundError:
            return func.HttpResponse(
                json.dumps({
                    "error": "No analysis result cached yet. "
                             "Upload All_Diets.csv to trigger processing."
                }),
                mimetype="application/json",
                status_code=404
            )
=======
        connection_string = os.environ["AzureWebJobsStorage"]

        blob_service_client = BlobServiceClient.from_connection_string(
            connection_string
        )

        blob_client = blob_service_client.get_blob_client(
            container="datasets",
            blob="All_Diets.csv"
        )

        csv_data = blob_client.download_blob().readall()

        result = analyze_diets(
            io.BytesIO(csv_data)
        )
>>>>>>> fcbc2b33dc511076dfb360994472731e94bf15d8

        return func.HttpResponse(
            json.dumps(result),
            mimetype="application/json",
            status_code=200
        )

    except Exception as e:

        return func.HttpResponse(
            json.dumps({
                "error": str(e)
            }),
            mimetype="application/json",
            status_code=500
        )