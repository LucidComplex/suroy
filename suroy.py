#!/bin/env python
import room
import os


def load_rooms(directory):
    rooms = os.scandir(directory)
    room_dict = {}
    for room_data in rooms:
        if room_data.is_file() and room_data.name.endswith('.rdf'):
            room_dict[room_data.name[:-4]] = room.Room(room_data)

    return room_dict
