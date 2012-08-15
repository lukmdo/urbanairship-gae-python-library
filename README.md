# GAE wrapper of [Urban Airship python-library](https://github.com/urbanairship/python-library)

Until the [outbound sockets](https://developers.google.com/appengine/docs/features#Roadmap_Features) are in development ([#issue1164](http://code.google.com/p/googleappengine/issues/detail?id=1164)) this

## Usage

Drop in [urbanairship python-library](https://github.com/urbanairship/python-library)

```bash
wget --no-check-certificate https://raw.github.com/urbanairship/python-library/master/urbanairship.py
```

Then import ```Airship``` from ```gae_urbanairship``` rest stays the same

```python
from gae_urbanairship import Airship

airship = Airship(application_key, master_secret)
airship.push({'aps': {'alert': 'Hello'}}, device_tokens=['device_token'])
```
