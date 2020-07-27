#!/usr/bin/env bash

export ENABLE_PDF_EXPORT=1
mkdocs build --clean --strict --use-directory-urls --site-dir ./.site