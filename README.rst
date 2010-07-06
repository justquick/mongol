Mongol
======

:Authors:
   Justin Quick <justquick@gmail.com>
:Version: 0.1


::

    pip install mongol==0.1.0

Mongol is a web analytics tool to let you track your site's traffic and generate custom reports.
It uses MongoDB as the datastore and Python with pymongo to populate and query the database.
It uses standard WSGI to gather analytics information and serve a tracking GIF pixel.
Custom analytics data can be tossed at the service and you can then make custom reports to track pretty much anything you want.
This project is perfect at answering questions like *"What are the top 10 most viewed pages?"*

Requirements
--------------

Mongol requires `pymongo <http://api.mongodb.org/python/1.7+/api/pymongo/>`_ to connect to a `MongoDB <http://www.mongodb.org/>`_ instance.
For the serivce, it is recomended to use with `Gevent <http://www.gevent.org/>`_ but it also works with `Tornado <http://www.tornadoweb.org/>`_ and even `Apache <http://httpd.apache.org/>`_/`mod_wsgi <http://code.google.com/p/modwsgi/>`_.
Here is the recomended list of requirements::

    sudo pip install pymongo gevent
    
Install
--------

Setup and install MongoDB. Here is their `quickstart guide <http://www.mongodb.org/display/DOCS/Quickstart>`_.
Next, download the source code and install the scripts::

    git clone git://github.com/justquick/mongol.git
    cd mongol
    sudo python setup.py install


``mongol-serve``
-----------------

::

    mongol-serve [address:port]
    
Starts the service instance at the optional address and port. Defaults to host at 0.0.0.0:8000.
This service hosts the tracking GIF but you can pass any sort of analytics data as ``GET`` parameters.
The only two required parameters are 1) ``site`` which is the domain of your site and 2) ``url`` which is the absolute URL of the page you wish to track.
``site`` and ``url`` will be populated if ``HTTP_REFERER`` which the browser sends as the page that the tracking GIF was found on.
Any other ``GET`` parameters are stored for later use.

``mongol-report``
-----------------

::

    mongol-report config-file
    
Generates JSON reports from the analytics database based on the configuration parameters found in the ``config-file`` filename argument.
This is best put on a cronjob so that the generated reports are up to date.
Report files can be served up by a separate service (ideally `lighttpd <http://www.lighttpd.net/>`_) so that the analytics service doesnt get clogged up by serving the reports.

Configuration Options
----------------------

Configuration files contain sections of reports to generate when you run ``mongol-report``.
Each section name will generate one report file called ``section-name.json``.
Here are the options for each section:

 * ``output`` - required string. The output directory to store files in (eg ``~/mongol/reports``)
 * ``time`` - optional string. Time at which to remove older records (eg ``days:2``). Mongol is really suited to look at data in the past X amount of time and removes any records that were recorded before then. By default it does not do any limiting.
 * ``callback`` - optional string. Function name to wrap results with creating proper JSONP reports. Defaults to ``results``.
 * ``limit`` - optional int. Limit the results in the reports. Defaults to ``10``.
 * ``order`` - optional string. Order the results. Either ``A`` for ascending or ``D`` for descending. Defaults to ``D``
 * ``mapper`` - optional string. The JS source code of the mapping function to use in MongoDB's map/reduce capabilies. Defaults to ::
 
    function () {
        emit({url:this.url, title:this.title}, this.pageviews);
    }

 * ``reducer`` - optional string. The JS source code of the reducing function to use in MongoDB's map/reduce capabilies. Defaults to ::
 
    function (key, values) {
        var total = 0;
        for (var i = 0; i < values.length; i++) {
            total += values[i];
        }
        return total;
    }

For help with the map/reduce stuff, take a look at `MongoDB's MapReduce documentation <http://www.mongodb.org/display/DOCS/MapReduce>`_

TODO
------

 * Use cookies
 * Enable MongoDB clustering support