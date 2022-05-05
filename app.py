import os.path

from flask import Flask, request, current_app
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from xml.etree.ElementTree import parse, ParseError
import secrets

app = Flask(__name__)


class UploadForm(FlaskForm):
    upload_file = FileField(validators=[FileAllowed(['xml'])])

@app.post('/iatidoc')
def post_doc():
    upload_form = UploadForm()
    if upload_form.validate_on_submit():
        file = upload_form.upload_file.data
        try:
            tree = parse(file.filename)
            root_tag = tree.getroot().tag
            if root_tag == 'iati-activities':
                random_hex = secrets.token_hex(8)
                _, file_ext = os.path.splitext(file.filename)
                new_filename = random_hex + file_ext
                save_dir = os.path.join(current_app.root_path, 'static/files')
                file_path = os.path.join(save_dir, new_filename)
                file.save(file_path)
                return new_filename
            return 'Invalid xml file'
        except ParseError:
            # Invalid xml file
            return 'Invalid doc'
            pass


if __name__ == '__main__':
    app.run()
