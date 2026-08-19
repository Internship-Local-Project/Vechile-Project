variable "bucket_name" {
  description = "Cloud Storage bucket name"
  type        = string
}

variable "region" {
  description = "Cloud Storage bucket region"
  type        = string
}

variable "service_account_email" {
  description = "Vehicle ETL service account email"
  type        = string
}