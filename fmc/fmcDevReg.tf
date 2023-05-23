#Jeff Comer


#data "fmc_access_policies" "access_policy" {
#    name = "FTD"
#}

resource "fmc_access_policies" "access_policy" {
    name = "dcloud-accessPolicy"
    default_action = "permit"
}

resource "fmc_devices" "dcloud_ftd" {
    name = var.fmc_ftd1_name
    hostname = var.fmc_ftd1
    regkey = var.fmc_regkey
    type = "Device"
    access_policy {
        id = fmc_access_policies.access_policy.id
        type = fmc_access_policies.access_policy.type
    }
}