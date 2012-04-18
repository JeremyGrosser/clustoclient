# Clusto client libraries and utilities

clustohttp (the core of the client libraries) emulates the Clusto API to a limited extent with an instance of the ClustoProxy class. You must tell the ClustoProxy where you're running clusto-httpd by either passing the url argument to it's constructor, or by setting the `CLUSTO_URL` and optionally the `CLUSTO_AUTH` environment variables. `CLUSTO_URL` should be in the form `http://clusto.example.com` with no trailing slash. `CLUSTO_AUTH` should be a `username:password` if your API requires HTTP Basic authentication.

## Example redis templating

redis.conf.template:

```jinja
{% set redis_master = server.attr_value(key='redis', subkey='master', merge=True) %}
{% set redis_port = server.attr_value(key='redis', subkey='port', merge=True) %}

daemonize no
pidfile /var/run/redis.pid

{% for ip in server.attr_values(key='ip', subkey='ipstring') %}
bind {{ ip }}
{% endfor %}

{% if redis_port %}
port {{ redis_port }}
{% endif %}

{% if redis_master %}
slaveof {{ redis_master }}
{% endif %}
```

Generating the config:

```shell
export CLUSTO_URL=http://clusto.example.com
export CLUSTO_AUTH=username:password
clusto-template -r . redis.conf.template /etc/redis.conf
```
