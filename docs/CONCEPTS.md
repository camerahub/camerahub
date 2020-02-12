# Concepts

## Introduction

CameraHub is a database and application for cataloguing film cameras, lenses, accessories, films, negatives and prints - as well a range of other information
such as exhibitions, orders, and darkroom chemicals.

CameraHub is strictly governed by relational database principles which can make it seem fiddly and complicated to use, but this structured data gives CameraHub
its power. The data is all stored in a database backend and managed by the CameraHub app, which does its best to be helpful when adding data and hopefully hide
most of the sharp edges from the user. This guide tries to explain the key concepts behind CameraHub. There are also some [screenshots](SCREENSHOTS.md) to
illustrate how to use CameraHub.

## User data

Out of the box, CameraHub is mostly empty, ready for you to enter your own data. However if you install CameraHub in the recommended way, it comes with some pre-
filled data e.g. about manufacturers, film emulsions, film sizes, metering modes, etc, to get you up and running faster. In many cases you'll want to add to
this data to suit your own needs but you shouldn't need to edit anything that already exists.

Normally, you shouldn't need to go out of your way to add this type of data, as CameraHub will prompt you if you need to add it inline while adding cameras,
lenses, films, etc.

### Unique identifiers

Every object registered in CameraHub (e.g. camera, lenses, films, negatives, etc) is allocated a unique ID number, starting at 1 and counting up. This number is
used to reference other objects. This number is often prefixed with a `#` for readability, e.g. _Film #99_.

One exception where alternative naming is also used is for negatives. A negative might have an ID of #100 but it may also be referred to in the format 18/6,
where 18 is the ID number of the film it belongs to, and 6 is the number of the frame, separated by a forward slash. This alternative system makes it easier
to handle negatives in the darkroom.

### Camera and lens models

CameraHub makes the distinction between a camera model (any model of camera or lens that exists) and a camera or lens that is actually in your collection. This
is because it is possible for you to own two cameras of the same model, and saves having to duplicate much of the information.

Camera and lens models are the central component of CameraHub. Camera and lens models can relate to each other in one of two ways:

* directly, for fixed-lens cameras (e.g. compacts)
* via a lens mount, for interchangeable-lens cameras (e.g. SLRs)

### Cameras and lenses

You will be guided through questions when adding a new camera or lens. When adding a fixed-lens camera you will be asked to give details about the lens at the
same time, which is then associated only with that camera. When adding an interchangeable-lens camera, you only specify the lens mount. You can add
interchangeable lenses separately, which are then available to use with any camera with the same mount.

Cameras and lenses have properties of different types. Some are text (like the model name), some are numerical (like the maximum aperture of a lens), some are
yes/no (like whether a lens has autofocus) and some are multiple choice (like the different metering modes a camera supports).

### Films and negatives

If you use the cameras and lenses to take photographs, you'll want to start entering information about films and negatives into CameraHub. The word _negatives_
is a bit misleading as it refers to any image taken with a camera, including slides - which are positive!

CameraHub lets you record a stash of films, which you can then load into a camera. Films are associated with a camera. They can be developed with a developer and
archived in an archive.

When you take pictures, we recommend you take notes about your exposures using a smartphone app, a piece of paper, or what ever method suits you. Then you can
enter the data into CameraHub at a later date. Negatives are associated with films and inherit some of their properties from the film they belong to.

Negatives are also associated with a lens, as on many cameras it is possible to change lens between exposures.

### Prints

Whether you have a darkroom, or you get your negatives printed at a lab, CameraHub can track your prints. Prints are associated with the negative they were made
from. You'll be able to add other info about how the print was made.

You can also record orders for prints and record sales.

### Scans and tagging

Scans refer to digital versions of negatives, slides or prints that can be made with a scanner or a digital camera. Each negative/slide/print can be scanned
more than once. Each scan must be recorded separately.

In a future version of CameraHub, this app will introduce an API that can be used by a client-side tagger to tag your JPG scans.

### Accessories

CameraHub allows you to track your collection of camera and lens accessories, too. There are several "special" kinds of accessories that have their own
properties, commands and relationships, and there are general accessories with no special properties. You can create your own types of general accessory.

Special types of accessory with their own properties include:

* battery
* filter
* filter adapter
* flash
* meter
* mount adapter
* projector
* teleconverter

Types of general accessory with no special properties could include cases or straps. General accessories can be associated with cameras or lenses, or neither.

### Series

A series is a group of camera models and/or lens models. An example of a series could be _Canon T-series_, and it could contain camera models such as the _Canon
T80_ and _Canon T90_. Series are designed to provide visibility of camera and lens models that exist, and could be added to the collection. It is possible to
create custom series and they can be used for any purpose to help you keep track of your collection. A camera or lens model can belong to more than one series
and a series can contain a mixture of camera and lens models.
