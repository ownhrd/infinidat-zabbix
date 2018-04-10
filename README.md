# infinidat-zabbix
Мониторинг INFINIDAT.

* Импортировать скрипт `infinibox_zabbix.py` в `/usr/lib/zabbix/externalscripts`
* Поменять `login` и `password` в `infinibox_zabbix.py` (r/o user в INFINIBOX)
* Поменять IP-адрес от INFINIBOX в тимплейте (макро {$INFINIBOX_IP}) `Template_InfiniBox.xml`
