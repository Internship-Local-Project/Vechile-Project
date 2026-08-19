resource "google_storage_bucket" "this" {
  name     = var.bucket_name
  location = var.region

  uniform_bucket_level_access = true

  versioning {
    enabled = true
  }

  labels = {
    project     = "vehicle-etl"
    environment = "development"
    data_layer  = "raw"
  }
}

resource "google_storage_bucket_iam_member" "service_account" {
  bucket = google_storage_bucket.this.name

  role = "roles/storage.objectAdmin"

  member = "serviceAccount:${var.service_account_email}"
}