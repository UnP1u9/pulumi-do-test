# import pulumi
from pulumi import Config

config = Config()

repo_name = config.get('repo_name') or "container-repo-therapypractice"
region = config.get('region') or 'nyc3'
k8_node_size = config.get("k8_node_size") or 's-4vcpu-8gb'
bastion_size = config.get("bastion_size") or 's-1vcpu-1gb'
k8_node_count = config.get_float("k8_node_count") or 1
k8_node_count_max = config.get_float("k8_node_count_max") or k8_node_count
mysql_node_size = config.get('mysql_node_size') or 'db-s-1vcpu-1gb'
mongo_node_size = config.get('mongo_node_size') or 'db-s-1vcpu-1gb'
AWS_ACCESS_KEY_ID = config.get_secret("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY  = config.get_secret("AWS_SECRET_ACCESS_KEY")
mysql_node_count = config.get_float("mysql_node_count") or 1
mongo_node_count = config.get_float("mongo_node_count") or 1
# mysql_node_size must be greater thean 1vcpu if mysql_node_count > 1
# https://docs.digitalocean.com/reference/api/api-reference/#tag/Databases
dockerconfigjson = config.get_secret("dockerconfigjson")