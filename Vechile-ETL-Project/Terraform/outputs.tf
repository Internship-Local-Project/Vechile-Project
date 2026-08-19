output "service_account_email" {
  description = "Service account email"
  value       = module.service_account.email
}

output "storage_bucket" {
  description = "Cloud Storage bucket"
  value       = module.storage.bucket_name
}

output "storage_bucket_url" {
  description = "Cloud Storage bucket URL"
  value       = module.storage.bucket_url
}



output "bigquery_bronze_dataset" {
  description = "Bronze BigQuery dataset ID"
  value       = module.bigquery.bronze_dataset_id
}

output "bigquery_silver_dataset" {
  description = "Silver BigQuery dataset ID"
  value       = module.bigquery.silver_dataset_id
}

output "bigquery_gold_dataset" {
  description = "Gold BigQuery dataset ID"
  value       = module.bigquery.gold_dataset_id
}