# Demo Configuration Generator [![Build Status](https://travis-ci.com/NeovaHealth/demo-conf-generator.svg?token=igX7qDwhAWz4yJv1VvQp)](https://travis-ci.com/NeovaHealth/demo-conf-generator)
Super simple commandline tool to generate an Open-eObs configuration for demoing the product.

Pass it a trust name & trust status and it will create an Odoo module with the trust's logo and name configured and ready to install.

## Example usage
`new_openeobs_config --output=~/Documents --name="Colin's Amazing Healthcare" --status="NHS Trust" colin_test`

### options
 - module_name: Name of module folder
 - output: Place to output the module folder
 - name: Name of Trust
 - status: Status of Trust (NHS Trust, Foundation Trust etc)
 - email: Email for Trust
 - website: Website for Trust