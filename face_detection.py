#!/usr/bin/env python

# Copyright 2015 Google, Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Draws squares around faces in the given image."""

import argparse
import base64

from PIL import Image
from PIL import ImageDraw

from googleapiclient import discovery
import httplib2
from oauth2client.client import GoogleCredentials
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './auth.json'


# [START get_vision_service]
DISCOVERY_URL='https://vision.googleapis.com/$discovery/rest?version=v1'


def get_vision_service():
    credentials = GoogleCredentials.get_application_default()
    return discovery.build('vision', 'v1', credentials=credentials,
                           discoveryServiceUrl=DISCOVERY_URL)
# [END get_vision_service]


# [START detect_face]
def detect_face(face_file, max_results=4):
    """Uses the Vision API to detect faces in the given file.
    Args:
        face_file: A file-like object containing an image with faces.
    Returns:
        An array of dicts with information about the faces in the picture.
    """
    image_content = face_file.read()
    batch_request = [{
        'image': {
            'content': base64.b64encode(image_content).decode('UTF-8')
            },
        'features': [{
            'type': 'FACE_DETECTION',
            'maxResults': max_results,
            }]
        }]

    service = get_vision_service()
    request = service.images().annotate(body={
        'requests': batch_request,
        })
    response = request.execute()
    return response['responses'][0]['faceAnnotations']
# [END detect_face]

# [START print_landmarks]
def print_landmarks(face):
    """prints out landmark results for a face object"""
    coordinates = list()
    for landmark in face['landmarks']:
        # print landmark['type']
        # print 'x: ' + str(landmark['position']['x'])
        # print 'y: ' + str(landmark['position']['y'])
        # print 'z: ' + str(landmark['position']['z'])
        coordinates.append(landmark['position']['x'])
        coordinates.append(landmark['position']['y'])
        coordinates.append(landmark['position']['z'])
    print coordinates
    return coordinates

    #print face['landmarks'][1]
# [END print_landmarks]

# [START highlight_faces]
def highlight_faces(image, faces, output_filename):
    """Draws a polygon around the faces, then saves to output_filename.
    Args:
      image: a file containing the image with the faces.
      faces: a list of faces found in the file. This should be in the format
          returned by the Vision API.
      output_filename: the name of the image file to be created, where the faces
          have polygons drawn around them.
    """
    im = Image.open(image)
    draw = ImageDraw.Draw(im)

    for face in faces: #assume there is only one face.
        box = [(v.get('x', 0.0), v.get('y', 0.0)) for v in face['fdBoundingPoly']['vertices']]
        draw.line(box + [box[0]], width=5, fill='#00ff00')
        print_landmarks(face)

    del draw
    im.save(output_filename)
# [END highlight_faces]

# [START main] 
def main(input_filename, max_results): #always use 1 for max_results
    with open(input_filename, 'rb') as image:
        faces = detect_face(image, max_results)
        #print('Found %s face%s' % (len(faces), '' if len(faces) == 1 else 's'))

        return print_landmarks(faces[0])
        #print('Writing to file %s' % output_filename)
        # Reset the file pointer, so we can read the file again
        #image.seek(0)
        #highlight_faces(image, faces, output_filename)
# [END main]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Detects faces in the given image.')
    parser.add_argument(
        'input_image', help='the image you\'d like to detect faces in.')
    parser.add_argument(
        '--out', dest='output', default='out.jpg',
        help='the name of the output file.')
    parser.add_argument(
        '--max-results', dest='max_results', default=4,
        help='the max results of face detection.')
    args = parser.parse_args()

    main(args.input_image, args.output, args.max_results)
