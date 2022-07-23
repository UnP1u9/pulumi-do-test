import pulumi_digitalocean as do


mysql_cluster = do.DatabaseCluster("mysql",
                                   name="mysql",
                                   engine="mysql",
                                   node_count="1",
                                   region="nyc3",
                                   size="db-s-1vcpu-1gb",
                                   version="8",
                                   )

mysql_read_replica = do.DatabaseReplica("mysql-read-replica",
        name="mysql-read-replica",
        cluster_id=mysql_cluster.id,
        size="db-s-1vcpu-1gb",
    region="nyc3")


db_fw = do.DatabaseFirewall("db-fw",
                            cluster_id=mysql_cluster.id,
                            rules=[
                                do.DatabaseFirewallRuleArgs(
                                type="ip_addr",
                                value="8.8.8.8",
                            ), ])

db_fw_ro = do.DatabaseFirewall("db-fw-ro",
                            cluster_id=mysql_read_replica.id,
                            rules=[
                                do.DatabaseFirewallRuleArgs(
                                type="ip_addr",
                                value="8.8.8.8",
                            ), ])