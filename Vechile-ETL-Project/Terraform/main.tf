module "service_account" {
  source = "./modules/service-account"

  account_id   = var.service_account_id
  display_name = var.service_account_display_name
}

module "storage" {
  source = "./modules/storage"

  bucket_name           = var.bucket_name
  region                = var.region
  service_account_email = module.service_account.email
}

module "bigquery" {
  source = "./modules/bigquery"

  location              = var.region
  service_account_email = module.service_account.email
}
