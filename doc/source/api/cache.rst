Cache
===============================================

**b2sdk** caches the mapping between bucket name and bucket
id, so that the user of the library does not need to maintain
the mapping to call the api.


.. autoclass:: b2sdk.v1.AbstractCache

.. autoclass:: b2sdk.v1.AuthInfoCache()
   :special-members: __init__

.. autoclass:: b2sdk.v1.DummyCache()
   :special-members: __init__

.. autoclass:: b2sdk.v1.InMemoryCache()
   :special-members: __init__
