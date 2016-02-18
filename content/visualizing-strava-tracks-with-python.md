Title: Visualizing Strava Tracks with Python
Date: 2015-01-22
Category: dev
Tags:
Summary: ![Visualizing Strava Tracks with Python]({filename}/img/visualizing-strava-tracks-with-python/summary.png)
Slug: visualizing-strava-tracks-with-python
Authors: AK


I love using [Strava](http://www.strava.com) to track of my biking and snowboarding. While I rarely compete with the hoards of people who are much faster than I am (or are using [DigitalEPO](http://www.digitalepo.com/)), I do like to compare my times against my own PR's.

Strava generally does a nice job of allowing you to explore individual activities, but no method exists for simultaneously visualizing multiple activities. I commonly ride the same trails but slightly vary my route. Take the ride below for example: this represents one of perhaps a dozen different rides I've done on this same trail system. It would be nice to visualize where I ride the most and where I ride the least.

![Strava's activity overview]({filename}/img/visualizing-strava-tracks-with-python/strava.png)

Thankfully, Strava makes it really easy to export raw position data from completed activities as GPX files. GPX (GPS Exchange Format) is an XML data format for GPS data. The GPX format is able to describe waypoints, tracks, and routes. Strava uses tracks to store activity position data as follows:

    :::xml
    <gpx>
      <trk>
        <trkseg>
          <trkpt lat="DD.ddd" lon="DD.ddd">
	        <ele>MMM.mm</ele>
            <time>YYY-MM-DD HH:MM:SS</time>
          </trkpt>
          ...
        </trkseg>
      </trk>
    </gpx>




We'll make use of two Python libraries here: [`gpxpy`](https://pypi.python.org/pypi/gpxpy/0.8.8) to read GPX files into Python and `matplotlib` to for plotting figures. First, let's load an activity into Python:

    :::python
    import gpxpy
    import matplotlib.pyplot as plt

    gpx_file = open('20140918-LPQ-Ride.gpx', 'r')
    gpx = gpxpy.parse(gpx_file)

We can then traverse the GPX data structure to extract position data. In this case, since we're only visualizing the data in 2D, there's no need to pull the elevation data along with each point.

    ::python
    lat = []
    lon = []

    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                lat.append(point.latitude)
                lon.append(point.longitude)

Finally, `matplotlib` allows us to plot the activity:

    :::python
    fig = plt.figure(facecolor = '0.05')
    ax = plt.Axes(fig, [0., 0., 1., 1.], )
    ax.set_aspect('equal')
    ax.set_axis_off()
    fig.add_axes(ax)
    plt.plot(lon, lat, color = 'deepskyblue', lw = 0.2, alpha = 0.8)

![LPQ ride on Sept. 18, 2014]({filename}/img/visualizing-strava-tracks-with-python/lpq-single.png)

The resulting plot, unsurprisingly, looks like the track we saw on Strava's web app (above). This little bit of code provides the foundation for exploring and visualizing trail usage trends over time.

With a little more Python code, we can read in a bunch of Strava activities from a directory, plot them together, and save the result to a file:

    :::python
    from os import listdir
    from os.path import isfile, join
    import matplotlib.pyplot as plt
    import gpxpy

    data_path = 'lpq'
    data = [f for f in listdir(data_path) if isfile(join(data_path,f))]

    lat = []
    lon = []

    fig = plt.figure(facecolor = '0.05')
    ax = plt.Axes(fig, [0., 0., 1., 1.], )
    ax.set_aspect('equal')
    ax.set_axis_off()
    fig.add_axes(ax)

    for activity in data:
        gpx_filename = join(data_path,activity)
        gpx_file = open(gpx_filename, 'r')
        gpx = gpxpy.parse(gpx_file)

        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    lat.append(point.latitude)
                    lon.append(point.longitude)
        plt.plot(lon, lat, color = 'deepskyblue', lw = 0.2, alpha = 0.8)
        lat = []
        lon = []

    filename = data_path + '.png'
    plt.savefig(filename, facecolor = fig.get_facecolor(), bbox_inches='tight', pad_inches=0, dpi=300)

![2014 LPQ Rides]({filename}/img/visualizing-strava-tracks-with-python/lpq.png)

I made a few more for two other trail systems I commonly ride. Next up: visualizing my [Moves](http://www.moves-app.com) data.

![2014 Daley Ranch Rides]({filename}/img/visualizing-strava-tracks-with-python/daley.png)

![2014 Laguna Mountain Rides]({filename}/img/visualizing-strava-tracks-with-python/laguna.png)
