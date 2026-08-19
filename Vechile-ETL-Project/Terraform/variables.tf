variable "project_id" {
  description = "Google Cloud project ID"
  type        = string
}

variable "region" {
  description = "Google Cloud region"
  type        = string
  default     = "asia-south1"
}

variable "service_account_id" {
  description = "Service account ID"
  type        = string
  default     = "vehicle-etl-sa"
}

variable "service_account_display_name" {
  description = "Service account display name"
  type        = string
  default     = "Vehicle ETL Service Account"
}

variable "bucket_name" {
  description = "Globally unique Cloud Storage bucket name"
  type        = string
}

variable "dataset_id" {
  description = "BigQuery dataset ID"
  type        = string
  default     = "vehicle_analytics"
}