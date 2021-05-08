Operations
##########

Backup
******

By console
==========

These commands can be run interactively in the dev environment or by using ``kubectl exec``::

    poetry run python manage.py dbbackup
    poetry run python manage.py mediabackup

    poetry run python manage.py dbrestore
    poetry run python manage.py mediarestore

Note: due to a `bug <https://github.com/django-dbbackup/django-dbbackup/issues/245>`_ in django-dbbackup, restoring this way
will not work for brand new deployments. Instead, you will need to exec into the pod and restore manually::

    # Substitute the random characters for your env
    kubectl exec -it camerahub-app-6944b9d746-nmlwm -- sh

    # Get name of .psql backup file
    ls backup

    # Restore it
    psql -h $CAMERAHUB_DB_HOST -p $CAMERAHUB_DB_PORT -U $CAMERAHUB_DB_USER $CAMERAHUB_DB_NAME < backup/default-camerahub-5888d6fc58-bgmxx-2021-02-03-223246.psql

By cron
=======

Kubernetes automatically creates CronJobs to make backups of the Postgres database and the media directory.
By default these CronJobs are disabled, but they can be manually run with::

    kubectl create job --from=cronjob/postgres-backup postgres-backup-manual-001
    kubectl create job --from=cronjob/media-backup media-backup-manual-001

N.B. these restore jobs automatically restore the most recent backup::

    kubectl create job --from=cronjob/postgres-restore postgres-restore-manual-001
    kubectl create job --from=cronjob/media-restore media-restore-manual-001
