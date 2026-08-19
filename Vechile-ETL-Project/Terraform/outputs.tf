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

output "bigquery_dataset" {
  description = "BigQuery dataset"
  value       = module.bigquery.dataset_id
}

output "bigquery_dataset_id" {
  description = "BigQuery dataset ID"
  value       = module.bigquery.dataset_id
}

output "bronze_table" {
  description = "Bronze BigQuery table"
  value       = module.bigquery.bronze_table
}

output "silver_table" {
  description = "Silver BigQuery table"
  value       = module.bigquery.silver_table
}

output "gold_table" {
  description = "Gold BigQuery table"
  value       = module.bigquery.gold_table
}