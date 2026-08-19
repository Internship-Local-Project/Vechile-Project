output "dataset_id" {
  description = "BigQuery dataset ID"
  value       = google_bigquery_dataset.this.dataset_id
}

output "bronze_table" {
  description = "Bronze BigQuery table"
  value       = google_bigquery_table.bronze.table_id
}

output "silver_table" {
  description = "Silver BigQuery table"
  value       = google_bigquery_table.silver.table_id
}

output "gold_table" {
  description = "Gold BigQuery table"
  value       = google_bigquery_table.gold.table_id
}