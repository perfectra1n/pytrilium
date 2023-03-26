# Pytrilium

Python SDK (wrapper, whatever you want to call it) for interacting with [Trilium's](https://github.com/zadam/trilium) ETAPI. The exact OpenAPI spec definition file that I'm trying to match can be found [here](https://github.com/zadam/trilium/blob/master/src/etapi/etapi.openapi.yaml).

You can use either your password or an ETAPI token to authenticate to the Trilium instance.



## Installation

```bash
pip install pytrilium
```

## Examples

### Using tokens or password to authenticate
Token:
```python
from pytrilium.PyTrilium import PyTrilium

pytrilium_client = PyTrilium("https://trilium.example.com", token="TTDaTeG3sadffy2_eOtgqvZoI6xHvga/6vhz61ezke1RpoX47vPI93zs5qs=")

print(pytrilium_client.get_note_content_by_id("MLDQ3EGWsU8e"))
```

Password:
```python
from pytrilium.PyTrilium import PyTrilium

pytrilium_client = PyTrilium("https://trilium.example.com", password="thisisabadpassword1")

print(pytrilium_client.get_note_content_by_id("MLDQ3EGWsU8e"))
```

### Basic Use Case

This will just print out the contents of a note, as one large string. Trilium's API returns it in the HTML format.

```python
from pytrilium.PyTrilium import PyTrilium

pytrilium_client = PyTrilium("https://trilium.example.com", token="TTDaTeG3sadffy2_eOtgqvZoI6xHvga/6vhz61ezke1RpoX47vPI93zs5qs=")

print(pytrilium_client.get_note_content_by_id("MLDQ3EGWsU8e"))
```

Export a note to a file

```python
from pytrilium.PyTrilium import PyTrilium

test_client = PyTrilium("https://trilium.example.com", token="TTDaTeG3sadffy2_eOtgqvZoI6xHvga/6vhz61ezke1RpoX47vPI93zs5qs=")

print(test_client.get_note_content_by_id("MLDQ3EGWsU8e"))

test_client.export_note_by_id("MLDQ3EGWsU8e", "./test.zip")
```

### More Advanced

If I'm braindead or this just doesn't do what you want it to, you can still use the underlying `requests.Session` that I've set up so that you can still interact with the API. This way you can still make manual requests if you would like to, and do whatever you would like with them.

To print out a Note's content without using other helpers -

```python
from pytrilium.PyTrilium import PyTrilium

pytrilium_client = PyTrilium("https://trilium.example.com", token="TTDaTeG3sadffy2_eOtgqvZoI6xHvga/6vhz61ezke1RpoX47vPI93zs5qs=")

resp = pytrilium_client.make_request('notes/<noteid>/content')
print(resp.text)
```

## Currently implemented functions
```
attempt_basic_call
auth_login
auth_logout
clean_url
create_note
create_note_revision
delete_branch_by_id
delete_note_by_id
export_note_by_id
get_attribute_by_id
get_branch_by_id
get_days_note
get_inbox_note
get_months_note
get_note_by_id
get_note_content_by_id
get_weeks_note
get_year_note
make_request
make_requests_session
patch_branch_by_id
patch_note_by_id
post_attribute
post_branch
print_custom_functions
put_note_content_by_id
refresh_note_ordering
set_session_auth
valid_response_codes
```

## Misc
To get a quick list of currently available paths from the OpenAPI spec (doesn't always mean what's in this package or not):

```bash
curl https://raw.githubusercontent.com/zadam/trilium/master/src/etapi/etapi.openapi.yaml 2>/dev/null | yq -e ".paths | keys"
```