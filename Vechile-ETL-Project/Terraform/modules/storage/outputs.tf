output "bucket_name" {
  description = "Vehicle ETL Cloud Storage bucket"
  value       = google_storage_bucket.this.name
}

output "bucket_url" {
  description = "Vehicle ETL Cloud Storage bucket URL"
  value       = google_storage_bucket.this.url
}