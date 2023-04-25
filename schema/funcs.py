from math import degrees
from itertools import chain, count
from re import match
from decimal import Decimal
from django.utils.safestring import mark_safe
from numpy import arctan


def boolicon(obj):
    img = '<img src="/static/svg/{}.svg" width="30" height="30" alt="{}" title="{}">'
    if obj is not None:
        if bool(obj):
            return_value = mark_safe(img.format('yes', 'Yes', 'Yes'))  # pylint: disable=consider-using-f-string
        else:
            return_value = mark_safe(img.format('no', 'No', 'No'))  # pylint: disable=consider-using-f-string
    else:
        return_value = None

    return return_value


def colouricon(obj):
    img = '<img src="/static/svg/{}.svg" width="30" height="30" alt="{}" title="{}">'
    if obj is not None:
        if bool(obj):
            return_value = mark_safe(img.format('colour', 'Colour', 'Colour'))  # pylint: disable=consider-using-f-string
        else:
            return_value = mark_safe(img.format('bw', 'Black & White', 'Black & White'))  # pylint: disable=consider-using-f-string
    else:
        return_value = None

    return return_value


def locationicon(obj):
    img = '<img src="/static/svg/{}.svg" width="30" height="30" alt="{}" title="{}">'
    if obj is not None:
        if bool(obj):
            return_value = mark_safe(img.format('location', 'Location', 'Location'))  # pylint: disable=consider-using-f-string
        else:
            return_value = 'None'
    else:
        return_value = None

    return return_value


def angle_of_view(diag, focal):
    # fov = 2 arctan (d / 2f)
    if diag is not None and focal is not None:
        angle = round(degrees(2 * arctan(float(diag) / (2*float(focal)))))
    else:
        angle = None
    return angle


def to_dict(instance):
    opts = instance._meta
    data = {}
    for field in chain(opts.concrete_fields, opts.private_fields):
        data[field.name] = field.value_from_object(instance)
    for field in opts.many_to_many:
        data[field.name] = [i.id for i in field.value_from_object(instance)]
    return data


def canondatecode(datecode, introduced=1960, discontinued=2100):
    """Decode Canon datecodes to discover the year of manufacture. Datecodes are sometimes ambiguous so by passing in the dates
    that the model was introduced and discontinued, the year of manufacture can be pinned down
    """

    # While there are non-None defaults for these values in this function, the calling code
    # always passes the variable, even if it is None. So passing in None will override the default
    # value at the top of the function. So here we check for None values and set a default if necessary.
    if introduced is None:
        introduced = 1960

    if discontinued is None:
        discontinued = 2100

    # Initialise empty list of candidate dates
    guesses = []

    # AB1234, B1234A, B123A
    # From 1960-2012, the date code is in the form of "AB1234". "A" indicates the factory. Prior to 1986, "A" is moved to the end.
    # "B" is a year code that indicates the year of manufacture. Canon increments this letter each year starting with A in 1960
    # Of the 4 digits, the first two are the month of manufacture. Sometimes the leading 0 is omitted.
    oldstyle = match(r"^[A-Z]?([A-Z])[0-9]{3,4}[A-Z]?$", datecode.upper())

    # From 2008, the date code is 10 digits. The first two correspond to the year & month of manufacture.
    # From 2008-2012 the month code runs from 38-97. In 2013, it is reset to 01. These are treated as different epochs.
    newstyle = match(r"^(\d{2})\d{8}$", datecode.upper())

    if oldstyle:
        dateletter = oldstyle.group(1)
        epochstart = 1960
        epochend = 2012

        # Calculate datenumber as years since epoch
        datenumber = ord(dateletter) - ord('A')

        # Find all years within an epoch that a letter could represent
        for i in count(0):
            guess = epochstart + datenumber + i*26

            # Stop if we go above the end date of the datecode epoch
            if guess > epochend:
                break

            # Add our guess to the list
            guesses.append(guess)
            print(guess)

    elif newstyle:
        datenumber = newstyle.group(1)

        # First epoch
        if 38 <= datenumber <= 97:
            epochstart = 2008
            epochend = 2012
            start = 38

            guess = epochstart + int((datenumber - start) / 12)
            guesses.append(guess)

        # Second epoch
        else:
            epochstart = 2013
            epochend = 2100
            start = 1

            # Find all years within an epoch that a letter could represent
            for i in count(0):
                guess = epochstart + int(((datenumber + i*100) - start) / 12)
                if guess > epochend:
                    break
                guesses.append(guess)

	# Now examine our guesses for plausibility based on when the lens was released & discontinued
    plausible = []
    for guess in guesses:
        # Skip if our guess is before the lens was introduced
        if guess < introduced:
            continue
        # Stop if our guess is after the lens was discontinued
        if guess > discontinued:
            continue
        plausible.append(guess)

    # If we narrowed it down to one year, return that. Otherwise, return nothing.
    if len(plausible) == 1:
        year = plausible[0]
    else:
        year = None

    return year

def deg_to_dms(decdegrees):
    """
    Convert from decimal degrees to degrees, minutes, seconds.
    """
    decdegrees = Decimal(decdegrees)
    # Multiply degrees up 3600 to get integer second resolution, divide by 60 to get mins and secs
    mins, secs = divmod(abs(decdegrees)*3600, 60)
    # Further divide by 60 to get degrees and mins
    degs, mins = divmod(mins, 60)
    # round down degs and mins. Secs remains a float
    degs, mins = int(degs), int(mins)
    return degs, mins, secs


def deg_to_dms_rational(decdegrees):
    """
    Convert from decimal degrees to degrees, minutes, seconds expressed as rationals
    This returns 3 rationals formatted as a string suitable for pyexiv2, e.g.
    'Exif.GPSInfo.GPSLatitude': '51/1 27/1 3148/100'
    """
    (degs, mins, secs) = deg_to_dms(decdegrees)
    # As secs is a float, we multiply by 100 for increased precision in the rational
    roundedsecs = round(secs * 100)
    return f"{degs}/1 {mins}/1 {roundedsecs}/100"


def gps_ref(direction, angle):
    """
    Return the direction of a GPS coordinate
    """
    angle=Decimal(angle)
    if direction == 'latitude':
        hemi = 'N' if angle>=0 else 'S'
    elif direction == 'longitude':
        hemi = 'E' if angle>=0 else 'W'
    else:
        hemi = None
    return hemi
