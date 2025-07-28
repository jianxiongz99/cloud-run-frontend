project="PROJECT_ID"  # Replace with your actual project ID
region="us-central1"
subnet="projects/$project/regions/us-central1/subnetworks/subnet-name"  # Replace with your actual subnet name
service_account="cloudrun-sa@$project.iam.gserviceaccount.com"  # Replace with your actual service account email
service_name="frontend"

gcloud run deploy $service_name \
--allow-unauthenticated \
--source . \
--region $region \
--project $project \
--max-instances 1 \
--cpu 0.1 --memory 128Mi \
--concurrency 1 \
--service-account $service_account \
--subnet $subnet
 