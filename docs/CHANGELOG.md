# Changelog

## `0.1.0`

14 Oct 2019

* First stable release

## `0.1.1`

23 Oct 2019

* Add owner field to various user-specific models for future multi-user support (#107)
* Drop support for movies, digital cameras & filter adapters (#109)
* Roll lightmeter and projector into generic accessories (#109)
* Add patchy support for Kubernetes (#112)

## `0.1.2`

25 Oct 2019

* Run PhotoDB in uwsgi and serve static content
* Reduce Docker image size
* Create various env vars to configure PhotoDB
* Various improvements to Kubernetes manifests

## `0.1.3`

25 Oct 2019

* Add libpq at runtime

## `0.1.4`

25 Oct 2019

* Use correct var for production mode

## `0.1.5`

21 Jan 2020

* Final release of 0.1.x series to validate CI

## `0.2.0`

18 Feb 2020

* Add activation step for user sign-ups (#176)
* Add password reset functionality (#177)
* Add moderation of public data (#172)
* Add 'About' page (#192)
* Rework secrets (#187)
* Use StatefulSet to run resilient Postgres database (#193)

## `0.2.1`

19 Feb 2020

* Make Django be aware of its own hostname/domain (#189)
* Set "from" email address (#189)
* Use absolute URL in email templates (#189)

## `0.3.0`

25 Feb 2020

* Update styling and add nav bar (#178, #197)
* Add disambiguation to camera model & lens model (#199)
* Shortcut static pages with views (#160)
* Make model headings clickable (#205)
* Collapsing subsections for inlines and actions (#131)
* Implement daily database backups in prod (#203)
* Swap PNG graphics for SVGs (#200)
* Add basic stats page (#142)
* Add homepage beta banner and jumbotron (#217)
* Temporarily disable moderation until it works (#202)

## `0.3.1`

2 Mar 2020

* Require disambiguation for models with the same name (#221)
* Fix backup manifest
* Fix typo in doc

## `0.3.2`

4 Mar 2020

* Add Help section with basic docs (#194)
* Restyle camera model and lens model detail views (#133 and #136)
* Restyle Edit link (#225)
* Restyle Add link (#214 and #226)
