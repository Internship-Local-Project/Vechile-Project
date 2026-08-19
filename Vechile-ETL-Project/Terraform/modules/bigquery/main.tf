# =========================
# DATASETS
# =========================

resource "google_bigquery_dataset" "bronze" {
  dataset_id = "bronze"
  location   = var.location
}

resource "google_bigquery_dataset" "silver" {
  dataset_id = "silver"
  location   = var.location
}

resource "google_bigquery_dataset" "gold" {
  dataset_id = "gold"
  location   = var.location
}


# =========================
# BRONZE TABLES
# =========================

resource "google_bigquery_table" "bronze_manufacturers" {
  dataset_id = google_bigquery_dataset.bronze.dataset_id
  table_id   = "bronze_manufacturers"
  deletion_protection = false
}

resource "google_bigquery_table" "bronze_dealers" {
  dataset_id = google_bigquery_dataset.bronze.dataset_id
  table_id   = "bronze_dealers"
  deletion_protection = false
}

resource "google_bigquery_table" "bronze_customers" {
  dataset_id = google_bigquery_dataset.bronze.dataset_id
  table_id   = "bronze_customers"
  deletion_protection = false
}

resource "google_bigquery_table" "bronze_vehicles" {
  dataset_id = google_bigquery_dataset.bronze.dataset_id
  table_id   = "bronze_vehicles"
  deletion_protection = false
}

resource "google_bigquery_table" "bronze_payments" {
  dataset_id = google_bigquery_dataset.bronze.dataset_id
  table_id   = "bronze_payments"
  deletion_protection = false
}


# =========================
# SILVER TABLES
# =========================

resource "google_bigquery_table" "silver_manufacturers" {
  dataset_id = google_bigquery_dataset.silver.dataset_id
  table_id   = "silver_manufacturers"
  deletion_protection = false
}

resource "google_bigquery_table" "silver_dealers" {
  dataset_id = google_bigquery_dataset.silver.dataset_id
  table_id   = "silver_dealers"
  deletion_protection = false
}

resource "google_bigquery_table" "silver_customers" {
  dataset_id = google_bigquery_dataset.silver.dataset_id
  table_id   = "silver_customers"
  deletion_protection = false
}

resource "google_bigquery_table" "silver_vehicles" {
  dataset_id = google_bigquery_dataset.silver.dataset_id
  table_id   = "silver_vehicles"
  deletion_protection = false
}

resource "google_bigquery_table" "silver_payments" {
  dataset_id = google_bigquery_dataset.silver.dataset_id
  table_id   = "silver_payments"
  deletion_protection = false
}


# =========================
# GOLD TABLES
# =========================

resource "google_bigquery_table" "gold_manufacturers" {
  dataset_id = google_bigquery_dataset.gold.dataset_id
  table_id   = "gold_manufacturers"
  deletion_protection = false
}

resource "google_bigquery_table" "gold_dealers" {
  dataset_id = google_bigquery_dataset.gold.dataset_id
  table_id   = "gold_dealers"
  deletion_protection = false
}

resource "google_bigquery_table" "gold_customers" {
  dataset_id = google_bigquery_dataset.gold.dataset_id
  table_id   = "gold_customers"
  deletion_protection = false
}

resource "google_bigquery_table" "gold_vehicles" {
  dataset_id = google_bigquery_dataset.gold.dataset_id
  table_id   = "gold_vehicles"
  deletion_protection = false
}

resource "google_bigquery_table" "gold_payments" {
  dataset_id = google_bigquery_dataset.gold.dataset_id
  table_id   = "gold_payments"
  deletion_protection = false
}


# =========================
# DATASET IAM
# =========================

resource "google_bigquery_dataset_iam_member" "bronze_service_account" {
  dataset_id = google_bigquery_dataset.bronze.dataset_id
  role       = "roles/bigquery.dataEditor"
  member     = "serviceAccount:${var.service_account_email}"
}

resource "google_bigquery_dataset_iam_member" "silver_service_account" {
  dataset_id = google_bigquery_dataset.silver.dataset_id
  role       = "roles/bigquery.dataEditor"
  member     = "serviceAccount:${var.service_account_email}"
}

resource "google_bigquery_dataset_iam_member" "gold_service_account" {
  dataset_id = google_bigquery_dataset.gold.dataset_id
  role       = "roles/bigquery.dataEditor"
  member     = "serviceAccount:${var.service_account_email}"
}