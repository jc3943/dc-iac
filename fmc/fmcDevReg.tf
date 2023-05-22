#Jeff Comer

#resource "fmc_access_policies" "access_policy" {
#    name = "FMC Access Policy"
    # default_action = "block" # Cannot have block with base IPS policy
#    default_action = "permit"
#}

data "fmc_access_policies" "access_policy" {
    name = "FTD"
}

resource "fmc_devices" "dcloud_ftd" {
    name = var.fmc_ftd1_name
    hostname = var.fmc_ftd1
    regkey = var.fmc_regkey
    type = "Device"
    access_policy {
        id = data.fmc_access_policies.access_policy.id
        type = data.fmc_access_policies.access_policy.type
    }
}