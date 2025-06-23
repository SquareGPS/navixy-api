# Table of contents

* [README](README.md)
* [Overview](overview.md)
* [Authentication](authentication.md)
* [Getting started](getting-started.md)
* [Technical reference](technical-reference.md)

## Guides

* [Activating a GPS device](guides/activating-a-gps-device.md)
* [Creating a custom asset](guides/creating-a-custom-asset.md)
* [Configuring an asset link](guides/configuring-an-asset-link.md)

## Endpoint Reference

* ```yaml
  type: builtin:openapi
  props:
    models: true
  dependencies:
    spec:
      ref:
        kind: openapi
        spec: navixy-repo
  ```
