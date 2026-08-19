output "bronze_dataset_id" {
  description = "Bronze BigQuery dataset ID"
  value       = google_bigquery_dataset.bronze.dataset_id
}

output "silver_dataset_id" {
  description = "Silver BigQuery dataset ID"
  value       = google_bigquery_dataset.silver.dataset_id
}

output "gold_dataset_id" {
  description = "Gold BigQuery dataset ID"
  value       = google_bigquery_dataset.gold.dataset_id
}