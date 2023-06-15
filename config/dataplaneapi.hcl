config_version = 2

name = "bbaa644a628b"

mode = "single"

dataplaneapi {
  advertised {}

  scheme = ["http"]
}

haproxy {
  reload {
    reload_delay    = 5
    reload_cmd      = "service haproxy reload"
    restart_cmd     = "service haproxy restart"
    reload_strategy = "custom"
  }
}
