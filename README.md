NoApi (in beta)
===============

For when you want to have part of your program be executed on a different machine, and it would seem dumb to make a whole-ass API for literally every internal action.

With NoApi you can simply use objects and variables that exist on a remote machine as if they were working locally.


See what I mean
---------------

On one device:

    import noapi
    noapi.Node(1234, namespace=__import__(__file__))
    
    some_object = SomeClass()


On another:

    import noapi
     noapi.Node(port=1234, namespace=__import__(__file__))

    backend = noapi.Remote(1234, 'whatever ip').control_portal
    
    print(backend.some_object.foo)
    backend.some_object.bar.some_method('args', 'work', 'too')


So you can use your remotely running backend just the same as if it was an imported package (here called 'backend')


Use at your own risk tho
------------------------

This library is not really in active development or secure in the slightest. Also the only documentation is this readme but usage is pretty simple.
