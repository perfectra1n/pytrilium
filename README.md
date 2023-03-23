# Pytrilium

This is just a place holder while I build out this API for Trilium

Here's where the API definition should be found:
https://github.com/zadam/trilium/blob/master/src/etapi/etapi.openapi.yaml

To get a quick list of currently available paths from the OpenAPI spec:
```bash
curl https://raw.githubusercontent.com/zadam/trilium/master/src/etapi/etapi.openapi.yaml 2>/dev/null | yq -e ".paths | keys"
```