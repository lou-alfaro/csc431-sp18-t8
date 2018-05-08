# Copyright 2015 Google Inc.
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

from register import get_model, storage
from flask import Blueprint, current_app, redirect, render_template, request, \
    url_for
#from PIL import Image, ImageFilter
#import os
#import gdal
#import urllib, cStringIO
#import json

crud = Blueprint('crud', __name__)


# [START upload_image_file]
def upload_image_file(file):
    """
    Upload the user-uploaded file to Google Cloud Storage and retrieve its
    publicly-accessible URL.
    """
    if not file:
        return None

    public_url = storage.upload_file(
        file.read(),
        file.filename,
        file.content_type
    )

    current_app.logger.info(
        "Uploaded file %s as %s.", file.filename, public_url)

    return public_url
# [END upload_image_file]

@crud.route("/")
def list_raw():
    token = request.args.get('page_token', None)
    if token:
        token = token.encode('utf-8')

    maps, next_page_token = get_model().list_raw(cursor=token)

    return render_template(
        "list.html",
        maps=maps,
        next_page_token=next_page_token)

@crud.route("/tiff")
def list_tiff():
    token = request.args.get('page_token', None)
    if token:
        token = token.encode('utf-8')

    maps, next_page_token = get_model().list_tiff(cursor=token)

    return render_template(
        "list.html",
        maps=maps,
        next_page_token=next_page_token)

@crud.route('/<id>')
def view(id):
    map = get_model().read_raw(id)
    if not map:
        map = get_model().read_tiff(id)

    return render_template("view.html", map=map)




@crud.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        data = request.form.to_dict(flat=True)

        # If an image was uploaded, update the data to point to the new image.
        # [START image_url]
        image_url = upload_image_file(request.files.get('image'))
        # [END image_url]

        # [START image_url2]
        if image_url:
            data["imageUrl"] = image_url
        # [END image_url2]

        map = get_model().create_raw(data)

        return redirect(url_for('.view', id=map['id']))

    return render_template("form.html", action="Add", map={})

@crud.route('/<id>/convert', methods=['GET', 'POST'])
def convert(id):
    map = get_model().read_raw(id)
    if not map:
        map = get_model().read_tiff(id)

    if request.method == 'POST':
        #inFile = Image.open(cStringIO.StringIO(urllib.urlopen(map['imageUrl']).read()))

        #gdalString = "gdal_translate " + str(inFile) + " " + "-of GTiff " + str(inFile) + ".tif"
        #os.system(gdalString)
        data = request.form.to_dict(flat=True)

        image_url = upload_image_file(request.files.get('image'))

        if image_url:
            data['imageUrl'] = image_url

        map = get_model().update_raw(data, id)

        return redirect(url_for('.view', id=map['id']))

    return render_template("reference.html", action="Edit", map=map)

@crud.route('/<id>/coord', methods=['GET', 'POST'])
def coord(id):
    map = get_model().read_raw(id)
    if not map:
        map = get_model().read_tiff(id)

    if request.method == 'POST':
        data = request.form.to_dict(flat=True)

        points = map["refPoints"]

        if points:
            map["refPoints"].append(data)
        else:
            map["refPoints"] = [data]

        return redirect(url_for('.registration', id=map['id']))

    return render_template("coord.html", action="Edit", map=map)


@crud.route('/<id>/delete')
def delete(id):
    get_model().delete(id)
    return redirect(url_for('.list'))
