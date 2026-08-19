resource "google_bigquery_dataset" "this" {
  dataset_id  = var.dataset_id
  description = "Vehicle ETL dataset"
  location    = var.location
}

resource "google_bigquery_table" "bronze" {
  dataset_id = google_bigquery_dataset.this.dataset_id
  table_id   = "bronze"
}

resource "google_bigquery_table" "silver" {
  dataset_id = google_bigquery_dataset.this.dataset_id
  table_id   = "silver"
}

resource "google_bigquery_table" "gold" {
  dataset_id = google_bigquery_dataset.this.dataset_id
  table_id   = "gold"
}

resource "google_bigquery_dataset_iam_member" "service_account" {
  dataset_id = google_bigquery_dataset.this.dataset_id
  role       = "roles/bigquery.dataEditor"
  member     = "serviceAccount:${var.service_account_email}"
}