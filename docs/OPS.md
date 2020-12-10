# Operations

## Backup

### By console

These commands can be run interactively in the dev environment or by using `kubectl exec`

```
poetry run python manage.py dbbackup
poetry run python manage.py mediabackup
```

```
poetry run python manage.py dbrestore
poetry run python manage.py mediarestore
```

### By cron

Kubernetes automatically creates CronJobs to make backups of the Postgres database and the media directory.
By default these CronJobs are disabled, but they can be manually run with

```
kubectl create job --from=cronjob/postgres-backup postgres-backup-manual-001
kubectl create job --from=cronjob/media-backup media-backup-manual-001
```

N.B. these restore jobs automatically restore the most recent backup

```
kubectl create job --from=cronjob/postgres-restore postgres-restore-manual-001
kubectl create job --from=cronjob/media-restore media-restore-manual-001
```
