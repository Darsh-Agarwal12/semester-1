# Week 1.6, Session 1: Task 5

from datetime import datetime

from feed import QuakeFeed
from quake import Quake


class QuakeDatasetError(Exception):
    """
    An exception type for errors involving QuakeDataset.
    """
    pass


class QuakeDataset:
    """
    An earthquake dataset obtained from a USGS data feed.
    """

    def __init__(self, feed):
        """
        Creates an empty dataset, linked to a specific data feed.
        """
        if not isinstance(feed, QuakeFeed):
            raise TypeError("feed must be specified as a QuakeFeed object")

        self.feed = feed
        self.data = []

    def read_feed(self):
        """
        Refreshes this dataset with data from the linked feed.

        The new data replaces any existing data.
        """
        # Write code here to replace existing data with new earthquake data.
        # Use the value returned by the feed's reader() method as the
        # subject of a for loop.

        # Keep in mind that the items obtained by this for loop will be
        # dictionaries. You will need to extract the required values from
        # each dictionary and convert them into the required types before
        # creating a Quake object and storing it in the list.

        self.data = []
        for item in self.feed.reader():
            time_text = item['time'].replace('Z', '')
            time_obj = datetime.fromisoformat(time_text)
            quake = Quake(
                time_obj,
                float(item['latitude']),
                float(item['longitude']),
                float(item['depth']),
                float(item['mag'])
            )
            # Add it to our list
            self.data.append(quake)
        

    def __len__(self):
        """
        Returns the size of this dataset.
        """
        # Write code here that returns the number of quakes downloaded
        return len(self.data)

    def __str__(self):
        """
        Returns information on this dataset as a string.
        """
        # Write code here to create and return a string representation
        # (Include number of quakes and details of the feed that was used)
        return f"{len(self.data)} quakes, from {self.feed}"

    def mean_depth(self):
        """
        Returns the mean depth of the quakes in this dataset.
        """
        if len(self.data) == 0:
            raise QuakeDatasetError("dataset is empty")

        total = sum(quake.depth for quake in self.data)
        return total / len(self.data)

    def mean_magnitude(self):
        """
        Returns the mean magnitude of the quakes in this dataset.
        """
        # Write code here that computes the mean magnitude of all the
        # quakes currently in the dataset
        if len(self.data) == 0:
            raise QuakeDatasetError("dataset is empty")

        total = sum(quake.magnitude for quake in self.data)
        return total / len(self.data)

    def shallowest_quake(self):
        """
        Returns details of the shallowest quake in this dataset.
        """
        if len(self.data) == 0:
            raise QuakeDatasetError("dataset is empty")

        shallowest = self.data[0]
        for quake in self.data[1:]:
            if quake.depth < shallowest.depth:
                shallowest = quake
        return shallowest

    def strongest_quake(self):
        """
        Returns details of the strongest quake in this dataset.
        """
        # Write code here that finds and returns the strongest quake
        # (i.e., the one with the largest magnitude)
        if len(self.data) == 0:
            raise QuakeDatasetError("dataset is empty")

        strongest = self.data[0]
        for quake in self.data[1:]:
            if quake.magnitude > strongest.magnitude:
                strongest = quake
        return strongest

    def deepest_quake(self):
        """
        Returns details of the deepest quake in this dataset.
        """
        if len(self.data) == 0:
            raise QuakeDatasetError("dataset is empty")

        deepest = self.data[0]
        for quake in self.data[1:]:
            if quake.depth > deepest.depth:
                deepest = quake
        return deepest

    def weakest_quake(self):
        """
        Returns details of the weakest quake in this dataset.
        """
        if len(self.data) == 0:
            raise QuakeDatasetError("dataset is empty")

        weakest = self.data[0]
        for quake in self.data[1:]:
            if quake.magnitude < weakest.magnitude:
                weakest = quake
        return weakest

    def format_quakes(self):
        """
        Returns a formatted table, each containing details of a quake.
        """
        if len(self.data) == 0:
            raise QuakeDatasetError("dataset is empty")

        # Write code here that creates a formatted table of quakes
        # (i.e., a string with one line per quake, each line containing
        # the time, latitude, longitude, depth and magnitude of the quake)
        lines = []
        for quake in self.data:
            lines.append(f"{quake.when} {quake.latitude} {quake.longitude} {quake.depth} {quake.magnitude}")
        return "\n".join(lines)

    def range_longitude_latitude(self):
        """
        Returns the details of all quakes within a specified number of degrees of a specified longitude and latitude.
        """
        

    
