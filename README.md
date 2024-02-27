[![codecov](https://codecov.io/gh/trpubz/MTBL_DriverKit/graph/badge.svg?token=LJBMG3P28W)](https://codecov.io/gh/trpubz/MTBL_DriverKit)
[![Python package](https://github.com/trpubz/MTBL_DriverKit/actions/workflows/python-package.yml/badge.svg?branch=feat%2Fupgrade-py3-12-1)](https://github.com/trpubz/MTBL_DriverKit/actions/workflows/python-package.yml)
# MTBL DriverKit

## Installation
This was packaged with poetry, to install with `pip install` ensure that `MTBL-DriverKit @ git+https://github.com/trpubz/MTBL_DriverKit.git@v0.4.0` syntax is located in requirements.txt

## Dependencies
* selenium>='4.16'
  * as of Selenium v4.0, Selenium Manager handles driver install/handling
* You need to have Chrome installed for this package work off the shelf.

## Requirements
* you must have io read/write authority in the directory you want to run this package from

## Usage
`from mtbl_driverkit import mtbl_driverkit as DK` in the file you wish
