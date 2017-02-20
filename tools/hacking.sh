#!/bin/bash
flake8 kmclient | tee flake8.log
exit ${PIPESTATUS[0]}
